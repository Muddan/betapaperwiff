<template>
  <v-app>
    <PopUp></PopUp>
    <Header></Header>
    <v-content>
      <nuxt />
    </v-content>
    <Footer></Footer>
  </v-app>
</template>
<script>
import Header from '../components/Header'
import Footer from '../components/Footer'
import PopUp from '../components/Widgets/PopUp'
export default {
  components: {
    Footer,
    Header,
    PopUp
  },
  async beforeMount() {
    await this.$store.dispatch('user/sessionStart')
    await this.$store.dispatch('stories/getAllStories')
    await this.$store.dispatch('stories/getStoryTags')
  }
}
</script>
<style lang="scss">
@import '@/css/main.scss';
</style>
