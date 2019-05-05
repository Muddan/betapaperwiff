/* eslint-disable no-unused-vars */
import Vue from 'vue'
import { endpoints } from '../../api/endpoints'
import * as types from './mutation-types'

const actions = {
  getStoryTags(context, payload) {
    this.$axios({
      method: 'GET',
      url: endpoints.API_GET_TAGS
    }).then(response => {
      if (response.status === 200) {
        const tags = response.data.map(tag => {
          return tag.name
        })
        context.commit(types.SET_AVAILABLE_TAGS, tags)
      }
    })
  },
  async getAllStories(context, payload) {
    await this.$axios.$get(endpoints.API_GET_STORIES).then(response => {
      context.commit(types.SET_ALL_STORIES, response)
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
  publishStory(context, payload) {
    return this.$axios.$post(endpoints.API_PUBLISH_STORY, {
      storyTitle: payload.storyTitle,
      userId: payload.userId,
      content: payload.content,
      tags: payload.tags
    })
  }
}

export default actions
