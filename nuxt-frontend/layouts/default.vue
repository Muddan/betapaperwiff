<template>
  <v-app class="grey lighten-5">
    <Header></Header>
    <v-content>
      <nuxt />
    </v-content>
    <Footer></Footer>
    <!-- <v-navigation-drawer v-model="rightDrawer" :right="right" temporary fixed>
      <v-list>
        <v-list-tile @click.native="right = !right">
          <v-list-tile-action>
            <v-icon light>compare_arrows</v-icon>
          </v-list-tile-action>
          <v-list-tile-title>Switch drawer (click me)</v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer> -->
  </v-app>
</template>
<script>
import Header from '../components/Header'
import Footer from '../components/Footer'
export default {
  components: {
    Footer,
    Header
  },
  mounted() {
    this.$store.dispatch('user/sessionStart')
    this.$store.dispatch('stories/getAllStories')
    this.$store.dispatch('stories/getStoryTags')
  }
}
</script>
