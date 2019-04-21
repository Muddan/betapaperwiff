import Vue from "vue"
import Router from "vue-router"
import Home from "./views/Home.vue"
import Write from "./views/Write.vue"

Vue.use(Router)

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/tags/:tagName",
      name: "tags",
      component: () =>
        import(/* webpackChunkName: "about" */ "./views/TagView.vue")
    },
    {
      path: "/a/:userName/:storyId?",
      name: "userprofile",
      component: () =>
        import(/* webpackChunkName: "about" */ "./views/UserProfile.vue")
    },
    {
      path: "/join",
      name: "join",
      component: () =>
        import(/* webpackChunkName: "about" */ "./views/Login.vue")
    },
    {
      path: "/write",
      name: "write",
      component: Write
    }
  ]
})
