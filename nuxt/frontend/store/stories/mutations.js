import * as types from './mutation-types'

const mutations = {
  /**
   * Adds all available story tags in the store
   * @param state
   * @param payload
   */
  [types.SET_AVAILABLE_TAGS](state, payload) {
    state.availableTags = payload
  },

  /**
   * Adds all stories in the store
   * @param state
   * @param payload
   */
  [types.SET_ALL_STORIES](state, payload) {
    state.allStories = payload
  },

  /**
   * Applies single filter to the story listing
   * @param state
   * @param payload
   */
  [types.SET_STORY_FILTERS](state, payload) {
    let afterFilter = state.allStories.filter(story => {
      return story.tags.includes(payload.tag)
    })
    state.filteredStories = afterFilter
  },

  [types.SET_CURRENT_STORY](state, payload) {
    state.currentStory = payload
  }
}

export default mutations
