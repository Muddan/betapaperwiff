import Vue from "vue"
import App from "./App.vue"
import router from "./router"
import store from "./store/index"
import Vuetify from "vuetify"

import VueAxios from "vue-axios"
import VueAuthenticate from "vue-authenticate"
var SocialSharing = require("vue-social-sharing")
import axios from "axios"

import "@fortawesome/fontawesome-free/css/all.css"
import "material-design-icons-iconfont/dist/material-design-icons.css"
import "vuetify/dist/vuetify.min.css"
import "@/stylus/main.styl"

Vue.config.productionTip = false

Vue.use(SocialSharing)

axios.interceptors.response.use(
  function(response) {
    return response
  },
  function(error) {
    // let originalRequest = error.config
    // if (error.response.status === 401 && !originalRequest._retry) {
    //   // if the error is 401 and hasent already been retried
    //   originalRequest._retry = true // now it can be retried
    //   return Vue.axios
    //     .post("/users/token", null)
    //     .then(data => {
    //       store.dispatch("authfalse")
    //       store.dispatch("authtruth", data.data)
    //       originalRequest.headers["Authorization"] =
    //         "Bearer " + store.state.token // new header new token
    //       return Vue.axios(originalRequest) // retry the request that errored out
    //     })
    //     .catch(error => {
    //       for (let i = 0; i < error.response.data.errors.length; i++) {
    //         if (error.response.data.errors[i] === "TOKEN-EXPIRED") {
    //           auth.logout()
    //           return
    //         }
    //       }
    //     })
    // }
    // if (error.response.status === 404 && !originalRequest._retry) {
    //   originalRequest._retry = true
    //   window.location.href = "/"
    //   return
    // }
    return Promise.reject(error)
  }
)

Vue.use(VueAxios, axios)

Vue.use(VueAuthenticate, {
  tokenName: "access_token",
  baseUrl: `${process.env.VUE_APP_BASE_URL}:5000`, // Your API domain

  providers: {
    google: {
      clientId:
        "430441876577-0opc3qqi2ieoev8hnfqr9ftirc3oamuq.apps.googleusercontent.com",
      redirectUri: `${process.env.VUE_APP_BASE_URL}` //  client app URL
    },
    twitter: {
      redirectUri: `${process.env.VUE_APP_BASE_URL}`,
      popupOptions: { width: 495, height: 645 }
    }
  }
})

Vue.use(Vuetify, {
  iconfont: "fa"
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app")
