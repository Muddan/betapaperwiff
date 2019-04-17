import Vue from "vue"
// import * as types from "./mutation-types"
import { ActionTree } from "vuex"
import RootState from "@/store/types/rootState"
import UserState from "../../types/userState"
import * as types from "./mutation-types"
import axios from "axios"

const actions: ActionTree<UserState, RootState> = {
  sessionStart(context: any, payload: any) {
    if (localStorage.getItem("paperwiff/user")) {
      console.log("SESSION EXISTS")
      let userDetails = JSON.parse(
        localStorage.getItem("paperwiff/user") || "{}"
      )
      context.commit(types.SET_SIGNED_STATE, true)
      context.commit(types.SET_CURRENT_USER, userDetails.currentUser)
    } else {
      console.log("UNAUTHENTICCATED USER")
    }
  },
  loginUser(context: any, payload: any) {
    let loginInUser = {
      isSignedIn: true,
      currentUser: {
        ...payload,
        following_tags: [],
        followers: null,
        following: null
      }
    }
    localStorage.setItem("paperwiff/user", JSON.stringify(loginInUser))
    context.commit(types.SET_SIGNED_STATE, true)
    context.commit(types.SET_CURRENT_USER, loginInUser.currentUser)
  },
  logoutUser(context: any, payload: any) {
    context.commit(types.SET_SIGNED_STATE, false)
    context.commit(types.SET_CURRENT_USER, {})
    localStorage.clear()
  },

  getUserDetails(context: any, payload: any) {},

  addToFollowingFilters(context: any, payload: any) {
    context.commit(types.FOLLOW_FILTERS, payload.tag)
  }
}

export default actions
