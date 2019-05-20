import Vue from 'vue'
import Cloudinary from 'cloudinary-vue'

Vue.use(Cloudinary)
// ..or provide some global cloudinary service configuration..
Vue.use(Cloudinary, {
  configuration: { cloudName: 'wokong' }
  //             ^ cloudinary configuration options
})
