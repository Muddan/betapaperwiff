<template>
  <div class="nav-bar">
    <v-navigation-drawer app v-model="drawer" disable-resize-watcher>
      <user-info></user-info>
      <join-us></join-us>
    </v-navigation-drawer>
    <v-toolbar height="80px" app flat color="white" :scrollOffScreen="true">
      <v-toolbar-side-icon class="hidden-md-and-up" @click="drawer = !drawer">
        <v-icon color="#337fb5">fas fa-bars</v-icon>
      </v-toolbar-side-icon>
      <v-toolbar-title class="#337fb5">
        <router-link to="/">
          <img class="logo-img" src="../assets/logo.png">
        </router-link>
      </v-toolbar-title>

      <v-spacer class="hidden-md-and-up"></v-spacer>
      <v-spacer class="hidden-sm-and-down"></v-spacer>

      <!-- Search icon -->
      <!-- <v-dialog v-model="dialog" :full-width="true" :fullscreen="false">
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on">
            <v-icon color="#337fb5">search</v-icon>
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
            <v-btn color="#337fb5" flat @click="dialog = false">Search</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>-->

      <!-- Write icon -->
      <router-link to="/write">
        <v-btn color="#337fb5" flat value="help">
          <v-icon size="18px" left>fas fa-feather</v-icon>
          <span>Write</span>
        </v-btn>
      </router-link>
      <v-menu left bottom offset-y transition="slide-y-reverse-transition">
        <template v-slot:activator="{ on }">
          <v-btn class="hidden-md-and-down" v-on="on" flat icon color="#337fb5">
            <v-icon size="18px">fa fa-ellipsis-v</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-tile @click="signOut" v-if="isSignedIn">Sign Out</v-list-tile>
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
import JoinUs from "@/components/Blocks/JoinUs.vue";

export default {
  name: "NavigationDrawer",
  components: {
    UserInfo,
    JoinUs
  },
  data: () => ({
    drawer: false,
    dialog: false,
    logout: false,
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
  methods: {
    signOut() {
      this.$store.dispatch("User/logoutUser");
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
    .v-toolbar__title {
      max-width: 150px;
      .logo-img {
        width: 100%;
      }
    }
    .v-toolbar__content {
      max-width: 1400px;
      margin: auto;
    }
  }
}
</style>
