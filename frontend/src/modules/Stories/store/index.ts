import RootState from "@/store/types/rootState"
import { Module } from "vuex"
import StoriesState from "../../types/storiesState"
import getters from "./getter"
import mutations from "./mutations"
import actions from "./actions"

const Stories: Module<StoriesState, RootState> = {
  namespaced: true,
  state: {
    availableTags: [],
    allStories: [],
    filteredStories: [],
    currentStory: null
  },
  getters,
  actions,
  mutations
}
export default Stories
