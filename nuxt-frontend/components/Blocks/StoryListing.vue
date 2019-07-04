<template>
  <div class="articles-tab">
    <div class="tab-list">
      <v-subheader
        v-for="(label, index) in FeedType"
        :key="index"
        depressed
        class="feed-title"
        :class="{ 'feed-title--active': activeTab === label.title }"
        @click="changeTab(label)"
      >
        {{ label.title }}
      </v-subheader>
      <!-- <v-subheader
        v-if="isSignedIn"
        depressed
        class="feed-title"
        :class="{ 'feed-title--active': activeTab === 'Feed' }"
        @click.stop="changeTab({ title: 'Feed', status: false })"
      >
        {{ 'Feed' }}
      </v-subheader> -->
    </div>

    <story-items
      v-if="getCurrentUserFeed()"
      :stories="getCurrentUserFeed()"
    ></story-items>
    <no-ssr>
      <InfiniteLoading spinner="bubbles" @infinite="infiniteHandler">
        <div slot="no-more" class="no-more-text">
          The End.
        </div>
      </InfiniteLoading>
    </no-ssr>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import StoryItems from '@/components/Blocks/StoryItems.vue'
import InfiniteLoading from 'vue-infinite-loading'
import { endpoints } from '../../api/endpoints'

export default {
  name: 'StoryListing',
  components: {
    StoryItems,
    InfiniteLoading
  },
  data() {
    return {
      loader: null,
      loading: false,
      pageNo: 1,
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
      isSignedIn: 'user/isSignedIn',
      userFeed: 'user/userFeed'
    })
  },
  methods: {
    infiniteHandler($state) {
      this.$axios
        .$get(`${endpoints.API_GET_STORIES}?pageNo=${this.pageNo}`)
        .then(async res => {
          await this.$store.commit('stories/SET_ALL_STORIES', {
            items: res.result.items,
            loadMore: true
          })
          this.pageNo++
          if (
            this.$store.state.stories.allStories.length < res.result.totalItems
          ) {
            $state.loaded()
          } else {
            $state.complete()
          }
        })
    },
    changeTab(tab) {
      this.activeTab = tab.title
    },
    getCurrentUserFeed() {
      // if (this.activeTab === 'Feed') {
      //   return this.$store.dispatch('user/userFeed')
      // } else {
      //   return this.allStories
      // }
      return this.allStories
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

  .tab-list {
    display: flex;
    .feed-title {
      cursor: pointer;
      padding: 0 20px;
      border-bottom: 2px solid #f6f9fb;
      transition: all 0.2s ease-in-out;
      &.feed-title--active {
        color: #337fb5 !important;
        border-bottom: 2px solid #337fb5;
      }
    }
  }
  .no-more-text {
    box-sizing: border-box;
    padding: 20px;
    font-size: 20px;
  }
}
</style>
