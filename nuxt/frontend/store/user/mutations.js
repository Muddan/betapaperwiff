import * as types from './mutation-types'

const mutations = {
  [types.SET_SIGNED_STATE](state, payload) {
    state.isSignedIn = payload
  },

  [types.SET_CURRENT_USER](state, payload) {
    state.current = payload
  },
  [types.SET_ACCESS_TOKENS](state, payload) {
    state.access_token = payload.access_token
    state.refresh_token = payload.refresh_token
  },

  [types.SET_USER_PROFILE](state, payload) {
    state.userProfile = payload
  },
  [types.FOLLOW_FILTERS](state, payload) {
    if (state.current.followingTags.includes(payload)) {
      state.current.followingTags = state.current.followingTags.filter(tag => {
        return tag !== payload
      })
      console.log(state.current.followingTags)
    } else {
      state.current.followingTags.push(payload)
    }
  }
}

export default mutations
