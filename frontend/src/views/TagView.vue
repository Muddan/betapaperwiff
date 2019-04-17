<template>
  <v-container>
    <v-content v-if="tagExits">
      <div class="tagDetails">
        <div class="tagname-section">
          <header>
            <h3 class="main-title">{{ tagName }}</h3>
          </header>
        </div>
        <div class="main-content">
          <v-layout>
            <v-flex class="sidebar-section sidebar-left hidden-sm-and-down" md3 xs12>
              <key-links></key-links>
            </v-flex>
            <v-flex class="content-section" md9 xs12>
              <story-items :stories="getTagStories()"></story-items>
            </v-flex>
          </v-layout>
        </div>
      </div>
    </v-content>
    <v-content v-else>
      <div class="nf-content">
        <v-layout>
          <div class="nf-section">
            <h2 class="oops">Oops!</h2>
            <h3 class="msg">This tag is not available.</h3>
            <div class="homelink">
              <router-link to="/">Let's go Home</router-link>
            </div>
          </div>
        </v-layout>
      </div>
    </v-content>
  </v-container>
</template>

<script>
import { mapGetters } from "vuex";
import StoryItems from "@/components/Blocks/StoryItems.vue";
import KeyLinks from "@/components/Blocks/KeyLinks.vue";

export default {
  name: "TagView",
  components: {
    StoryItems,
    KeyLinks
  },
  computed: {
    ...mapGetters({
      availableTagNames: "Stories/availableTags",
      allStories: "Stories/allStories"
    }),
    tagName() {
      return this.$route.params.tagName;
    },
    tagExits() {
      let currentTagName = this.$route.params.tagName;
      return this.availableTagNames.includes(currentTagName);
    }
  },
  methods: {
    getTagStories() {
      return this.allStories.filter(story => {
        return story.tags.includes(this.$route.params.tagName);
      });
    }
  }
};
</script>

<style lang="scss">
$logosection-color: #043344;
.tagname-section {
  margin: 20px 0;
  padding: 20px 0;
  text-align: center;
  // color: #36789a;
  color: $logosection-color;
  overflow: hidden;

  .main-title {
    font-family: "Adamina", serif;
    font-size: 55px;
    font-weight: bold;
    text-transform: uppercase;
  }
}
.nf-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  .oops {
    font-size: 5rem;
  }
  .msg {
    text-transform: uppercase;
  }
  .homelink {
    text-align: center;
    box-sizing: border-box;
    padding: 15px;
    margin: 20px 0;
    a {
      font-size: 26px;
      font-weight: bold;
      text-decoration: underline;
      color: #043344;
    }
  }
}
.tagDetails {
  .keylinks-main {
    margin-top: 35px;
  }
}
</style>
