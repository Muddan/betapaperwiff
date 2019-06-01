<template>
  <div class="user-profile-main">
    <v-container>
      <div class="user-profile-header">
        <div class="profile-content-wrapper">
          <div class="img-container">
            <v-avatar class="avatar-main" size="200px">
              <img class="profile-img" :src="userProfile.userImage" />
            </v-avatar>
          </div>
          <div class="profile-details">
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
                >{{ 'Follow' }}</v-btn
              >
            </div>
            <p class="profile-bio">{{ userProfile.about }}</p>

            <div class="profile-stats">
              <div class="stats">
                <p class="value">
                  {{ userStories.length }}
                </p>
                <h3 class="label">Stories</h3>
              </div>
              <div class="stats">
                <p class="value">
                  {{ userProfile.followingAuthors.length }}
                </p>
                <h3 class="label">Following</h3>
              </div>
              <div v-if="loggedInUser" class="stats">
                <p class="value">
                  {{ savedStories }}
                </p>
                <h3 class="label">Saved Stories</h3>
              </div>
            </div>
          </div>
        </div>
      </div>
      <v-layout>
        <v-flex xs3 md3 class="hidden-sm-and-down">
          <v-flex class="sidebar-section sidebar-left ">
            <user-info :image-only="false" :only-mobile="true"></user-info>
            <key-links></key-links>
          </v-flex>
        </v-flex>
        <v-flex xs12 md6>
          <v-flex class="sidebar-section sidebar-main">
            <h3 v-if="userStories.length == 0">No stories posted.</h3>
            <story-items v-else :stories="userStories"></story-items>
          </v-flex>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import StoryItems from '@/components/Blocks/StoryItems.vue'
import KeyLinks from '@/components/Blocks/KeyLinks.vue'
import UserInfo from '@/components/Blocks/UserInfo.vue'

import { endpoints } from '@/api/endpoints.js'

export default {
  components: {
    StoryItems,
    KeyLinks,
    UserInfo
  },
  computed: {
    loggedInUser() {
      return (
        this.$store.state.user.current.userName === this.$route.params.userName
      )
    },
    savedStories() {
      return this.$store.state.user.current.saveForLater.length
    }
  },
  async asyncData({ app, route, store, env, error }) {
    let userProfile = ''
    if (store.state.user.isSignedIn) {
      userProfile = await app.$axios.$post(
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
    } else {
      userProfile = await app.$axios.$post(endpoints.API_GET_AUTHOR_DETAILS, {
        userName: route.params.userName
      })
    }

    const userStories = await app.$axios({
      method: 'GET',
      url: `${endpoints.API_GET_STORIES}?userName=${route.params.userName}`
    })
    return {
      userProfile: userProfile.result,
      userStories: userStories.data.result.items
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
      if (!this.loggedInUser) {
        this.$store.commit('ui/SET_SHOW_POPUP', {
          status: true,
          component: 'SignUp'
        })
        return
      }
      alert(authorId)
      this.$store.dispatch('user/followAuthor', authorId)
    }
  }
}
</script>
<style lang="scss">
.user-profile-main {
  max-width: 1400px;
  margin: auto;
  .user-profile-header {
    .profile-content-wrapper {
      text-align: center;
      .avatar-main {
        z-index: 1;
        transform: translateZ(10px);
        border-top: 1px solid #337fb5;
        border-bottom: 1px solid #337fb5;
        img {
          padding: 10px;
        }
      }
      .profile-details {
        background: #fff;
        border-radius: 8px;
        transform: translateY(-40px);
        padding-top: 50px;
        padding-bottom: 30px;
        border-bottom: 4px solid #337fb5;
        box-shadow: 0 10px 20px 0 rgba(0, 0, 0, 0.05);
        cursor: pointer;
        @media (max-width: 768px) {
          max-width: 98%;
          margin: auto;
        }
        .profile-name {
          font-size: 26px;
        }
        .user-name {
          opacity: 0.5;
          font-weight: normal;
        }
        .action-btns,
        .profile-bio {
          margin-top: 10px;
        }
        .profile-bio {
          color: #2e2e2e;
          box-sizing: border-box;
          padding: 0 5px;
        }
        .profile-stats {
          box-sizing: border-box;
          padding-top: 10px;
          display: flex;
          justify-content: space-evenly;
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
            width: 30%;
          }
          .stats:not(:last-child) {
            border-right: 1px solid #f2f2f2;
          }
        }
      }
    }
  }
  .sidebar-left {
    margin: 30px 10px;
    .user-info {
      margin-top: 20px;
    }
  }
  .sidebar-main {
    margin: 20px 10px;
  }
  // bottom section
}
</style>
