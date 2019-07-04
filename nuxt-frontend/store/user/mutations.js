/* eslint-disable no-console */
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
    state.current = payload
  },
  [types.FOLLOW_FILTERS](state, payload) {
    if (state.current.followingTags.includes(payload)) {
      state.current.followingTags = state.current.followingTags.filter(tag => {
        return tag !== payload
      })
    } else {
      state.current.followingTags.push(payload)
    }
  },

  [types.SET_READINGLIST](state, payload) {
    state.readingListStories = payload
  },

  [types.SET_PUBLISHED_STORIES](state, payload) {
    state.userArticlesStories = payload
  },
  [types.SET_USER_FEED](state, payload) {
    state.userFeed = payload
  }
}

export default mutations
