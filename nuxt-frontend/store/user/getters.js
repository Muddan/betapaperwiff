const getter = {
  isSignedIn: state => state.isSignedIn,
  currentUser: state => state.current,
  getAccessTokens: state => {
    return {
      acces_token: state.access_token,
      refresh_token: state.refresh_token
    }
  },
  userTags: state => state.current.followingTags,
  likedStories: state => state.current.likedStories,
  followingAuthors: state => state.current.followingAuthors,
  savedStories: state => state.current.saveForLater,
  followingTags: state => state.current.followingTags
}

export default getter
