import RootState from "@/store/types/rootState"
import { Module } from "vuex"
import UserState from "../../types/userState"
import getters from "./getter"
import mutations from "./mutations"
import actions from "./actions"
const User: Module<UserState, RootState> = {
  namespaced: true,
  state: {
    isSignedIn: false,
    current: {
      user_id: null,
      first_name: "",
      last_name: "",
      username: "",
      email: "",
      following_tags: [],
      followers: null,
      following: null
    },
    session_started: new Date().toLocaleString()
  },
  getters,
  actions,
  mutations
}
export default User
