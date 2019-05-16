import Vue from 'vue'
import axios from 'axios'

export default ({ store }) => {
  // axios.create({
  //   _AXIOS_BASE_URL_: 'http://127.0.0.1:5000'
  // })

  axios.interceptors.response.use(
    function(response) {
      return response
    },
    function(error) {
      const originalRequest = error.config
      if (error.response.status === 401 && !originalRequest._retry) {
        // if the error is 401
        originalRequest._retry = true // now it can be retried

        return axios
          .post('http://localhost:5000/auth/refresh', null, {
            headers: {
              Authorization: 'Bearer ' + store.state.user.refresh_token
            }
          })
          .then(data => {
            store.dispatch('user/setTokens', {
              access_token: data.data.access_token,
              refresh_token: store.state.user.refresh_token
            })
            originalRequest.headers.Authorization =
              'Bearer ' + store.state.user.access_token // new header new token
            return Vue.axios(originalRequest) // retry the request that errored out
          })
      }
      return Promise.reject(error)
    }
  )
}

Vue.use(axios)
