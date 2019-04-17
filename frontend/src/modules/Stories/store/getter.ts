import { GetterTree } from "vuex"
import RootState from "@/store/types/rootState"
import StoriesState from "../../types/storiesState"

const getters: GetterTree<StoriesState, RootState> = {
  availableTags: state => state.availableTags,
  allStories: state => state.allStories,
  filteredStories: state => state.filteredStories,
  currentStory: state => state.currentStory
}

export default getters
