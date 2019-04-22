import { app } from "@/endpoints"
import Vue from "vue"
import { ActionTree } from "vuex"
import RootState from "@/store/types/rootState"
import UserState from "../../types/userState"
import * as types from "./mutation-types"

const actions: ActionTree<UserState, RootState> = {
  refreshTokens(context: any, payload: any) {
    console.log("Called my shit")
  },
  sessionStart(context: any, payload: any) {
    if (localStorage.getItem("paperwiff/user")) {
      let userDetails = JSON.parse(
        localStorage.getItem("paperwiff/user") || "{}"
      )
      let tokens = {
        access_token: userDetails.access_token,
        refresh_token: userDetails.refresh_token
      }
      context.commit(types.SET_SIGNED_STATE, true)
      context.commit(types.SET_ACCESS_TOKENS, tokens)
      context.commit(types.SET_CURRENT_USER, userDetails.userDetails)
    } else {
      console.log("FRESH SESSIOn")
    }
  },
  loginUser(context: any, payload: any) {
    let tokens = {
      access_token: payload.access_token,
      refresh_token: payload.refresh_token
    }
    localStorage.setItem("paperwiff/user", JSON.stringify(payload))
    context.commit(types.SET_ACCESS_TOKENS, tokens)
    context.commit(types.SET_SIGNED_STATE, true)
    context.commit(types.SET_CURRENT_USER, payload.userDetails)
  },
  logoutUser(context: any, payload: any) {
    let tokens = {
      access_token: "",
      refresh_token: ""
    }
    context.commit(types.SET_SIGNED_STATE, false)
    context.commit(types.SET_CURRENT_USER, {})
    context.commit(types.SET_ACCESS_TOKENS, tokens)
    localStorage.clear()
  },

  getUserDetails(context: any, payload: any) {
    return Vue.axios({
      method: "POST",
      url: app.API_GET_USER_DETAILS,
      data: {
        userName: payload
      }
    }).then(res => {
      if (res.status == 200) context.commit(types.SET_USER_PROFILE, res.data)
      else {
        console.log("error fetching use details")
      }
    })
  },

  addToFollowingFilters(context: any, payload: any) {
    // Update the tags in sycn with local data
    let userDetails = JSON.parse(localStorage.getItem("paperwiff/user") || "{}")
    if (userDetails.userDetails.followingTags.includes(payload.tag)) {
      userDetails.userDetails.followingTags = userDetails.userDetails.followingTags.filter(
        (tag: any) => {
          return tag !== payload.tag
        }
      )
    } else {
      userDetails.userDetails.followingTags.push(payload.tag)
    }
    localStorage.setItem("paperwiff/user", JSON.stringify(userDetails))

    Vue.axios
      .post(
        app.API_FOLLOW_TAG,
        {
          tag: payload.tag,
          userId: "111704191453898225276"
        },
        {
          headers: { Authorization: "Bearer " + context.state.access_token }
        }
      )
      .then(res => {
        if (res.status == 200) {
          context.commit(types.FOLLOW_FILTERS, payload.tag)
        } else {
          console.log("Error")
        }
      })
  }
}

export default actions
