<template>
  <div class="header-main">
    <v-navigation-drawer v-model="drawer" app :disable-resize-watcher="true">
      <v-list>
        <v-list-tile
          v-for="(link, i) in mobileLinks"
          :key="i"
          :to="link.to"
          router
          exact
        >
          <v-list-tile-action>
            <v-icon>{{ link.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title v-text="link.title" />
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar height="80px" flat app class="white" :scroll-off-screen="true">
      <v-toolbar-side-icon class="hidden-md-and-up" @click="drawer = !drawer" />
      <v-toolbar-title>
        <span class="font-weight-light">paper</span><span>wiff</span>
      </v-toolbar-title>
      <v-spacer />
      <v-btn color="#337fb5" flat>
        <v-icon color="#337fb5" size="18px" left>create</v-icon>
        <span>Write</span>
      </v-btn>
      <!-- <v-btn icon @click.stop="rightDrawer = !rightDrawer">
        <v-icon>menu</v-icon>
      </v-btn> -->
    </v-toolbar>
  </div>
</template>

<script>
export default {
  name: 'Header',
  data() {
    return {
      drawer: false,
      mobileLinks: [
        {
          icon: 'apps',
          title: 'Welcome',
          to: '/'
        },
        {
          icon: 'bubble_chart',
          title: 'Inspire',
          to: '/inspire'
        }
      ]
    }
  }
}
</script>

<style lang="scss">
.header-main {
  .v-toolbar {
    .v-toolbar__content {
      max-width: 1400px;
      margin: auto;
      padding: 0;
    }
  }
}
</style>
