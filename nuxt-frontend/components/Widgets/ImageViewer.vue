<template>
  <div class="">
    <v-dialog v-model="isShowImageViewer" content-class="imageview-pop">
      <img class="profile-img" :src="imageViewUrl" />
    </v-dialog>
  </div>
</template>

<script>
export default {
  name: 'ImageViewer',
  data() {
    return {
      dialog: false
    }
  },
  computed: {
    isShowImageViewer: {
      get: function() {
        return this.$store.state.ui.isShowImageViewer
      },
      set: function() {
        this.$store.commit('ui/SET_IMAGE_VIEWER', {
          status: false
        })
      }
    },
    imageViewUrl: {
      get() {
        return this.$store.state.ui.imageViewUrl
      },
      set() {
        this.$store.commit('ui/SET_IMAGE_VIEWER', {
          status: false,
          imageViewUrl: ''
        })
      }
    }
  }
}
</script>
<style lang="scss" scoped>
.profile-img {
  width: 100%;
  display: inherit;
}
</style>
<style lang="scss">
.imageview-pop {
  height: auto;
  max-width: 30%;
  @media (max-width: 768px) {
    max-width: 100%;
  }
}
</style>
