<template>
  <keep-alive>
    <component :is="getComponent"></component>
  </keep-alive>
</template>
<script>
import PageNotFound from '../components/Errors/PageNotFound.vue'
export default {
  components: {
    PageNotFound
  },
  props: {
    error: {
      type: Object,
      default: null
    }
  },
  computed: {
    getComponent() {
      if (this.error.statusCode === 404) {
        return 'PageNotFound'
      } else {
        return ''
      }
    }
  }
}
</script>

<style></style>
