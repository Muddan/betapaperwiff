<template>
  <v-app>
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
<style lang="scss">
/** Transitions */
.application {
  background: #f9f9f9 !important;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.1s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
.slidedown-enter-active,
.slidedown-leave-active {
  transition: transform 0.3s, opacity 0.3s;
}
.slidedown-enter, .slidedown-leave-to /* .fade-leave-active below version 2.1.8 */ {
  transform: translateY(10%);
  opacity: 0;
  max-width: 1400px;
  overflow: hidden;
}
</style>
