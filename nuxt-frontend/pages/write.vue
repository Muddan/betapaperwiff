<template>
  <div class="write-content">
    <v-container>
      <div class="header-section">
        <header>
          <h3 v-if="isSigned" class="main-title">
            Welcome, {{ currentUser.firstName }} !
          </h3>
          <p class="subheading">compose an epic.</p>
        </header>
      </div>
      <div class="form-section">
        <v-flex xs12 sm12 class="header-img-main">
          <image-input v-model="storyForm.headerImage" class="header-img-main">
            <div slot="activator">
              <v-container
                v-if="!storyForm.headerImage.imageURL"
                v-ripple
                height="300px"
                class="placeholder"
              >
                <v-img
                  height="300px"
                  src="~assets/images/placeholder-image.png"
                  alt=""
                />
              </v-container>
              <v-container v-else v-ripple class="bg-holder">
                <v-img
                  :src="storyForm.headerImage.imageURL"
                  alt="avatar"
                ></v-img>
              </v-container>
            </div>
          </image-input>
        </v-flex>
        <v-flex xs12 sm12>
          <v-text-field
            v-model="storyForm.title"
            required
            label="Title"
            single-line
            solo
          ></v-text-field>
        </v-flex>
        <v-flex xs12 sm12>
          <v-textarea
            v-model="storyForm.summary"
            solo
            name="input-7-4"
            label="Summary"
          ></v-textarea>
        </v-flex>

        <!-- <v-flex xs12 sm6>
          <v-select
            prepend-icon="language"
            :items="translateLanguages"
            solo
            label="Select translation language"
            @change="setLanguage"
          ></v-select>
        </v-flex>-->
        <v-flex xs12 sm12 wrap>
          <v-subheader>
            Start your story
          </v-subheader>
          <section class="editor-content">
            <div
              v-quill:myQuillEditor="editorOption"
              class="quill-editor"
              :content="storyForm.content"
              @change="onEditorChange($event)"
            >
              >
            </div>
          </section>
        </v-flex>
        <v-flex class="tags-input" sm12 xs12>
          <v-combobox
            v-model="storyForm.selectedTags"
            :items="tagsArray"
            label="Select Tags"
            chips
            clearable
            solo
            multiple
            @input="limiter"
          >
            <template v-slot:selection="data">
              <v-chip
                :selected="data.selected"
                close
                @input="remove(data.item)"
              >
                <strong>{{ data.item }}</strong
                >&nbsp;
              </v-chip>
            </template>
          </v-combobox>
        </v-flex>

        <v-btn
          :loading="publishing"
          :disabled="publishing"
          dark
          color="#337fb5"
          @click="publishStory"
        >
          Publish
          <template v-slot:loader>
            <span class="custom-loader">
              <v-icon light>cached</v-icon>
            </span>
          </template>
        </v-btn>
      </div>
    </v-container>
  </div>
</template>

<script>
import ImageInput from '@/components/Blocks/ImageInput'

import { mapGetters } from 'vuex'

export default {
  transition: 'slidedown',

  components: {
    ImageInput
  },
  middleware: 'auth',
  data() {
    return {
      file: '',
      saved: false,
      storyForm: {
        headerImage: {
          imageURL: null,
          imageFile: null
        },
        title: '',
        content: '',
        summary: '',
        translatedContent: '',
        selectedLanguage: 'english',
        selectedTags: []
      },
      validForm: true,
      loader: null,
      publishing: false,

      showEditor: false,
      editorOption: {
        modules: {
          toolbar: [
            ['bold', 'italic', 'underline', 'strike'],
            ['blockquote', 'code-block'],
            ['link'],
            [{ size: ['small', false, 'large', 'huge'] }],
            [{ list: 'ordered' }, { list: 'bullet' }],
            [{ align: [] }]
          ]
        }
      },
      translateLanguages: [
        {
          text: 'kananda'
        },
        { text: 'hindi' },
        {
          text: 'bengali'
        }
      ]
    }
  },
  computed: {
    ...mapGetters({
      isSignedIn: 'user/isSignedIn',
      currentUser: 'user/currentUser',
      storyTagsAvailable: 'stories/availableTags'
    }),
    tagsArray() {
      return this.storyTagsAvailable.map(tag => {
        return tag.name
      })
    }
  },
  created() {
    this.$on('input', function(data) {
      this.storyForm.headerImage.imageURL = data.imageURL
      this.storyForm.headerImage.imageFile = data.imageFile
    })
  },
  methods: {
    isSigned() {
      return this.isSigned
    },
    remove(item) {
      this.storyForm.selectedTags.splice(
        this.storyForm.selectedTags.indexOf(item),
        1
      )
      this.storyForm.selectedTags = [...this.storyForm.selectedTags]
    },
    onEditorChange({ quill, html, text }) {
      this.storyForm.content = html
    },
    publishStory() {
      if (!this.storyForm.title.length) {
        this.$store.dispatch('notification/warning', {
          title: 'ah Oh!',
          message: 'We need a title for your story'
        })
        this.validForm = false
      }
      if (!this.storyForm.selectedTags.length > 0) {
        this.$store.dispatch('notification/warning', {
          title: 'ah Oh!',
          message: 'Please select atleast one tag'
        })
        this.validForm = false
      }
      if (
        this.storyForm.content.length === 0 ||
        this.storyForm.content.split(' ').length > 1000
      ) {
        this.$store.dispatch('notification/warning', {
          title: 'ah Oh!',
          message: 'Please use maximum of 1000 words to finish your story.'
        })
        this.validForm = false
      }
      if (!this.isSigned) {
        this.validForm = false
      }
      if (this.validForm) {
        this.$store.dispatch('notification/progress', {
          title: 'Publishing your story...'
        })
        this.$store.dispatch('stories/publishStory', {
          storyTitle: this.storyForm.title,
          userId: this.currentUser.userId,
          content: this.storyForm.content,
          summary: this.storyForm.summary,
          tags: this.storyForm.selectedTags,
          headerImage: this.storyForm.headerImage.imageFile,
          datePublished: new Date(),
          language: this.storyForm.selectedLanguage
        })
        this.storyForm = {
          headerImage: {
            imageURL: null,
            imageFile: null
          },
          title: '',
          content: '',
          summary: '',
          translatedContent: '',
          selectedLanguage: 'english',
          selectedTags: []
        }
      }
    },
    limiter(e) {
      if (e.length > 3) {
        this.$store.dispatch('notification/warning', {
          title: 'Not allowed !',
          message: 'Please choose upto 3 tags only'
        })
        e.pop()
      }
    }
  }
}
</script>
<style lang="scss" scoped>
$logosection-color: #043344;
.write-content {
  max-width: 1400px;
  margin: auto;
}
.editor-content {
  background: #fff;
  box-shadow: 0px 3px 1px -2px rgba(0, 0, 0, 0.2),
    0px 2px 2px 0px rgba(0, 0, 0, 0.14), 0px 1px 5px 0px rgba(0, 0, 0, 0.12);
  .quill-editor {
    min-height: 200px;
    max-height: 400px;
    overflow-y: auto;
  }
}
.header-section {
  margin: 20px 0;
  padding: 20px 0;
  text-align: left;
  // color: #36789a;
  color: $logosection-color;
  overflow: hidden;
  @media (max-width: 768px) {
    padding: 0;
    margin: 0;
  }

  .main-title {
    font-family: 'Adamina', serif;
    font-size: 30px;
    font-weight: bold;
    text-transform: capitalize;
  }
}
.form-section {
  .header-img-main {
    margin: 20px 0;
    background: #f1f2f4;
    .placeholder {
      text-align: center;
      background: url('~assets/images/placeholder-image.png');
      background-size: 32%;
      background-origin: padding-box;
      background-repeat: no-repeat;
      background-position: center center;
    }
    .bg-holder {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 300px;
      width: 100%;
      padding: 0;
      overflow: hidden;
      h3 {
        width: 100%;
        text-align: center;
      }
      @media (max-width: 768px) {
        min-height: 150px;
        max-height: 150px;
      }
    }
    @media (max-width: 768px) {
      min-height: 200px;
      max-height: 200px;
    }
  }
  .content-preview-main {
    border: 1px solid #2e2e2e;
  }
  .tags-input {
    margin-top: 30px;
  }
}
</style>
