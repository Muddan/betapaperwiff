<template>
  <div class="nav-bar">
    <v-navigation-drawer app v-model="drawer" disable-resize-watcher>
      <v-list>
        <v-list class="pa-1">
          <v-list-tile avatar>
            <v-list-tile-avatar>
              <img src="https://randomuser.me/api/portraits/women/85.jpg">
            </v-list-tile-avatar>

            <v-list-tile-content>
              <v-list-tile-title>John Leider</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
        <template v-for="(item, index) in items">
          <v-list-tile :key="index">
            <v-list-tile-content>{{item.title}}</v-list-tile-content>
          </v-list-tile>
          <v-divider :key="`divider-${index}`"></v-divider>
        </template>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar app color="white" :scrollOffScreen="true">
      <v-toolbar-side-icon class="hidden-md-and-up" @click="drawer = !drawer"></v-toolbar-side-icon>

      <v-spacer class="hidden-md-and-up"></v-spacer>
      <div class="app-title">
        <router-link to="/">
          <img src="@/assets/logo.png" alt="local restaurants">
        </router-link>
      </div>
      <v-btn v-for="icon in icons" :key="icon" class="mx-3" icon>
        <v-icon size="24px">{{ icon }}</v-icon>
      </v-btn>
      <v-spacer class="hidden-sm-and-down"></v-spacer>

      <!-- Search icon -->
      <v-dialog v-model="dialog" :full-width="true" :fullscreen="false">
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on">
            <v-icon color="#114b5f">search</v-icon>
          </v-btn>
        </template>
        <v-card>
          <v-card-title class="headline">Use Google's location service?</v-card-title>
          <v-card-text>Let Google help apps determine location. This means sending anonymous location data to Google, even when no apps are running.</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="green darken-1" flat @click="dialog = false">Disagree</v-btn>
            <v-btn color="green darken-1" flat @click="dialog = false">Agree</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>

      <!-- Write icon -->
      <v-btn color="#114b5f" class="hidden-sm-and-down" flat value="help">
        <v-icon left>fas fa-edit</v-icon>
        <span>Write</span>
      </v-btn>
      <v-menu bottom offset-y>
        <template v-slot:activator="{ on }">
          <v-btn v-on="on" flat icon color="#f45b69">
            <v-icon>apps</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-tile v-for="(item, i) in items" :key="i" @click>
            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
          </v-list-tile>
        </v-list>
      </v-menu>
      <!-- <router-link to="/login" class="hidden-sm-and-down"></router-link> -->
    </v-toolbar>
  </div>
</template>
<script>
export default {
  name: "NavigationDrawer",
  data: () => ({
    drawer: false,
    dialog: false,
    appTitle: "Walker",
    items: [{ title: "Menu" }, { title: "Sign In" }, { title: "Join" }],
    icons: ["fab fa-facebook", "fab fa-twitter", "fab fa-instagram"]
  }),
  props: {
    source: String
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
    box-shadow: none;
    .v-toolbar__content {
      max-width: 1400px;
      margin: auto;
    }
  }
}
</style>
