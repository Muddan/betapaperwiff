import getter from './getters'
import action from './actions'
import mutation from './mutations'
export const state = () => ({
  isSignedIn: false,
  access_token: '',
  refresh_token: '',
  current: {
    userId: null,
    firstName: '',
    lastName: '',
    userName: '',
    email: '',
    followingTags: [],
    followingAuthors: null,
    joined: '',
    about: '',
    userImage: '',
    userArticles: [],
    likedStories: [],
    accountLicense: 'free'
  },
  session_started: new Date().toLocaleString(),
  userProfile: null
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
