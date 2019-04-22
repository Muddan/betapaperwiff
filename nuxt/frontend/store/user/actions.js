/* eslint-disable no-unused-vars */
import { app } from '../../api/endpoints'
import Vue from 'vue'
import * as types from './mutation-types'

const actions = {
  sessionStart(context, payload) {
    if (localStorage.getItem('paperwiff/user')) {
      let userDetails = JSON.parse(
        localStorage.getItem('paperwiff/user') || '{}'
      )
      let tokens = {
        access_token: userDetails.access_token,
        refresh_token: userDetails.refresh_token
      }
      context.commit(types.SET_SIGNED_STATE, true)
      context.commit(types.SET_ACCESS_TOKENS, tokens)
      context.commit(types.SET_CURRENT_USER, userDetails.userDetails)
    } else {
      console.log('STARTING FREESH')
    }
  },
  loginUser(context, payload) {
    let tokens = {
      access_token: payload.access_token,
      refresh_token: payload.refresh_token
    }
    localStorage.setItem('paperwiff/user', JSON.stringify(payload))
    context.commit(types.SET_ACCESS_TOKENS, tokens)
    context.commit(types.SET_SIGNED_STATE, true)
    context.commit(types.SET_CURRENT_USER, payload.userDetails)
  },
  logoutUser(context, payload) {
    let tokens = {
      access_token: '',
      refresh_token: ''
    }
    context.commit(types.SET_SIGNED_STATE, false)
    context.commit(types.SET_CURRENT_USER, {})
    context.commit(types.SET_ACCESS_TOKENS, tokens)
    localStorage.clear()
  },

  getUserDetails(context, payload) {
    this.$axios({
      method: 'POST',
      url: app.API_GET_USER_DETAILS,
      data: {
        userName: payload
      }
    }).then(res => {
      if (res.status == 200) context.commit(types.SET_USER_PROFILE, res.data)
      else {
        console.log('error fetching use details')
      }
    })
  },

  addToFollowingFilters(context, payload) {
    // Update the tags in sycn with local data
    let userDetails = JSON.parse(localStorage.getItem('paperwiff/user') || '{}')
    if (userDetails.userDetails.followingTags.includes(payload.tag)) {
      userDetails.userDetails.followingTags = userDetails.userDetails.followingTags.filter(
        tag => {
          return tag !== payload.tag
        }
      )
    } else {
      userDetails.userDetails.followingTags.push(payload.tag)
    }
    localStorage.setItem('paperwiff/user', JSON.stringify(userDetails))

    Vue.axios
      .post(
        app.API_FOLLOW_TAG,
        {
          tag: payload.tag,
          userId: '111704191453898225276'
        },
        {
          headers: { Authorization: 'Bearer ' + context.state.access_token }
        }
      )
      .then(res => {
        if (res.status == 200) {
          context.commit(types.FOLLOW_FILTERS, payload.tag)
        } else {
          console.log('Error')
        }
      })
  }
}

export default actions
