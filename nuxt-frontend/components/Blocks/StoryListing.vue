<template>
  <div class="articles-tab">
    <v-btn
      v-for="(label, index) in FeedType"
      :key="index"
      depressed
      :class="{ 'v-btn--active': activeTab === label.title }"
      @click="changeTab(label)"
    >
      {{ label.title }}
    </v-btn>
    <v-btn
      v-if="isSignedIn"
      depressed
      :class="{ 'v-btn--active': activeTab === 'Feed' }"
      @click.stop="changeTab({ title: 'Feed', status: false })"
    >
      {{ 'Feed' }}
    </v-btn>
    <v-scroll-y-transition>
      <story-items :stories="getCurrentUserFeed()"></story-items>
    </v-scroll-y-transition>
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
      loading: false,
      FeedType: [
        { title: 'Latest', status: true }
        // { title: 'Popular', status: false }
      ],
      activeTab: 'Latest',
      toggleTab: 0
    }
  },
  computed: {
    ...mapGetters({
      filteredStories: 'stories/filteredStories',
      allStories: 'stories/allStories',
      isSignedIn: 'user/isSignedIn'
    })
  },
  watch: {
    loader() {
      const l = this.loader
      this[l] = !this[l]

      setTimeout(() => (this[l] = false), 3000)

      this.loader = null
    }
  },
  methods: {
    changeTab(tab) {
      this.activeTab = tab.title
    },
    getCurrentUserFeed() {
      if (this.activeTab === 'Feed') {
        return this.filteredStories
      } else {
        return this.allStories
      }
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
  .v-item-group {
    display: flex;
    justify-content: space-evenly;
    box-shadow: none;
    background: none;
    padding: 10px 0;
    .v-btn {
      padding: 20px;
      border-radius: 8px;
    }
  }
  .v-btn--active {
    background-color: #337fb5 !important;
    color: #fff !important;
    border-radius: 8px;
  }
}
</style>
