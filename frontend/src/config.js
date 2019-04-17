let BASE_URL = process.env.VUE_APP_BASE_URL

export default {
  app: {
    BASE_URL: BASE_URL,
    API_CREATE_STORY: `${BASE_URL}/create`,
    API_GET_STORIES: `${BASE_URL}/stories/`,
    API_GET_STORY: `${BASE_URL}/story/:storyId`,
    API_GET_USER_STORY: `${BASE_URL}/user/story/:storyId`,
    API_GET_USER: `${BASE_URL}/user/:userId`,
    API_GET_CATEGORIES: `${BASE_URL}/categories`
  },
  cognito: {
    REGION: "ap-southeast-1",
    USER_POOL_ID: "ap-southeast-1_RRHfQuiCv",
    APP_CLIENT_ID: "3h5bsc07q3j273lpft45hiu19m"
  }
}
