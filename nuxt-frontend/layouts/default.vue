<template>
  <v-app>
    <PopUp></PopUp>
    <ImageViewer></ImageViewer>
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
import ImageViewer from '../components/Widgets/ImageViewer'
export default {
  components: {
    Footer,
    Header,
    PopUp,
    ImageViewer
  },
  async beforeMount() {
    await this.$store.dispatch('user/sessionStart')
    await this.$store.dispatch('stories/getStoryTags')
  }
}
</script>
<style lang="scss">
@import '@/css/main.scss';
</style>
