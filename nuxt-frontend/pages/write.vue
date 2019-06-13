<template>
  <div class="write-content">
    <v-container>
      <div class="header-section">
        <header>
          <span v-if="isSigned" class="main-title">
            <strong>Welcome</strong>, {{ currentUser.firstName }} !
          </span>
        </header>
        <v-subheader>compose an epic.</v-subheader>
      </div>
      <div class="form-section">
        <v-subheader>Upload an image for your post</v-subheader>
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
            label="Add Tags"
            chips
            clearable
            solo
            multiple
            :counter="3"
            hint="Select upto 3 tags"
            :persistent-hint="true"
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

          <div class="chip-container">
            <span
              v-for="(item, index) in tagsArray"
              :key="index"
              class="chip"
              @click="
                () => {
                  if (!storyForm.selectedTags.includes(item)) {
                    storyForm.selectedTags.push(item)
                    limiter(storyForm.selectedTags)
                  }
                }
              "
            >
              {{ item }}
            </span>
          </div>
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
        content: '<p></p>',
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
            [{ size: ['small', false, 'large', 'huge'] }]
            // [{ list: 'ordered' }, { list: 'bullet' }],
            // [{ align: [] }]
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
        return tag.value
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
        this.$store
          .dispatch('stories/publishStory', {
            storyTitle: this.storyForm.title,
            userId: this.currentUser.userId,
            content: this.storyForm.content,
            summary: this.storyForm.summary,
            tags: this.storyForm.selectedTags,
            headerImage: this.storyForm.headerImage.imageFile,
            datePublished: new Date(),
            language: this.storyForm.selectedLanguage
          })
          .then(res => {
            if (res && res.status === 200) {
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
              this.$router.push('/')
            }
          })
      }
    },
    limiter(e) {
      if (e.length > 3) {
        this.$store.dispatch('notification/warning', {
          title: '',
          message: 'Please choose upto 3 tags only'
        })
        e.pop()
      }
    }
  }
}
</script>
<style lang="scss">
$logosection-color: #043344;
.write-content {
  max-width: 1000px;
  margin: 20px auto;
  background: #fff;
  box-shadow: 0 10px 20px 0 rgba(0, 0, 0, 0.05);

  border-radius: 8px;
  .v-subheader {
    padding: 0;
  }
}
.editor-content {
  box-shadow: none;
  background: #fdfdfd;
  border-radius: 8px;

  .ql-toolbar.ql-snow {
    border: none;
    border-bottom: 1px solid #2e2e2e;
  }
  .quill-editor {
    min-height: 200px;
    overflow-y: auto;
    border: none;
  }
}
.header-section {
  margin: 20px 0;
  padding: 20px 0;
  text-align: left;
  color: $logosection-color;
  overflow: hidden;
  @media (max-width: 768px) {
    padding: 0;
    margin: 0;
  }

  .main-title {
    font-size: 30px;
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
      @media (max-width: 768px) {
        min-height: 200px;
        max-height: 200px;
      }
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
    margin-bottom: 15px;
    .v-chip {
      background: #f7fafc;
      .v-chip__content {
        text-transform: capitalize;
        font-size: 12px;
      }
      .v-chip__close {
        .v-icon {
          &::before {
            color: #337fb5;
          }
        }
      }
    }

    .chip-container {
      padding: 5px 0;
      border-bottom: 1px solid #f2f2f2;
      display: flex;
      flex-wrap: wrap;
      .chip {
        border-radius: 8px;
        padding: 5px 10px;
        background: #f7fafc;
        color: #337fb5;
        margin-right: 10px;
        margin-bottom: 10px;
        font-size: 12px;
        text-decoration: none;
        text-transform: capitalize;
        cursor: pointer;
        @media (max-width: 768px) {
          font-size: 10px;
        }
        &:hover {
          background: #fbfeff;
        }
      }
      .read-time {
        float: right;
        font-size: 12px;
        color: #b1b1b1;
      }
    }
  }
  .v-text-field.v-text-field--solo:not(.v-text-field--solo-flat)
    > .v-input__control
    > .v-input__slot {
    box-shadow: none;
    background: #fdfdfd;
    border-radius: 8px;
  }
}
</style>
