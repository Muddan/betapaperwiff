const BASE_URL = `https://paperwiff.com`
const CLOUDINARY = {
  cloud_name: 'wokong'
}

export const endpoints = {
  BASE_URL: BASE_URL,
  upload_preset: 'paperwiff',

  // USER ENDPOINTS
  API_USER_UPDATE: `${BASE_URL}/api/user/updateUser`,
  API_USER_STORIES: `${BASE_URL}/api/user/userfeed`,
  API_USER_AUTH: `${BASE_URL}/api/auth/signin`,
  API_GET_USER_DETAILS: `${BASE_URL}/api/user/details`,
  API_GET_USER_PROFILE: `${BASE_URL}/api/user/profile`,

  // Social Features
  API_FOLLOW_TAG: `${BASE_URL}/api/user/follow/tag`,
  API_FOLLOW_AUTHOR: `${BASE_URL}/api/user/follow/author`,
  API_STORY_LIKE: `${BASE_URL}/api/user/story/like`,
  API_STORY_SAVE: `${BASE_URL}/api/user/story/save`,

  // AUthor details
  API_GET_AUTHOR_DETAILS: `${BASE_URL}/api/user/authorDetails`,

  // STORY ENDPOINTS
  API_PUBLISH_STORY: `${BASE_URL}/api/story/publish`,
  API_GET_STORIES: `${BASE_URL}/api/story/allstories`,
  API_GET_TAGS: `${BASE_URL}/api/story/alltags`,
  API_GET_STORY_DETAILS: `${BASE_URL}/api/story/details`,
  API_TRANSTLATE: `${BASE_URL}/api/story/translate`,
  API_GET_TAG_STORIES: `${BASE_URL}/api/story/tag/stories`,

  // Misc Apis
  IMAGE_UPLOAD: `https://api.cloudinary.com/v1_1/${
    CLOUDINARY.cloud_name
  }/upload`
}
