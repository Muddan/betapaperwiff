<template>
  <div class="articles-tab">
    <v-tabs class="tab-header" centered color="#fff" icons-and-text>
      <v-tabs-slider color="#114b5f"></v-tabs-slider>

      <v-tab v-if="isSignedIn" href="#feed">Feed</v-tab>

      <v-tab href="#latest">Latest</v-tab>

      <v-tab-item v-if="isSignedIn" value="feed">
        <story-items :stories="getCurrentUserFeed"></story-items>
      </v-tab-item>
      <v-tab-item value="latest">
        <story-items :stories="getCurrentUserFeed"></story-items>
      </v-tab-item>
    </v-tabs>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import StoryItems from '@/components/Blocks/StoryItems.vue'
export default {
  name: 'StoryListing',
  components: {
    StoryItems
  },
  data() {
    return {
      loader: null,
      loading: false
    }
  },
  computed: {
    ...mapGetters({
      filteredStories: 'stories/filteredStories',
      allStories: 'stories/allStories',
      isSignedIn: 'user/isSignedIn'
    }),
    getCurrentUserFeed() {
      if (this.filteredStories.length > 0) {
        return this.filteredStories
      } else {
        return this.allStories
      }
    }
  },
  watch: {
    loader() {
      const l = this.loader
      this[l] = !this[l]

      setTimeout(() => (this[l] = false), 3000)

      this.loader = null
    }
  }
}
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
}
</style>
