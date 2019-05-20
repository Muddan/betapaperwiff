<template>
  <div class="nav-bar">
    <v-navigation-drawer v-model="drawer" app disable-resize-watcher>
      <v-flex class="container">
        <user-info></user-info>
        <join-us></join-us>
        <key-links></key-links>
      </v-flex>
    </v-navigation-drawer>
    <v-toolbar height="80px" app flat color="white" :scroll-off-screen="true">
      <v-toolbar-side-icon class="hidden-md-and-up" @click="drawer = !drawer">
        <v-icon color="#337fb5">fas fa-bars</v-icon>
      </v-toolbar-side-icon>
      <v-toolbar-title class="#337fb5">
        <router-link to="/">
          <img class="logo-img" src="../assets/logo.png" />
        </router-link>
      </v-toolbar-title>

      <v-spacer class="hidden-md-and-up"></v-spacer>
      <v-spacer class="hidden-sm-and-down"></v-spacer>
      <router-link to="/write">
        <v-btn color="#337fb5" flat value="help">
          <v-icon size="18px" left>fas fa-feather</v-icon>
          <span>Write</span>
        </v-btn>
      </router-link>
      <v-menu left bottom offset-y transition="slide-y-reverse-transition">
        <template v-slot:activator="{ on }">
          <v-btn class="hidden-md-and-down" flat icon color="#337fb5" v-on="on">
            <v-icon size="18px">fa fa-ellipsis-v</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-tile v-if="isSignedIn" @click="signOut">Sign Out</v-list-tile>
          <v-list-tile-content v-for="(item, i) in items" :key="i">
            <v-list-tile>
              <router-link :to="item.link">
                <v-list-tile-title>{{ item.title }}</v-list-tile-title>
              </router-link>
            </v-list-tile>
          </v-list-tile-content>
        </v-list>
      </v-menu>
    </v-toolbar>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
import UserInfo from '@/components/Blocks/UserInfo.vue'
import JoinUs from '@/components/Blocks/JoinUs.vue'
import KeyLinks from '@/components/Blocks/KeyLinks.vue'

export default {
  name: 'NavigationDrawer',
  components: {
    UserInfo,
    JoinUs,
    KeyLinks
  },
  props: {
    source: {
      type: String,
      default: ''
    }
  },
  data: () => ({
    drawer: false,
    dialog: false,
    logout: false,
    items: [{ title: 'settings', link: '/settings' }]
  }),

  computed: {
    ...mapGetters({
      isSignedIn: 'user/isSignedIn'
    })
  },
  methods: {
    signOut() {
      this.$store.dispatch('notification/success', {
        title: 'Logged Out!',
        message: 'Successfully logged out.'
      })
      this.$store.dispatch('user/logoutUser')
      this.$router.push('/')
    }
  }
}
</script>
<style lang="scss">
.app-title {
  overflow: hidden;
  height: 100%;
  box-sizing: border-box;
  padding: 10px;
  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
}
.nav-bar {
  .v-toolbar {
    .v-toolbar__title {
      max-width: 150px;
      .logo-img {
        width: 100%;
      }
    }
    box-shadow: 0 10px 20px 0 rgba(0, 0, 0, 0.05) !important;

    .v-toolbar__content {
      max-width: 1400px;
      margin: auto;
    }
  }
}
</style>
