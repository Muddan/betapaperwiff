/* eslint-disable no-console */
import Vue from 'vue'
import * as types from './mutation-types'
const mutations = {
  /**
   * Adds all available story tags in the store
   * @param state
   * @param payload
   */
  [types.SET_AVAILABLE_TAGS](state, payload) {
    payload.forEach((tag, index) => {
      Vue.set(state.availableTags, index, tag)
    })
    // state.availableTags = payload
  },
  /**
   * Adds all stories in the store
   * @param state
   * @param payload
   */
  [types.SET_ALL_STORIES](state, payload) {
    if (state.allStories.length) {
      const currentStories = state.allStories
      state.allStories = currentStories.concat(payload)
    } else {
      state.allStories = payload
    }
  },
  [types.SET_TOTAL_STORIES](state, payload) {
    state.totalStories = payload
  },

  /**
   * Applies single filter to the story listing
   * @param state
   * @param payload
   */
  [types.SET_STORY_FILTERS](state, payload) {
    const afterFilter = state.allStories.filter(story => {
      return story.tags.includes(payload.tag)
    })
    state.filteredStories = afterFilter
  },

  [types.SET_CURRENT_STORY](state, payload) {
    state.currentStory = payload
  },
  [types.SET_USER_FEED](state, payload) {
    state.filteredStories = payload
  }
}

export default mutations
