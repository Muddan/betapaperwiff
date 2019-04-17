<template>
  <div class="nav-bar">
    <v-navigation-drawer app v-model="drawer" disable-resize-watcher>
      <v-list>
        <v-list-tile-sub-title class="pa-1">
          <user-info></user-info>
        </v-list-tile-sub-title>
        <template v-for="(item, index) in items">
          <v-list-tile :key="index">
            <v-list-tile-content>{{item.title}}</v-list-tile-content>
          </v-list-tile>
          <v-divider :key="`divider-${index}`"></v-divider>
        </template>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar height="50px" app dark color="#2a7b9c" :scrollOffScreen="true">
      <v-toolbar-side-icon class="hidden-md-and-up" @click="drawer = !drawer"></v-toolbar-side-icon>

      <v-spacer class="hidden-md-and-up"></v-spacer>
      <div class="app-title">
        <router-link to="/">
          <img src="@/assets/logo.png" alt="local restaurants">
        </router-link>
      </div>
      <v-spacer class="hidden-sm-and-down"></v-spacer>

      <!-- Search icon -->
      <v-dialog v-model="dialog" :full-width="true" :fullscreen="false">
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on">
            <v-icon color="#f2f2f2">search</v-icon>
          </v-btn>
        </template>
        <v-card>
          <v-card-text>
            <v-flex xs12 sm12>
              <v-text-field label="Outline" single-line outline clearable></v-text-field>
            </v-flex>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="#f2f2f2" flat @click="dialog = false">Search</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>

      <!-- Write icon -->
      <router-link to="/write">
        <v-btn color="#f2f2f2" class="hidden-sm-and-down" flat value="help">
          <v-icon size="18px" left>fas fa-edit</v-icon>
          <span>Write</span>
        </v-btn>
      </router-link>
      <v-menu left bottom offset-y transition="slide-y-reverse-transition">
        <template v-slot:activator="{ on }">
          <v-btn v-on="on" flat icon color="#f2f2f2">
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
import { mapGetters } from "vuex";
import UserInfo from "@/components/Blocks/UserInfo.vue";

export default {
  name: "NavigationDrawer",
  components: {
    UserInfo
  },
  data: () => ({
    drawer: false,
    dialog: false,
    appTitle: "Walker",
    items: [
      { title: "Join", link: "/join" },
      { title: "About Paperwiff", link: "/" }
    ]
  }),
  props: {
    source: String
  },
  computed: {
    ...mapGetters({
      isSignedIn: "User/isSignedIn"
    })
  },
  mounted() {
    if (window.gapi) {
      window.gapi.load("auth2", () => {
        const auth2 = window.gapi.auth2.init({
          client_id:
            "430441876577-gpsarrij27132ir90dqb493hanfrn0og.apps.googleusercontent.com"
        });
      });
    }
  },
  methods: {
    signOut() {
      if (window.gapi) {
        var auth2 = window.gapi.auth2.getAuthInstance();
        auth2.signOut().then(
          function() {
            console.log("User signed out.");
            this.$store.dispatch("User/logoutUser");
          }.bind(this)
        );
      }
    }
  }
};
</script>
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
    box-shadow: 0 10px 30px 0 rgba(0, 0, 0, 0.3);
    .v-toolbar__content {
      max-width: 1400px;
      margin: auto;
    }
  }
}
</style>
