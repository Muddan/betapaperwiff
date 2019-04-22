/* eslint-disable no-unused-vars */
import { app } from '../../api/endpoints'
import Vue from 'vue'
import * as types from './mutation-types'

const actions = {
  getStoryTags(context, payload) {
    this.$axios({
      method: 'GET',
      url: app.API_GET_TAGS
    }).then(response => {
      if (response.status == 200) {
        let tags = response.data

        tags = tags.map(tag => {
          return tag.name
        })
        context.commit(types.SET_AVAILABLE_TAGS, tags)
      }
    })
  },
  async getAllStories(context, payload) {
    await this.$axios.$get(app.API_GET_STORIES).then(response => {
      context.commit(types.SET_ALL_STORIES, response)
    })
  },
  setStoryFilters(context, payload) {
    context.commit(types.SET_STORY_FILTERS, payload)
  },
  getCurrentStory(context, payload) {
    this.$axios
      .$post(app.API_GET_STORY_DETAILS, {
        storyId: 'motivation-to-be-alive'
      })
      .then(res => {
        if (res.status == 200) {
          context.commit(types.SET_CURRENT_STORY, res.data.details[0])
        } else {
          console.log('Error while fetching story details')
        }
      })
  },
  publishStory(context, payload) {
    return this.$axios
      .$post(app.API_PUBLISH_STORY, {
        storyTitle: payload.storyTitle,
        userId: payload.userId,
        content: payload.content,
        tags: payload.tags
      })
      .then(res => {
        if (res.status === 200) return res.data
        else {
          return 'Error while saving data'
        }
      })
  }
}

export default actions
