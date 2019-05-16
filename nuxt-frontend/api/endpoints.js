const BASE_URL = `http://127.0.0.1:5000`

export const endpoints = {
  BASE_URL: BASE_URL,

  // USER ENDPOINTS
  API_GET_USER_DETAILS: `${BASE_URL}/api/user/details`,
  API_FOLLOW_TAG: `${BASE_URL}/api/user/followtag`,
  API_USER_UPDATE: `${BASE_URL}/api/user/updateUser`,
  API_USER_STORIES: `${BASE_URL}/api/story/allstories`,

  // STORY ENDPOINTS
  API_PUBLISH_STORY: `${BASE_URL}/api/story/publish`,
  API_GET_STORIES: `${BASE_URL}/api/story/allstories`,
  API_GET_TAGS: `${BASE_URL}/api/story/alltags`,
  API_GET_STORY_DETAILS: `${BASE_URL}/api/story/storydetails`,
  API_TRANSTLATE: `${BASE_URL}/api/story/translate`,
  API_STORY_LIKE: `${BASE_URL}/api/story/storyLike`
}
