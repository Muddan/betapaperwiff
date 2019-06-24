<template>
  <div class="nav-bar">
    <v-navigation-drawer
      v-model="drawer"
      class="grey lighten-5"
      app
      disable-resize-watcher
      :temporary="true"
    >
      <v-flex xs12 class="mini-profile-mob">
        <user-info :image-only="false" :only-mobile="true"></user-info>
        <join-us></join-us>
        <v-list class="pt-0 pb-0">
          <div v-if="isSignedIn" class="user-profile-links">
            <v-subheader>
              My Account
            </v-subheader>
            <v-list-tile>
              <v-list-tile-title>
                <nuxt-link
                  :to="{
                    path: '/a/' + currentUser.userName
                  }"
                >
                  Profile
                </nuxt-link>
              </v-list-tile-title>
            </v-list-tile>
            <v-list-tile>
              <v-list-tile-title>
                <nuxt-link
                  :to="{
                    path: '/a/' + currentUser.userName + '/saved-stories'
                  }"
                >
                  Saved Stories
                </nuxt-link>
              </v-list-tile-title>
            </v-list-tile>
            <v-list-tile>
              <v-list-tile-title>
                <nuxt-link
                  :to="{
                    path: '/settings'
                  }"
                >
                  Settings
                </nuxt-link>
              </v-list-tile-title>
            </v-list-tile>
          </div>
          <v-subheader>
            Important Links
          </v-subheader>
          <v-list-tile v-for="item in keyLinks" :key="item.title">
            <v-list-tile-title>
              <nuxt-link :to="item.link">{{ item.title }}</nuxt-link>
            </v-list-tile-title>
          </v-list-tile>
          <v-divider></v-divider>
          <v-list-tile>
            <v-list-tile-title><h3>Become a member</h3></v-list-tile-title>
          </v-list-tile>
          <v-divider></v-divider>
          <v-subheader>
            Social Media
          </v-subheader>
          <v-btn
            v-for="(icon, index) in socialIcons"
            :key="index"
            :href="icon.link"
            class="mx-2"
            icon
          >
            <v-icon class="socialIcon">{{ icon.name }}</v-icon>
          </v-btn>
          <!-- <v-list-tile class="list-footer">
            <v-list-tile-title>
              &copy;2019 — <strong>Paperwiff</strong></v-list-tile-title
            >
          </v-list-tile> -->
        </v-list>
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
      <v-btn
        v-if="!isSignedIn"
        class="hidden-md-and-down"
        small
        round
        outline
        color="#4caf50"
        flat
        @click="openForm()"
      >
        <span>Join Us</span>
      </v-btn>
      <div v-show="isSignedIn" class="text-xs-center">
        <v-menu left bottom offset-y>
          <template v-slot:activator="{ on }">
            <v-btn flat icon color="#337fb5" v-on="on">
              <v-icon>
                notifications
              </v-icon>
            </v-btn>
          </template>
          <v-list>
            <v-list-tile>
              <v-subheader>No notifications</v-subheader>
            </v-list-tile>
          </v-list>
        </v-menu>
      </div>
      <v-menu left bottom offset-y transition="slide-y-reverse-transition">
        <template v-slot:activator="{ on }">
          <v-btn class="hidden-md-and-down" flat icon color="#337fb5" v-on="on">
            <v-avatar
              v-if="isSignedIn && currentUser.userImage"
              v-show="currentUser.userImage"
              size="35px"
            >
              <img :src="currentUser.userImage" />
            </v-avatar>
            <v-icon v-else size="18px">fa fa-ellipsis-v</v-icon>
          </v-btn>
        </template>
        <v-list>
          <nuxt-link
            v-if="isSignedIn"
            class="user-link"
            :to="{
              path: '/a/' + currentUser.userName
            }"
          >
            <v-list-tile class="username-header ">{{
              currentUser.firstName
            }}</v-list-tile>
          </nuxt-link>
          <nuxt-link
            v-if="isSignedIn"
            class="auth-links"
            :to="{
              path: '/a/' + currentUser.userName + '/published'
            }"
          >
            <v-list-tile>Published</v-list-tile>
          </nuxt-link>
          <nuxt-link
            v-if="isSignedIn"
            class="auth-links"
            :to="{
              path: '/a/' + currentUser.userName + '/saved-stories'
            }"
          >
            <v-list-tile>Saved Stories</v-list-tile>
          </nuxt-link>

          <v-divider v-if="isSignedIn"></v-divider>
          <v-list-tile-content v-for="(item, i) in items" :key="i">
            <v-list-tile>
              <router-link :to="item.link">
                <v-list-tile-title>{{ item.title }}</v-list-tile-title>
              </router-link>
            </v-list-tile>
          </v-list-tile-content>
          <v-list-tile v-if="isSignedIn" @click="signOut">Sign Out</v-list-tile>
        </v-list>
      </v-menu>
    </v-toolbar>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
import UserInfo from '@/components/Blocks/UserInfo.vue'
import JoinUs from '@/components/Blocks/JoinUs.vue'
// import KeyLinks from '@/components/Blocks/KeyLinks.vue'

export default {
  name: 'NavigationDrawer',
  components: {
    UserInfo,
    JoinUs
    // KeyLinks
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
    items: [
      { title: 'About Paperwiff', link: '/about' },
      { title: 'Settings', link: '/settings' }
    ],
    links: ['Home', 'Contacts', 'Settings'],
    socialIcons: [
      {
        name: 'fab fa-facebook',
        link: 'https://www.facebook.com/paperwiff/'
      },
      {
        name: 'fab fa-twitter',
        link: 'https://twitter.com/paperwiff?lang=en'
      },
      {
        name: 'fab fa-instagram',
        link: 'https://www.instagram.com/paperwiff/'
      }
    ],
    keyLinks: [
      { title: 'About Paperwiff', link: '/about' },
      // { title: 'Pricing', link: '/pricing' },
      { title: ' Privacy Policy', link: '/privacy-policy' },
      { title: 'Contact', link: '/contact' }
      // { title: 'Faq', link: '/faq' },
      // { title: 'Code of conduct', link: '/code-of-conduct' }
    ]
  }),

  computed: {
    ...mapGetters({
      isSignedIn: 'user/isSignedIn',
      currentUser: 'user/currentUser'
    })
  },
  methods: {
    signOut() {
      this.$store.dispatch('notification/success', {
        title: '',
        message: 'Successfully logged out.'
      })
      this.$store.dispatch('user/logoutUser')
      this.$router.push('/')
    },
    openForm() {
      this.$store.commit('ui/SET_SHOW_POPUP', {
        status: true,
        component: 'SignUp'
      })
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
  .list-footer {
    background: #fff;
    z-index: 1;
    width: 100%;
  }
  .mini-profile-mob {
    .user-info {
      margin-bottom: 10px;
    }
  }
}
.v-list {
  .username-header {
    .v-list__tile {
      font-weight: bold;
      font-size: 18px;
      letter-spacing: 1px;
    }
  }
}
</style>
