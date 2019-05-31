export default function({ $axios, redirect, store }) {
  $axios.onRequest(config => {
    // eslint-disable-next-line no-console
    console.log('Making request to ' + config.url)
  })

  $axios.onError(error => {
    const code = parseInt(error.response && error.response.status)
    if (code === 401) {
      const originalRequest = error.config
      if (error.response.status === 401 && !originalRequest._retry) {
        // if the error is 401
        originalRequest._retry = true // now it can be retried

        return $axios
          .$post('localhost:5000/api/auth/refresh', null, {
            headers: {
              Authorization: 'Bearer ' + store.state.user.refresh_token
            }
          })
          .then(data => {
            store.dispatch('user/setTokens', {
              access_token: data.access_token,
              refresh_token: store.state.user.refresh_token
            })
            originalRequest.headers.Authorization =
              'Bearer ' + store.state.user.access_token // new header new token
            return $axios(originalRequest) // retry the request that errored out
          })
      }
      return Promise.reject(error)
    }
  })
}
