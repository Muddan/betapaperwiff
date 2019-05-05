<template>
  <div class="write-content">
    <v-container>
      <!-- <div class="header-section">
        <header>
          <h3 v-if="isSigned" class="main-title">
            Welcome, {{ currentUser.firstName }} !
          </h3>
          <p class="subheading">compose an epic.</p>
        </header>
      </div> -->
      <div class="form-section">
        <v-flex xs12 sm6>
          <image-input v-model="headerImage" class="header-img-main">
            <div slot="activator">
              <v-container
                v-if="!headerImage"
                v-ripple
                class="bg-holder"
                color="grey lighten-3"
                height="300px"
              >
                <strong><span>Add banner for your post.</span></strong>
              </v-container>
              <v-container v-else v-ripple class="bg-holder">
                <v-img :src="headerImage.imageURL" alt="avatar"></v-img>
              </v-container>
            </div>
          </image-input>
        </v-flex>
        <v-flex xs12 sm6>
          <v-text-field
            v-model="title"
            label="Title"
            single-line
            solo
          ></v-text-field>
        </v-flex>

        <!-- <v-flex xs12 sm6>
          <v-select
            prepend-icon="language"
            :items="translateLanguages"
            solo
            label="Select translation language"
            @change="setLanguage"
          ></v-select>
        </v-flex> -->
        <v-flex class="white" xs12 sm6 wrap>
          <section class="container">
            <div
              v-quill:myQuillEditor="editorOption"
              class="quill-editor"
              :content="content"
              @change="onEditorChange($event)"
            >
              >
            </div>
          </section>
        </v-flex>
        <v-flex class="tags-input" sm6 xs12>
          <v-combobox
            v-model="selectedTags"
            :items="storyTagsAvailable"
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
  components: {
    ImageInput
  },

  data() {
    return {
      saved: false,
      headerImage: null,
      loader: null,
      publishing: false,
      title: '',
      content: '',
      translatedContent: '',
      selectedLanguage: 'english',
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
      selectedTags: [],
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
    })
  },
  methods: {
    onEditorChange({ editor, html, text }) {
      // eslint-disable-next-line no-console
      console.log('editor change!', editor, html, text)
      this.content = html
    },
    isSigned() {
      return this.isSigned
    },
    remove(item) {
      this.selectedTags.splice(this.selectedTags.indexOf(item), 1)
      this.selectedTags = [...this.selectedTags]
    },
    setLanguage(language) {
      this.selectedLanguage = language
    },
    // textChange(quill) {
    //   // const regex = /(<([^>]+)>)/gi
    //   const queryText = this.content

    //   setTimeout(() => {
    //     this.$store
    //       .dispatch('Stories/translate', {
    //         query: queryText,
    //         language: this.selectedLanguage
    //       })
    //       .then(res => {
    //         this.translatedContent = res.data.message
    //       })
    //   }, 1000)
    // },
    publishStory() {
      this.$store.dispatch('notification/progress', {
        title: 'Publishing your story...'
      })
      // this.$store
      //   .dispatch('Stories/publishStory', {
      //     storyTitle: this.title,
      //     userId: this.currentUser.userId,
      //     content: this.translatedContent,
      //     tags: this.selectedTags
      //   })
      //   .then(res => {})
    },
    limiter(e) {
      if (e.length > 3) {
        this.$store.dispatch('notification/warning', {
          title: 'Not allowed !',
          message: 'Please choose upto 3 tags only'
        })
        e.pop()
      }
    },
    launchFilePicker() {
      this.$refs.file.click()
    },
    onFileChange(fieldName, file) {
      const { maxSize } = this
      const imageFile = file[0]
      if (file.length > 0) {
        const size = imageFile.size / maxSize / maxSize
        if (!imageFile.type.match('image.*')) {
          // check whether the upload is an image
          this.errorDialog = true
          this.errorText = 'Please choose an image file'
        } else if (size > 1) {
          // check whether the size is greater than the size limit
          this.errorDialog = true
          this.errorText =
            'Your file is too big! Please select an image under 1MB'
        } else {
          // Append file into FormData and turn file into image URL
          const formData = new FormData()
          const imageURL = URL.createObjectURL(imageFile)
          formData.append(fieldName, imageFile)
          // Emit the FormData and image URL to the parent component
          this.$emit('input', { formData, imageURL })
        }
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
.container {
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
    min-height: 300px;
    max-height: 300px;
    overflow: hidden;
    margin: 20px 0;
    .bg-holder {
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 300px;
      max-height: 300px;
      background: #dddddd;
      padding: 0;
      @media (max-width: 768px) {
        min-height: 150px;
        max-height: 150px;
      }
    }
    @media (max-width: 768px) {
      min-height: 150px;
      max-height: 150px;
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
