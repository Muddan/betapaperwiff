<template>
  <div id="home-top" class="main-container">
    <div id="home">
      <v-fab-transition>
        <v-btn
          v-show="ScrollToTopHidden"
          v-scroll="onScroll"
          color="#77b6e2"
          fab
          dark
          fixed
          bottom
          right
          @click="$vuetify.goTo('#home-top')"
        >
          <v-icon>keyboard_arrow_up</v-icon>
        </v-btn>
      </v-fab-transition>
      <v-navigation-drawer
        v-model="leftDrawer"
        class="mobile-left-sidebar"
        app
        disable-resize-watcher
      >
        <v-flex class="container">
          <SidebarStories>
            <span slot="title">Popular Stories on Paperwiff</span>
          </SidebarStories>
        </v-flex>
      </v-navigation-drawer>
      <v-navigation-drawer
        v-model="rightDrawer"
        right
        class="mobile-left-sidebar"
        app
        disable-resize-watcher
      >
        <v-flex class="container">
          <tag-listing></tag-listing>
        </v-flex>
      </v-navigation-drawer>
      <div class="logo-section">
        <v-layout class="hidden-md-and-up">
          <v-btn flat icon color="#337fb5" @click="leftDrawer = !leftDrawer">
            <v-icon small>fas fa-clipboard-list </v-icon>
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn flat icon color="#337fb5" @click="rightDrawer = !rightDrawer">
            <v-icon small>fa fa-coins</v-icon>
          </v-btn>
        </v-layout>
      </div>
      <div class="main-content">
        <v-layout>
          <v-flex
            class="sidebar-section sidebar-left hidden-sm-and-down"
            md3
            xs12
            sm12
          >
            <user-info :image-only="false" :only-mobile="true"></user-info>
            <tag-listing></tag-listing>
            <v-scroll-y-transition>
              <key-links></key-links>
            </v-scroll-y-transition>
          </v-flex>
          <v-flex class="content-section" md6 xs12>
            <div class="articles-tab">
              <div class="tab-list">
                <v-subheader
                  v-for="(label, index) in FeedType"
                  :key="index"
                  depressed
                  class="feed-title"
                  :class="{ 'feed-title--active': activeTab === label.title }"
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
          </v-flex>
          <v-flex
            class="sidebar-section sidebar-right hidden-sm-and-down"
            md3
            xs12
            sm12
          >
            <v-scroll-y-transition>
              <join-us></join-us>
            </v-scroll-y-transition>
            <SidebarStories>
              <span slot="title">Popular Stories on Paperwiff</span>
            </SidebarStories>
          </v-flex>
        </v-layout>
      </div>
    </div>
  </div>
</template>
<script>
// Custom components
import TagListing from '@/components/Blocks/TagListing/TagListing.vue'
import UserInfo from '@/components/Blocks/UserInfo.vue'
import KeyLinks from '@/components/Blocks/KeyLinks.vue'
import JoinUs from '@/components/Blocks/JoinUs.vue'
import SidebarStories from '@/components/Blocks/SidebarStories/SidebarStories.vue'
import StoryItems from '@/components/Blocks/StoryItems.vue'

import { mapGetters } from 'vuex'

import InfiniteLoading from 'vue-infinite-loading'
import { endpoints } from '../api/endpoints'

export default {
  transition: 'fade',

  name: 'Home',
  components: {
    TagListing,
    UserInfo,
    KeyLinks,
    JoinUs,
    SidebarStories,
    StoryItems,
    InfiniteLoading
  },
  data() {
    return {
      snackbar: true,
      leftDrawer: false,
      rightDrawer: false,
      ScrollToTopHidden: false,
      pageNo: 2,
      FeedType: [
        { title: 'Latest', status: true }
        // { title: 'Popular', status: false }
      ],
      activeTab: 'Latest'
    }
  },
  computed: {
    ...mapGetters({
      filteredStories: 'stories/filteredStories',
      allStories: 'stories/allStories'
    })
  },
  mounted() {
    this.$store.dispatch('stories/getAllStories')
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
    onScroll(e) {
      if (window && typeof window === 'undefined') return
      const top = window.pageYOffset || e.target.scrollTop || 0
      this.ScrollToTopHidden = top > 100
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
.main-container {
  max-width: 1400px;
  width: 100%;
  margin: auto;
  @media (max-width: 1024px) {
    padding: 0;
  }
}
$logosection-color: #043344;
#home {
  margin-top: 20px;
  .logo-section {
    .main-title {
      font-family: 'Marck Script', cursive;
      font-size: 55px;
      font-weight: normal;
    }
    .socialIcon {
      color: $logosection-color;
    }
    .subtitle {
      box-sizing: border-box;
      padding: 20px 0;
      margin: 0;
      position: relative;
      font-size: 16px;
      color: $logosection-color;
      text-transform: lowercase;
      &::after,
      &::before {
        content: '';
        display: inline-block;
        width: 10%;
        height: 2px;
        background: $logosection-color;
        margin: 0 20px 5px 20px;
      }
    }
  }
  .content-section,
  .sidebar-section {
    box-sizing: border-box;
    padding: 0 15px;
    @media (max-width: 1024px) {
      padding: 0 8px;
    }
  }
  .sidebar-left,
  .sidebar-right {
    padding-top: 10px;
  }
  .articles-tab {
    padding-top: 10px;
    .v-tabs__bar {
      border-radius: 8px;
    }
  }
  .sidebar-stories-main {
    margin: 20px 0;
  }
  .mobile-left-sidebar {
    .container {
      padding: 0;
    }
  }
}
</style>
