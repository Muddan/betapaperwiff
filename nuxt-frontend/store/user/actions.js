/* eslint-disable no-console */
/* eslint-disable no-unused-vars */
import Vue from 'vue'
import firebase from 'firebase'
import { endpoints } from '../../api/endpoints'
import * as types from './mutation-types'
import 'firebase/auth'

const actions = {
  sessionStart(context, payload) {
    firebase.auth().onAuthStateChanged(async function(user) {
      if (user) {
        const currentUser = firebase.auth().currentUser
        context.commit(types.SET_SIGNED_STATE, true)

        const accessKeys = localStorage.getItem('paperwiff/user') || {}
        context.commit(types.SET_ACCESS_TOKENS, JSON.parse(accessKeys))

        await context.dispatch('getUserDetails', currentUser.uid)
        await context.dispatch('stories/userFeed', currentUser.uid, {
          root: true
        })
      }
    })
  },

  authenticate(context, payload) {
    this.$axios
      .$post(endpoints.API_USER_AUTH, {
        id_token: payload
      })
      .then(res => {
        context.dispatch('loginUser', res)
      })
  },

  async loginUser(context, payload) {
    const tokens = {
      access_token: payload.access_token,
      refresh_token: payload.refresh_token
    }
    localStorage.setItem(
      'paperwiff/user',
      JSON.stringify({
        access_token: payload.access_token,
        refresh_token: payload.refresh_token,
        userId: payload.userDetails.userId
      })
    )
    context.commit(types.SET_ACCESS_TOKENS, tokens)
    await context.commit(types.SET_SIGNED_STATE, true)
    await context.commit(types.SET_CURRENT_USER, payload.userDetails)
    context.dispatch(
      'notification/success',
      {
        title: 'Logged In',
        message: 'Welcome to paperwiff'
      },
      { root: true }
    )
    if (context.rootState.user.current.userId) {
      context.dispatch(
        'stories/userFeed',
        context.rootState.user.current.userId,
        { root: true }
      )
    }
  },
  setTokens(context, payload) {
    localStorage.setItem(
      'paperwiff/user',
      JSON.stringify({
        access_token: payload.access_token,
        refresh_token: payload.refresh_token
      })
    )
    context.commit(types.SET_ACCESS_TOKENS, payload)
  },

  logoutUser(context, payload) {
    firebase
      .auth()
      .signOut()
      .then(function() {
        console.log('SIGNOUT')
      })
    const tokens = {
      access_token: '',
      refresh_token: ''
    }
    context.commit(types.SET_SIGNED_STATE, false)
    context.commit(types.SET_CURRENT_USER, {})
    context.commit(types.SET_ACCESS_TOKENS, tokens)
    localStorage.clear()
  },

  async getUserDetails(context, payload) {
    await this.$axios
      .$post(
        endpoints.API_GET_USER_DETAILS,
        {
          userId: payload
        },
        {
          headers: {
            Authorization: 'Bearer ' + context.rootState.user.access_token
          }
        }
      )
      .then(res => {
        context.commit(types.SET_USER_PROFILE, res.result)
      })
  },
  updateUserDetails(context, payload) {
    return new Promise((resolve, reject) => {
      this.$axios
        .$post(endpoints.API_USER_UPDATE, payload, {
          headers: {
            Authorization: 'Bearer ' + context.rootState.user.access_token
          }
        })
        .then(res => {
          context.dispatch('getUserDetails', payload.userId)
          // context.commit(types.SET_USER_PROFILE, res.data.result)
          resolve(true)
        })
        .catch(e => {
          resolve(false)
        })
    })
  },
  followAuthor(context, payload) {
    this.$axios({
      method: 'POST',
      url: endpoints.API_FOLLOW_AUTHOR,
      data: {
        userId: context.rootState.user.current.userId,
        authorId: payload
      },
      headers: {
        Authorization: 'Bearer ' + context.rootState.user.access_token
      }
    }).then(async res => {
      if (res.status === 200) {
        await context.dispatch(
          'getUserDetails',
          context.rootState.user.current.userId
        )

        context.dispatch(
          'notification/success',
          {
            title: '',
            message: res.data.result.msg
          },
          { root: true }
        )
      }
    })
  },
  saveLater(context, payload) {
    this.$axios({
      method: 'POST',
      url: endpoints.API_STORY_SAVE,
      data: {
        userId: context.rootState.user.current.userId,
        storyId: payload
      },
      headers: {
        Authorization: 'Bearer ' + context.rootState.user.access_token
      }
    }).then(async res => {
      if (res.status === 200) {
        await context.dispatch(
          'getUserDetails',
          context.rootState.user.current.userId
        )

        context.dispatch(
          'notification/success',
          {
            title: '',
            message: res.data.result.msg
          },
          { root: true }
        )
      }
    })
  },
  userFeed(context, payload) {
    return this.$axios({
      method: 'POST',
      url: endpoints.API_USER_FEED,
      data: {
        userId: context.rootState.user.current.userId
      },
      headers: {
        Authorization: 'Bearer ' + context.rootState.user.access_token
      }
    }).then(res => {
      return res.data.result.items
    })
  }
}
export default actions
