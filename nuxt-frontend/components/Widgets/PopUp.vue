<template>
  <div class="">
    <v-dialog v-model="isVisible" content-class="general-pop-up">
      <keep-alive>
        <component :is="isComponent"></component>
      </keep-alive>
      <div class="close-btn">
        <v-btn icon color="grey darken-4" flat>
          <v-icon color="grey darken-4" @click="closePopup"
            >close</v-icon
          ></v-btn
        >
      </div>
    </v-dialog>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import SignUp from './SignUp'
export default {
  name: 'PopUp',
  components: {
    SignUp
  },
  data() {
    return {
      dialog: false
    }
  },
  computed: mapState({
    isVisible: state => state.ui.isShowPopup,
    isComponent: state => state.ui.componentName
  }),
  methods: {
    closePopup() {
      this.$store.commit('ui/SET_SHOW_POPUP', { status: false, component: '' })
    }
  }
}
</script>
<style lang="scss">
.general-pop-up {
  position: relative;
  max-width: 50%;
  @media (max-width: 768px) {
    max-width: 80%;
  }
  .close-btn {
    position: absolute;
    top: 0;
    right: 0;
  }
}
</style>
