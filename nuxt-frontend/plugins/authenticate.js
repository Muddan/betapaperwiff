import Vue from 'vue'
import VueAxios from 'vue-axios'
import VueAuthenticate from 'vue-authenticate'
import axios from 'axios'

Vue.use(VueAxios, axios)
Vue.use(VueAuthenticate, {
  baseUrl: 'http://localhost:5000', // Your API domain

  providers: {
    google: {
      clientId:
        '430441876577-0opc3qqi2ieoev8hnfqr9ftirc3oamuq.apps.googleusercontent.com',
      redirectUri: 'http://localhost:3000' // Your client app URL
    }
  }
})
