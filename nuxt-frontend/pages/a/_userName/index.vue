<template>
  <div class="user-profile-main">
    <v-container>
      <div class="user-profile-header">
        <div class="profile-content-wrapper">
          <v-layout class="header-layout">
            <v-flex xs12 md2>
              <div class="profile-details">
                <v-avatar class="avatar-main">
                  <img
                    class="profile-img"
                    :src="userProfile.userImage"
                    @click="viewImage(userProfile.userImage)"
                  />
                </v-avatar>
                <v-subheader>
                  Member Since
                  <strong class="joined-date">{{
                    new Date(userProfile.joined.$date).toLocaleString('en-us', {
                      month: 'long',
                      day: 'numeric',
                      year: 'numeric'
                    })
                  }}</strong>
                </v-subheader>
              </div>
            </v-flex>
            <v-flex xs12 md6>
              <div class="img-container">
                <h1 class="profile-name">
                  {{ userProfile.firstName }} {{ userProfile.lastName }}
                </h1>

                <h3 class="user-name">{{ userProfile.userName }}</h3>
                <div class="action-btns">
                  <v-btn
                    v-show="loggedInUser"
                    small
                    round
                    outline
                    color="#337fb5"
                    @click="editProfile(userProfile)"
                    >{{ 'Edit Profile' }}</v-btn
                  >
                  <v-btn
                    v-show="!loggedInUser"
                    small
                    round
                    outline
                    color="#337fb5"
                    @click="followAuthor(userProfile.userId)"
                    >{{ followedAuthor ? 'Following' : 'Follow' }}</v-btn
                  >
                </div>
                <p class="profile-bio">{{ userProfile.about }}</p>
                <div class="profile-stats">
                  <div class="stats">
                    <nuxt-link
                      class="stats-link"
                      :to="{
                        path: '/a/' + userProfile.userName + '/published'
                      }"
                      ><p class="value">{{ userStories.length }}</p>
                      <h3 class="label">Stories Published</h3>
                    </nuxt-link>
                  </div>
                  <div class="stats">
                    <p class="value">
                      {{ userProfile.followingAuthors.length }}
                    </p>
                    <h3 class="label">Following Users</h3>
                  </div>
                  <div v-if="loggedInUser" class="stats">
                    <nuxt-link
                      class="stats-link"
                      :to="{
                        path: '/a/' + userProfile.userName + '/saved-stories'
                      }"
                    >
                      <p class="value">{{ savedStories }}</p>
                      <h3 class="label">Saved Stories</h3>
                    </nuxt-link>
                  </div>
                </div>
              </div>
            </v-flex>
          </v-layout>
        </div>
      </div>
      <v-layout>
        <template>
          <v-flex xs3 md3 class="hidden-sm-and-down">
            <v-flex class="sidebar-section sidebar-left">
              <user-info :image-only="false" :only-mobile="true"></user-info>
              <KeyLinks></KeyLinks>
            </v-flex>
          </v-flex>
          <v-flex xs12 md6>
            <v-flex class="sidebar-section sidebar-main">
              <h3 v-if="userStories.length == 0">No stories posted.</h3>
              <div v-else class="user-stories">
                <v-subheader>Recent Stories</v-subheader>
                <story-items :stories="userStories"></story-items>
              </div>
            </v-flex>
          </v-flex>
          <v-flex xs3 md3 class="hidden-sm-and-down">
            <v-flex class="sidebar-section sidebar-left">
              <SidebarStories>
                <span slot="title">Popular Stories on Paperwiff</span>
              </SidebarStories>
            </v-flex>
          </v-flex>
        </template>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import StoryItems from '@/components/Blocks/StoryItems.vue'
import UserInfo from '@/components/Blocks/UserInfo.vue'
import SidebarStories from '@/components/Blocks/SidebarStories/SidebarStories.vue'
import KeyLinks from '@/components/Blocks/KeyLinks.vue'
import { mapGetters } from 'vuex'
import { endpoints } from '@/api/endpoints.js'
export default {
  transition: 'slidedown',
  components: {
    StoryItems,
    UserInfo,
    SidebarStories,
    KeyLinks
  },
  data() {
    return {
      userProfile: '',
      userStories: ''
    }
  },
  computed: {
    ...mapGetters({
      isSignedIn: 'user/isSignedIn',
      followingAuthors: 'user/followingAuthors'
    }),
    loggedInUser() {
      return (
        this.$store.state.user.current.userName === this.$route.params.userName
      )
    },
    savedStories() {
      return this.$store.state.user.current.saveForLater.length
    },
    followedAuthor() {
      if (this.isSignedIn && this.followingAuthors) {
        return this.followingAuthors.includes(this.userProfile.userId)
      } else {
        return false
      }
    }
  },
  async asyncData({ app, route, store, env, error, query }) {
    let userProfile = ''
    let userStories = ''
    if (store.state.user.current.userName === route.params.userName) {
      await app.$axios
        .$post(
          endpoints.API_GET_USER_DETAILS,
          {
            userId: store.state.user.current.userId
          },
          {
            headers: {
              Authorization: 'Bearer ' + store.state.user.access_token
            }
          }
        )
        .then(res => {
          userProfile = res.result
        })
        .catch(() => {
          error({ statusCode: 404 })
        })
      await app
        .$axios({
          method: 'GET',
          url: `${endpoints.API_GET_USER_STOREIS}?userId=${
            store.state.user.current.userId
          }`
        })
        .then(res => {
          userStories = res.data.result.items
        })
        .catch(() => {
          error({ statusCode: 404 })
        })
      return {
        userProfile: userProfile,
        userStories: userStories
      }
    }
    // NORMAL USER
    else {
      await app.$axios
        .$post(endpoints.API_GET_AUTHOR_DETAILS, {
          userName: route.params.userName
        })
        .then(res => {
          userProfile = res.result.details
        })
        .catch(() => {
          error({ statusCode: 404 })
        })
      await app
        .$axios({
          method: 'GET',
          url: `${endpoints.API_GET_AUTHOR_STOREIS}?userName=${
            route.params.userName
          }`
        })
        .then(res => {
          userStories = res.data.result.items
        })
        .catch(() => {
          error({ statusCode: 404 })
        })
      return {
        userProfile: userProfile,
        userStories: userStories
      }
    }
  },
  methods: {
    getDate(date) {
      const mlist = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
      ]
      const curDate = new Date(date)
      return `${curDate.getDate()}, ${
        mlist[curDate.getMonth()]
      } ${curDate.getFullYear()}`
    },
    editProfile(profile) {
      this.$router.push({ name: 'settings', params: { userProfile: profile } })
    },
    /**
     * @param authorID
     * Follows current story Author
     */
    followAuthor(authorId) {
      if (!this.isSignedIn) {
        this.$store.commit('ui/SET_SHOW_POPUP', {
          status: true,
          component: 'SignUp'
        })
      } else {
        this.$store.dispatch('user/followAuthor', authorId)
      }
    },
    viewImage(imageUrl) {
      this.$store.commit('ui/SET_IMAGE_VIEWER', {
        status: true,
        imageViewUrl: imageUrl
      })
    }
  }
}
</script>
<style lang="scss">
.user-profile-main {
  max-width: 1400px;
  margin: auto;
  .user-profile-header {
    border-radius: 8px;
    padding: 20px;
    padding-left: 0;
    background: #fff;
    .profile-content-wrapper {
      .header-layout {
        box-sizing: border-box;
        flex-wrap: wrap;
      }
      .avatar-main {
        z-index: 1;
        border-top: 1px solid #337fb5;
        border-bottom: 1px solid #337fb5;
        height: 150px !important;
        width: 150px !important;
        img {
          padding: 10px;
        }
        @media (max-width: 768px) {
          height: 150px !important;
          width: 150px !important;
        }
      }
      .profile-details {
        height: 100%;
        align-items: center;
        justify-content: center;
        display: flex;
        background: #fff;
        border-radius: 8px 0 0 8px;
        padding-top: 15px;
        flex-direction: column;
        @media (max-width: 768px) {
          padding-top: 0;
        }
      }
      .profile-name {
        font-size: 26px;
        display: inline-flex;
        align-items: center;
        box-sizing: border-box;
        padding: 10px 0 0;
      }
      .user-name {
        opacity: 0.5;
        font-weight: normal;
        padding-bottom: 10px;
      }
      .action-btns {
        padding-bottom: 10px;
        button {
          margin-left: 0;
        }
      }
      .profile-bio {
        color: #2e2e2e;
        box-sizing: border-box;
      }
      .profile-stats {
        box-sizing: border-box;
        padding-top: 10px;
        display: flex;
        justify-content: flex-start;
        flex-wrap: wrap;
        .value {
          margin: 0;
          font-weight: bold;
          color: #337fb5;
          font-size: 18px;
        }
        .label {
          font-weight: normal;
          opacity: 0.5;
          font-size: 14px;
        }
        .stats {
          display: inline-flex;
          align-items: center;
          padding-right: 10px;
          padding-bottom: 10px;
          border-right: 1px solid #f2f2f2;
          &:not(:first-child) {
            margin-left: 10px;
          }
          &:last-child {
            border-right: none;
          }
          @media (max-width: 768px) {
            &:nth-child(3) {
              margin-left: 0;
              border-right: none;
            }
          }
          .value {
            padding-right: 10px;
          }
          .stats-link {
            display: inline-flex;
            align-items: center;
          }
        }
      }
      .img-container {
        background: #fff;
        border-radius: 0 8px 8px 0;
        padding: 20px;
      }
    }
  }
  .sidebar-left {
    margin: 30px 10px;
    margin-top: 80px;
    .user-info {
      margin-top: 20px;
    }
  }
  .sidebar-main {
    margin: 20px 10px;
    @media (max-width: 768px) {
      margin: 0;
    }
    .user-stories {
      .v-subheader {
        margin-top: 10px;
      }
      .padding-0 {
        padding: 0;
      }
    }
  }
  .joined-date {
    padding-left: 10px;
  }
  // bottom section
}
</style>
