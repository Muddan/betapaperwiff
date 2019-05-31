/* eslint-disable no-console */
/* eslint-disable no-unused-vars */
import Vue from 'vue'
import { endpoints } from '../../api/endpoints'
import * as types from './mutation-types'
const actions = {
  getStoryTags(context, payload) {
    return this.$axios({
      method: 'GET',
      url: endpoints.API_GET_TAGS
    }).then(response => {
      if (response.status === 200) {
        context.commit(types.SET_AVAILABLE_TAGS, response.data.result.tags)
      }
    })
  },
  async getAllStories(context, payload) {
    await this.$axios.$get(endpoints.API_GET_STORIES).then(response => {
      context.commit(types.SET_ALL_STORIES, response.result.items)
      context.commit(types.SET_TOTAL_STORIES, response.result.totalItems)
    })
  },
  loadMoreStories(context, payload) {
    if (
      context.rootState.stories.allStories.length <
      context.rootState.stories.totalStories
    ) {
      this.$axios
        .$get(`${endpoints.API_GET_STORIES}?pageNo=${payload}`)
        .then(response => {
          context.commit(types.SET_ALL_STORIES, {
            items: response.result.items,
            loadMore: true
          })
        })
    }
  },
  async publishStory(context, payload) {
    const formData = new FormData()
    formData.append('file', payload.headerImage)
    formData.append('upload_preset', endpoints.upload_preset)
    await this.$axios.$post(endpoints.IMAGE_UPLOAD, formData).then(res => {
      payload.headerImage = res.secure_url
      this.$axios
        .$post(endpoints.API_PUBLISH_STORY, payload, {
          headers: {
            Authorization: 'Bearer ' + context.rootState.user.access_token
          }
        })
        .then(res => {
          if (res.result.status === 200) {
            context.dispatch('getAllStories')
            context.dispatch(
              'notification/success',
              {
                title: 'Success!',
                message: res.result.msg
              },
              { root: true }
            )
          } else {
            context.dispatch(
              'notification/error',
              {
                title: 'Failed!',
                message: res.result.msg
              },
              { root: true }
            )
          }
          context.dispatch('getAllStories')
          return res.result
        })
    })
  },

  addToFollowingFilters(context, payload) {
    this.$axios
      .$post(
        endpoints.API_FOLLOW_TAG,
        {
          userId: context.rootState.user.current.userId,
          tags: [payload.name]
        },
        {
          headers: {
            Authorization: 'Bearer ' + context.rootState.user.access_token
          }
        }
      )
      .then(res => {
        context.dispatch('getStoryTags')
      })
    context.dispatch(
      'user/getUserDetails',
      context.rootState.user.current.userId,
      { root: true }
    )
    context.dispatch(
      'stories/userFeed',
      context.rootState.user.current.userId,
      { root: true }
    )
  },
  like(context, payload) {
    if (context.rootState.user.isSignedIn) {
      this.$axios
        .$post(
          endpoints.API_STORY_LIKE,
          {
            storyId: payload,
            userId: context.rootState.user.current.userId
          },
          {
            headers: {
              Authorization: 'Bearer ' + context.rootState.user.access_token
            }
          }
        )
        .then(res => {
          context.dispatch('getAllStories')
          context.dispatch(
            'user/getUserDetails',
            context.rootState.user.current.userId,
            { root: true }
          )
        })
    }
  },
  userFeed(context, payload) {
    this.$axios(
      {
        method: 'GET',
        url: `${endpoints.API_GET_STORIES}?userId=${payload}`
      },
      {
        headers: {
          Authorization: 'Bearer ' + context.rootState.user.access_token
        }
      }
    ).then(res => {
      context.commit(types.SET_USER_FEED, res.data.result.items)
    })
  }
}

export default actions
