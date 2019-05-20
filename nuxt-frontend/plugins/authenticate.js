import Vue from 'vue'
import VueAxios from 'vue-axios'
import VueAuthenticate from 'vue-authenticate'
import axios from 'axios'

Vue.use(VueAxios, axios)
Vue.use(VueAuthenticate, {
  baseUrl: 'http://172.31.24.211:5000', // Your API domain

  providers: {
    google: {
      clientId:
        '430441876577-0opc3qqi2ieoev8hnfqr9ftirc3oamuq.apps.googleusercontent.com',
      redirectUri:
        'http://ec2-52-221-226-186.ap-southeast-1.compute.amazonaws.com' // Your client app URL
    }
  }
})
