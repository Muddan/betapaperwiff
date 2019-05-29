export const SocialFeatures = {
  methods: {
    /**
     * @param story
     * Likes story
     */
    async likeStory(storyId) {
      if (!this.isSignedIn) {
        this.$store.commit('ui/SET_SHOW_POPUP', {
          status: true,
          component: 'SignUp'
        })
        return
      }
      if (this.likedStories.includes(storyId)) {
        this.likeCount--
      } else {
        this.likeCount++
      }
      await this.$store.dispatch('stories/like', storyId)
    },
    /**
     * @param authorID
     * Follows current story Author
     */
    async followAuthor(authorId) {
      if (!this.isSignedIn) {
        this.$store.commit('ui/SET_SHOW_POPUP', {
          status: true,
          component: 'SignUp'
        })
        return
      }
      await this.$store.dispatch('user/followAuthor', authorId)
    },
    /**
     * @param storyId
     * Follows current story Author
     */
    async saveStory(storyId) {
      if (!this.isSignedIn) {
        this.$store.commit('ui/SET_SHOW_POPUP', {
          status: true,
          component: 'SignUp'
        })
        return
      }
      await this.$store.dispatch('user/saveLater', storyId)
    }
  }
}
