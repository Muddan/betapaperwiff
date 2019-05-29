const getter = {
  availableTags: state => state.availableTags,
  allStories: state => state.allStories,
  filteredStories: state => state.filteredStories,
  currentStory: state => state.currentStory,
  totalStories: state => state.totalStories
}

export default getter
