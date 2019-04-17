<template>
  <v-container>
    <v-content>
      <div class="header-section">
        <header>
          <h3 class="main-title" v-if="isSigned">Welcome, {{ currentUser.first_name }} !</h3>
          <p class="subheading">compose an epic.</p>
        </header>
      </div>
      <div class="form-section">
        <v-flex xs12 sm6>
          <v-text-field label="Title" single-line solo></v-text-field>
        </v-flex>
        <v-layout row wrap>
          <v-flex xs12 sm6>
            <vue-editor
              @text-change="textChange()"
              placeholder="Compose an epic..."
              v-model="content"
              :editorToolbar="customToolbar"
            ></vue-editor>
          </v-flex>
          <v-flex xs12 sm6 wrap>
            <vue-editor
              @text-change="textChange()"
              placeholder="Compose an epic..."
              v-model="content"
              :editorToolbar="customToolbar"
            ></vue-editor>
          </v-flex>
        </v-layout>

        <v-btn
          :loading="publishing"
          :disabled="publishing"
          color="#ffb3b9"
          @click="loader = 'publishing'"
        >
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

export default {
  components: {
    VueEditor
  },
  computed: {
    ...mapGetters({
      isSignedIn: "User/isSignedIn",
      currentUser: "User/currentUser"
    })
  },
  data() {
    return {
      loader: null,
      publishing: false,
      content: "",
      customToolbar: [
        ["bold", "italic", "underline"],
        [{ list: "ordered" }, { list: "bullet" }]
      ]
    };
  },
  watch: {
    loader() {
      const l = this.loader;
      this[l] = !this[l];

      setTimeout(() => (this[l] = false), 3000);

      this.loader = null;
    }
  },
  methods: {
    isSigned() {
      return this.isSigned;
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

