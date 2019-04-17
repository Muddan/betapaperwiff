import Vue from "vue"
// import * as types from "./mutation-types"
import { ActionTree } from "vuex"
import RootState from "@/store/types/rootState"
import StoriesState from "../../types/storiesState"
import * as types from "./mutation-types"
import axios from "axios"

const actions: ActionTree<StoriesState, RootState> = {
  getStoryTags(context: any, payload: any) {
    // axios({
    //   method: "get",
    //   url: "http://ec2-13-229-247-97.ap-southeast-1.compute.amazonaws.com:5000/"
    //   //   headers: {
    //   //     Token: this.authToken
    //   //   }
    // }).then(response => {
    //   context.commit(types.SET_AVAILABLE_TAGS, response.data.tags)
    // })
    let tags = [
      "Fiction",
      "Action & Adventure",
      "Crime",
      "Drama",
      "Fairytale",
      "Historical Fiction",
      "Horror",
      "Mystery",
      "Paranormal Romance",
      "Poetry",
      "Romance",
      "Sattire",
      "Science Fiction",
      "Suspense",
      "Thriller",
      "Non-Fiction",
      "Art",
      "Biography",
      "Book review",
      "Guide",
      "Travel",
      "Health",
      "History",
      "Memoir",
      "Spirituality",
      "Self-Help",
      "Politics",
      "Shayari"
    ]
    tags = tags.map(tag => {
      return tag.replace(" ", "").toLowerCase()
    })
    context.commit(types.SET_AVAILABLE_TAGS, tags)
  },
  getAllStories(context: any, payload: any) {
    axios({
      method: "get",
      url:
        "http://ec2-13-229-247-97.ap-southeast-1.compute.amazonaws.com:5000/stories/"
      //   headers: {
      //     Token: this.authToken
      //   }
    }).then(response => {
      context.commit(types.SET_ALL_STORIES, response.data)
    })
  },
  setStoryFilters(context: any, payload: any) {
    context.commit(types.SET_STORY_FILTERS, payload)
  },
  getCurrentStory(context: any, payload: any) {
    context.commit(types.SET_CURRENT_STORY, payload)
  }
}

export default actions
