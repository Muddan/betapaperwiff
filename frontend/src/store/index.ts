import Vue from "vue"
import Vuex from "vuex"
import User from "../modules/User/store"
import Stories from "../modules/Stories/store"

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    User,
    Stories
  }
})
export default store
