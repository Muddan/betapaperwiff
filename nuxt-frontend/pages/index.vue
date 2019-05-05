<template>
  <div class="main-container">
    <div id="home">
      <v-navigation-drawer
        v-model="leftDrawer"
        class="mobile-left-sidebar"
        app
        disable-resize-watcher
      >
        <v-flex class="container">
          <user-info></user-info>
          <key-links></key-links>
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
            <v-icon>fas fa-clipboard-list </v-icon>
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn flat icon color="#337fb5" @click="rightDrawer = !rightDrawer">
            <v-icon>fa fa-coins</v-icon>
          </v-btn>
        </v-layout>
      </div>
      <div class="main-content">
        <v-layout>
          <v-flex
            class="sidebar-section sidebar-left hidden-sm-and-down"
            md3
            xs12
          >
            <user-info></user-info>
            <tag-listing></tag-listing>
          </v-flex>
          <v-flex class="content-section" md6 xs12>
            <story-listing></story-listing>
          </v-flex>
          <v-flex
            class="sidebar-section sidebar-right hidden-sm-and-down"
            md3
            xs12
          >
            <join-us></join-us>
            <key-links></key-links>
          </v-flex>
        </v-layout>
      </div>
    </div>
  </div>
</template>
<script>
// Custom components
import TagListing from '@/components/Blocks/TagListing.vue'
import UserInfo from '@/components/Blocks/UserInfo.vue'
import StoryListing from '@/components/Blocks/StoryListing.vue'
import KeyLinks from '@/components/Blocks/KeyLinks.vue'
import JoinUs from '@/components/Blocks/JoinUs.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'Home',
  components: {
    TagListing,
    UserInfo,
    StoryListing,
    KeyLinks,
    JoinUs
  },
  data() {
    return {
      snackbar: true,
      leftDrawer: false,
      rightDrawer: false
    }
  },
  computed: {
    ...mapGetters({
      filteredStories: 'stories/filteredStories',
      allStories: 'stories/allStories'
    })
  }
}
</script>
<style lang="scss">
.main-container {
  max-width: 1400px;
  margin: auto;
  @media (max-width: 1024px) {
    padding: 0;
  }
}
$logosection-color: #043344;
#home {
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
}
</style>
