<template>
  <v-container>
    <v-content>
      <div class="header-section">
        <header>
          <h3 class="main-title" v-if="isSigned">Welcome, {{ currentUser.firstName }} !</h3>
          <p class="subheading">compose an epic.</p>
        </header>
      </div>
      <div class="form-section">
        <v-flex xs12 sm6>
          <v-text-field v-model="title" label="Title" single-line solo></v-text-field>
        </v-flex>
        <v-flex xs12 sm6>
          <v-select
            @change="setLanguage"
            prepend-icon="language"
            :items="translateLanguages"
            solo
            label="Select translation language"
          ></v-select>
        </v-flex>
        <v-layout row wrap>
          <v-flex class="white" xs12 sm6>
            <vue-editor
              ref="editor"
              @text-change="textChange()"
              placeholder="Compose an epic..."
              v-model="content"
              :editorToolbar="customToolbar"
            ></vue-editor>
          </v-flex>
          <v-flex class="white" xs12 sm6 wrap>
            <vue-editor
              placeholder="Translated text..."
              v-model="translatedContent"
              :editorToolbar="customToolbar"
            ></vue-editor>
          </v-flex>
          <v-flex class="tags-input" sm4 xs12>
            <v-combobox
              v-model="selectedTags"
              :items="storyTagsAvailable"
              label="Select Tags"
              chips
              clearable
              solo
              multiple
              v-on:input="limiter"
            >
              <template v-slot:selection="data">
                <v-chip :selected="data.selected" close @input="remove(data.item)">
                  <strong>{{ data.item }}</strong>&nbsp;
                </v-chip>
              </template>
            </v-combobox>
          </v-flex>
        </v-layout>

        <v-btn :loading="publishing" :disabled="publishing" color="#ffb3b9" @click="publishStory">
          Publish
          <template v-slot:loader>
            <span class="custom-loader">
              <v-icon light>cached</v-icon>
            </span>
          </template>
        </v-btn>
      </div>
    </v-content>
  </v-container>
</template>
 
<script>
import { VueEditor } from "vue2-editor";
import { mapGetters } from "vuex";
import axios from "axios";

export default {
  components: {
    VueEditor
  },
  computed: {
    ...mapGetters({
      isSignedIn: "User/isSignedIn",
      currentUser: "User/currentUser",
      storyTagsAvailable: "Stories/availableTags"
    })
  },
  data() {
    return {
      loader: null,
      publishing: false,
      title: "",
      content: "",
      translatedContent: "",
      selectedLanguage: "english",
      showEditor: false,
      customToolbar: [
        ["bold", "italic", "underline"],
        [{ list: "ordered" }, { list: "bullet" }]
      ],
      selectedTags: [],
      translateLanguages: [
        {
          text: "kananda"
        },
        { text: "hindi" },
        {
          text: "bengali"
        }
      ]
    };
  },
  watch: {
    // loader() {
    //   const l = this.loader;
    //   this[l] = !this[l];
    //   setTimeout(() => (this[l] = false), 3000);
    //   this.loader = null;
    // }
  },
  methods: {
    isSigned() {
      return this.isSigned;
    },
    remove(item) {
      this.selectedTags.splice(this.selectedTags.indexOf(item), 1);
      this.selectedTags = [...this.selectedTags];
    },
    setLanguage(language) {
      this.selectedLanguage = language;
    },
    textChange(quill) {
      let regex = /(<([^>]+)>)/gi;
      let queryText = this.content;

      setTimeout(() => {
        this.$store
          .dispatch("Stories/translate", {
            query: queryText,
            language: this.selectedLanguage
          })
          .then(res => {
            this.translatedContent = res.data.message;
            console.log(res);
          })
          .catch(err => {
            console.log(err);
          });
      }, 1000);
    },
    publishStory() {
      this.$store
        .dispatch("Stories/publishStory", {
          storyTitle: this.title,
          userId: this.currentUser.userId,
          content: this.translatedContent,
          tags: this.selectedTags
        })
        .then(res => {
          console.log(res);
        });
    },
    limiter(e) {
      if (e.length > 2) {
        alert("you can only select two");
        e.pop();
      }
    }
  }
};
</script>
<style lang="scss" scoped>
$logosection-color: #043344;
.header-section {
  margin: 20px 0;
  padding: 20px 0;
  text-align: left;
  // color: #36789a;
  color: $logosection-color;
  overflow: hidden;

  .main-title {
    font-family: "Adamina", serif;
    font-size: 30px;
    font-weight: bold;
    text-transform: capitalize;
  }
}
.form-section {
  .content-preview-main {
    border: 1px solid #2e2e2e;
  }
  .tags-input {
    margin-top: 30px;
  }
  .custom-loader {
    animation: loader 1s infinite;
    display: flex;
  }
  @-moz-keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
  @-webkit-keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
  @-o-keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
  @keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
}
</style>

