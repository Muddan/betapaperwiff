<template>
  <div class="articles-tab">
    <!-- <v-tabs class="tab-header" centered color="#fff" icons-and-text>
      <v-tabs-slider color="#114b5f"></v-tabs-slider>

      <v-tab v-if="isSignedIn" href="#feed">Feed</v-tab>

      <v-tab href="#latest">Latest</v-tab>

      <v-tab-item v-if="isSignedIn" value="feed">
        <story-items :stories="getCurrentUserFeed"></story-items>
      </v-tab-item>
      <v-tab-item value="latest">
        <story-items :stories="getCurrentUserFeed"></story-items>
      </v-tab-item>
    </v-tabs>-->
    <!-- <v-flex xs12 class="btn-group">
      <v-btn-toggle flat v-model="toggle_one" mandatory>
        <v-btn>Feed</v-btn>
        <v-btn>Latest</v-btn>
      </v-btn-toggle>
    </v-flex>-->
    <story-items :stories="getCurrentUserFeed"></story-items>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import StoryTags from "@/components/Blocks/StoryTags.vue";
import StoryItems from "@/components/Blocks/StoryItems.vue";
export default {
  name: "StoryListing",
  components: {
    StoryTags,
    StoryItems
  },
  data() {
    return {
      loader: null,
      loading: false,
      toggle_one: 0
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
  computed: {
    ...mapGetters({
      filteredStories: "Stories/filteredStories",
      allStories: "Stories/allStories",
      isSignedIn: "User/isSignedIn"
    }),
    getCurrentUserFeed() {
      if (this.filteredStories.length > 0) {
        return this.filteredStories;
      } else {
        return this.allStories;
      }
    }
  }
};
</script>
<style lang="scss">
.story-loader {
  display: block;
  width: 100%;
  text-align: center;
}
.story-content-main {
  .v-list__tile__content {
    .summary {
      font-size: 16px;

      white-space: normal;
    }
  }
}
.articles-tab {
  > .container {
    padding: 0;
  }
  .btn-group {
    text-align: center;
  }
  // .v-tabs.tab-header {
  //   border-radius: 8px;
  //   border: 1px solid #114b5f;
  //   border-top: 4px solid #114b5f;

  //   .theme--light.v-tabs__bar {
  //     margin-bottom: 35px;
  //     // box-shadow: 0 10px 30px 0 rgba(0, 0, 0, 0.1);
  //   }
  // }
}
</style>

