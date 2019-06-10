import getter from './getters'
import action from './actions'
import mutation from './mutations'
export const state = () => ({
  availableTags: [],
  allStories: [],
  totalStories: 0,
  filteredStories: [],
  currentStory: null,
  popularStories: []
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
export const strict = false
