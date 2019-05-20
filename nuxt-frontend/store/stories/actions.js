/* eslint-disable no-console */
/* eslint-disable no-unused-vars */
import Vue from 'vue'
import _ from 'lodash'
import { endpoints } from '../../api/endpoints'
import * as types from './mutation-types'
const actions = {
  getStoryTags(context, payload) {
    return new Promise((resolve, reject) => {
      return this.$axios({
        method: 'GET',
        url: endpoints.API_GET_TAGS
      }).then(response => {
        if (response.status === 200) {
          if (!localStorage.getItem('paperwiff/tags')) {
            localStorage.setItem(
              'paperwiff/tags',
              JSON.stringify(response.data.result.tags)
            )
          }
          context.commit(types.SET_AVAILABLE_TAGS, response.data.result.tags)
        }
      })
    })
  },
  async getAllStories(context, payload) {
    await this.$axios.$get(endpoints.API_GET_STORIES).then(response => {
      context.commit(types.SET_ALL_STORIES, response.result.items)
    })
  },
  setStoryFilters(context, payload) {
    context.commit(types.SET_STORY_FILTERS, payload)
  },
  getCurrentStory(context, payload) {
    this.$axios
      .$post(endpoints.API_GET_STORY_DETAILS, {
        storyId: payload
      })
      .then(res => {
        context.commit(types.SET_CURRENT_STORY, res.details[0])
      })
  },
  async publishStory(context, payload) {
    const formData = new FormData()
    formData.append('file', payload.headerImage)
    formData.append('upload_preset', endpoints.upload_preset)
    await this.$axios.$post(endpoints.IMAGE_UPLOAD, formData).then(res => {
      payload.headerImage = res.secure_url
      return this.$axios.$post(endpoints.API_PUBLISH_STORY, payload)
    })
  },

  addToFollowingFilters(context, payload) {
    let allTags = _.cloneDeep(context.rootState.stories.availableTags)
    allTags = allTags.map(tag => {
      if (tag.name === payload.name) {
        tag.status = !tag.status
      }
      return tag
    })
    this.$axios
      .$post(
        endpoints.API_FOLLOW_TAG,
        {
          userId: context.rootState.user.current.userId,
          tag: payload.name
        },
        {
          headers: {
            Authorization: 'Bearer ' + context.rootState.user.access_token
          }
        }
      )
      .then(res => {})
    context.commit(types.SET_AVAILABLE_TAGS, allTags)
    if (localStorage.getItem('paperwiff/user')) {
      const userDetails = JSON.parse(
        localStorage.getItem('paperwiff/user') || '{}'
      )
      if (userDetails.followingTags.includes(payload.name)) {
        userDetails.followingTags = userDetails.followingTags.filter(item => {
          return item !== payload.name
        })
      } else {
        userDetails.followingTags.push(payload.name)
      }
      localStorage.setItem('paperwiff/user', JSON.stringify(userDetails))
    }
    context.dispatch(
      'user/getUserDetails',
      context.rootState.user.current.userName,
      { root: true }
    )
    context.dispatch(
      'stories/userFeed',
      context.rootState.user.current.userId,
      { root: true }
    )
  },
  like(context, payload) {
    this.$axios
      .$post(endpoints.API_STORY_LIKE, {
        storyId: payload
      })
      .then(res => {
        console.log(res)
      })
  },
  userFeed(context, payload) {
    this.$axios({
      method: 'GET',
      url: `${endpoints.API_GET_STORIES}?userId=${payload}`
    }).then(res => {
      context.commit(types.SET_USER_FEED, res.data.result.items)
    })
  },
  updateAvailableTags(context, payload) {
    let tags = [[]]
    if (localStorage.getItem('paperwiff/tags')) {
      tags = JSON.parse(localStorage.getItem('paperwiff/tags') || '{}')
    }
    context.commit(types.SET_AVAILABLE_TAGS, tags)
    let allTags = _.cloneDeep(context.rootState.stories.availableTags)
    console.log(payload)

    allTags = allTags.map(tag => {
      if (payload.includes(tag.name)) {
        tag.status = !tag.status
      }
      return tag
    })
    context.commit(types.SET_AVAILABLE_TAGS, allTags)
  }
}

export default actions
