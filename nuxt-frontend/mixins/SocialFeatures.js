export const SocialFeatures = {
  data() {
    return {
      liked: false,
      liking: false
    }
  },
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
        await this.$store.dispatch('stories/like', storyId)
        this.liked = false
        this.likeCount--
      } else {
        await this.$store.dispatch('stories/like', storyId)
        this.liked = true
        this.likeCount++
      }
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
      // eslint-disable-next-line no-console
      console.log(authorId)
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
