/* eslint-disable no-console */
/* eslint-disable no-unused-vars */
import Vue from 'vue'
import { endpoints } from '../../api/endpoints'
import * as types from './mutation-types'

const actions = {
  async sessionStart(context, payload) {
    if (localStorage.getItem('paperwiff/user')) {
      const userDetails = JSON.parse(
        localStorage.getItem('paperwiff/user') || '{}'
      )
      const tokens = {
        access_token: userDetails.access_token,
        refresh_token: userDetails.refresh_token
      }
      context.commit(types.SET_SIGNED_STATE, true)
      context.commit(types.SET_ACCESS_TOKENS, tokens)
      await context.dispatch('getUserDetails', userDetails.userName)
      await context.dispatch('stories/userFeed', userDetails.userId, {
        root: true
      })
      await context.dispatch(
        'stories/updateAvailableTags',
        userDetails.followingTags,
        { root: true }
      )
    }
  },
  loginUser(context, payload) {
    const tokens = {
      access_token: payload.access_token,
      refresh_token: payload.refresh_token
    }
    localStorage.setItem(
      'paperwiff/user',
      JSON.stringify({
        access_token: payload.access_token,
        refresh_token: payload.refresh_token,
        userName: payload.userDetails.userName,
        userId: payload.userDetails.userId,
        followingTags: payload.userDetails.followingTags
      })
    )
    context.commit(types.SET_ACCESS_TOKENS, tokens)
    context.commit(types.SET_SIGNED_STATE, true)
    context.commit(types.SET_CURRENT_USER, payload.userDetails)
    context.dispatch(
      'stories/userFeed',
      context.rootState.user.current.userId,
      { root: true }
    )
    context.dispatch(
      'stories/updateAvailableTags',
      context.rootState.user.current.followingTags,
      { root: true }
    )
  },
  setTokens(context, payload) {
    context.commit(types.SET_ACCESS_TOKENS, payload)
  },
  logoutUser(context, payload) {
    const tokens = {
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
      url: endpoints.API_GET_USER_DETAILS,
      data: {
        userName: payload
      }
    }).then(res => {
      if (res.status === 200) {
        context.commit(types.SET_USER_PROFILE, res.data.result)
      }
    })
  },
  updateUserDetails(context, payload) {
    return new Promise((resolve, reject) => {
      this.$axios
        .$post(endpoints.API_USER_UPDATE, payload)
        .then(res => {
          if (res.status === 200) {
            // context.dispatch('getUserDetails', payload.userName)
            context.commit(types.SET_USER_PROFILE, res.data.result)
          }
          resolve(true)
        })
        .catch(e => {
          resolve(false)
        })
    })
  }
}
export default actions
