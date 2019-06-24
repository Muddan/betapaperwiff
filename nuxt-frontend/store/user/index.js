import getter from './getters'
import action from './actions'
import mutation from './mutations'
export const state = () => ({
  isSignedIn: false,
  access_token: '',
  refresh_token: '',
  readingListStories: [],
  userArticlesStories: [],
  current: {
    userId: null,
    firstName: '',
    lastName: '',
    userName: '',
    email: '',
    followingTags: [],
    followingAuthors: [],
    joined: '',
    about: '',
    userImage: '',
    userArticles: [],
    likedStories: [],
    accountLicense: 'free',
    location: '',
    skills: '',
    languages: [],
    availableFor: '',
    saveForLater: []
  },
  session_started: new Date().toLocaleString()
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
