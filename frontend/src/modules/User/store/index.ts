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
    access_token: "",
    refresh_token: "",
    current: {
      userId: null,
      firstName: "",
      lastName: "",
      userName: "",
      email: "",
      followingTags: [],
      followingAuthors: null,
      joined: "",
      about: "",
      userImage: "",
      userArticles: [],
      likedStories: [],
      accountLicense: "free"
    },
    session_started: new Date().toLocaleString(),
    userProfile: null
  },
  getters,
  actions,
  mutations
}
export default User
