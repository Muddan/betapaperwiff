let BASE_URL = `${process.env.VUE_APP_BASE_URL}/api`

export const app = {
  BASE_URL: BASE_URL,

  // USER ENDPOINTS
  API_GET_USER_DETAILS: `${BASE_URL}/user/details`,
  API_FOLLOW_TAG: `${BASE_URL}/user/followtag`,

  // STORY ENDPOINTS
  API_PUBLISH_STORY: `${BASE_URL}/story/publish`,
  API_GET_STORIES: `${BASE_URL}/story/allstories`,
  API_GET_TAGS: `${BASE_URL}/story/alltags`,
  API_GET_STORY_DETAILS: `${BASE_URL}/story/storydetails`,
  API_TRANSTLATE: `${BASE_URL}/story/translate`
}
