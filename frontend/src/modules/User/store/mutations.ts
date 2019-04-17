import Vue from "vue"
import { MutationTree } from "vuex"
import UserState from "../../types/userState"
import * as types from "./mutation-types"

const mutations: MutationTree<UserState> = {
  [types.SET_SIGNED_STATE](state, payload) {
    state.isSignedIn = payload
  },

  [types.SET_CURRENT_USER](state, payload) {
    state.current = payload
  },
  [types.FOLLOW_FILTERS](state, payload) {
    if (state.current.following_tags.includes(payload)) {
      state.current.following_tags = state.current.following_tags.filter(
        (tag: any) => {
          return tag !== payload
        }
      )
    } else {
      state.current.following_tags.push(payload)
    }
  }
}

export default mutations
