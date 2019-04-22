import getter from './getters'
import action from './actions'
import mutation from './mutations'
export const state = () => ({
  availableTags: [],
  allStories: [],
  filteredStories: [],
  currentStory: null
})
export const getters = () => ({
  getter
})
export const actions = () => ({
  action
})
export const mutations = () => ({
  mutation
})
