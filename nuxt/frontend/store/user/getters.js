const getter = {
  isSignedIn: state => state.isSignedIn,
  currentUser: state => state.current,
  getUserProfile: state => state.userProfile,
  getAccessTokens: state => {
    return {
      acces_token: state.access_token,
      refresh_token: state.refresh_token
    }
  }
}

export default getter
