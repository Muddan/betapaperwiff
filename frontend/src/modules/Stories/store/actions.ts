import { app } from "@/endpoints"

import Vue from "vue"
import { ActionTree } from "vuex"
import RootState from "@/store/types/rootState"
import StoriesState from "../../types/storiesState"
import * as types from "./mutation-types"

const actions: ActionTree<StoriesState, RootState> = {
  getStoryTags(context: any, payload: any) {
    Vue.axios({
      method: "GET",
      url: app.API_GET_TAGS
    }).then(response => {
      if (response.status == 200) {
        let tags = response.data

        tags = tags.map((tag: any) => {
          return tag.name
        })
        context.commit(types.SET_AVAILABLE_TAGS, tags)
      }
    })
  },
  getAllStories(context: any, payload: any) {
    Vue.axios.get(app.API_GET_STORIES).then(response => {
      context.commit(types.SET_ALL_STORIES, response.data)
    })
  },
  setStoryFilters(context: any, payload: any) {
    context.commit(types.SET_STORY_FILTERS, payload)
  },
  getCurrentStory(context: any, payload: any) {
    Vue.axios
      .post(app.API_GET_STORY_DETAILS, {
        storyId: payload
      })
      .then(res => {
        if (res.status == 200) {
          context.commit(types.SET_CURRENT_STORY, res.data.details[0])
        } else {
          console.log("Error while fetching story details")
        }
      })
  },
  publishStory(context: any, payload: any) {
    return Vue.axios
      .post(app.API_PUBLISH_STORY, {
        storyTitle: payload.storyTitle,
        userId: payload.userId,
        content: payload.content,
        tags: payload.tags
      })
      .then(res => {
        if (res.status === 200) return res.data
        else {
          return "Error while saving data"
        }
      })
  },
  translate(context: any, payload: any) {
    return Vue.axios.post(app.API_TRANSTLATE, {
      query: payload.query,
      language: payload.language
    })
  }
}

export default actions
