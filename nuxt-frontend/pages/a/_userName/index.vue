<template>
  <div class="user-profile-main">
    <v-container>
      <div class="user-profile-header">
        <v-layout v-if="userProfile" fluid row>
          <v-flex class="img-container" xs4 md2>
            <img class="profile-img" :src="userProfile.userImage" alt />
          </v-flex>

          <v-flex xs8 class="profile-details">
            <v-layout fluid align-center justify-center fill-height>
              <v-flex xs9 md10>
                <h1 class="profile-name">
                  {{ userProfile.firstName }} {{ userProfile.lastName }}
                </h1>
                <h3 class="user-name">{{ userProfile.userName }}</h3>
                <v-btn
                  v-if="loggedInUser"
                  outline
                  color="#6e6e6e"
                  @click="editProfile(userProfile)"
                  >Edit Profile</v-btn
                >
                <v-btn v-else outline color="#6e6e6e">Follow</v-btn>
                <p class="profile-bio">{{ userProfile.about }}</p>
              </v-flex>
            </v-layout>
          </v-flex>
        </v-layout>
        <v-layout class="joined-details">
          <v-flex xs4>
            <!-- <h3 class="label">Joined</h3>
            <p class="value">
              {{ getDate(userProfile.joined) }}
            </p>
          </v-flex> -->
            <v-flex row xs4>
              <h3 class="label">Stories published</h3>
              <p class="value">
                {{ userProfile.userArticles.length }}
              </p>
            </v-flex>
            <v-flex row xs4>
              <h3 class="label">Following</h3>
              <p class="value">
                {{ userProfile.followingAuthors.length }}
              </p>
            </v-flex>
            <h3 class="label">Location</h3>
            <p class="value">
              {{ userProfile.location }}
            </p>
          </v-flex>
        </v-layout>
      </div>
      <v-layout>
        <v-flex xs3 md3 class="hidden-sm-and-down">
          <v-flex class="sidebar-section sidebar-left ">
            <key-links></key-links>
          </v-flex>
        </v-flex>
        <v-flex xs12 md9>
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

import { endpoints } from '@/api/endpoints.js'

export default {
  components: {
    StoryItems,
    KeyLinks
  },
  computed: {
    loggedInUser() {
      return (
        this.$store.state.user.current.userName === this.$route.params.userName
      )
    }
  },
  async asyncData({ app, route, store, env, error }) {
    let userProfile = ''
    if (store.state.user.isSignedIn) {
      userProfile = await app.$axios.$post(endpoints.API_GET_USER_DETAILS, {
        userId: store.state.user.current.userId
      })
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
    }
  }
}
</script>
<style lang="scss">
.user-profile-main {
  max-width: 1400px;
  margin: auto;
  .user-profile-header {
    border: 1px solid #3e3e3e;
    border-radius: 4px;
    border-bottom: 4px solid #3e3e3e;
    box-sizing: border-box;
    background: #fff;
    padding: 20px;
    @media (max-width: 768px) {
      padding: 10px 0;
    }
    .joined-details {
      padding: 0 15px;
      .value {
        color: #6e6e6e;
      }
    }
    .img-container {
      display: flex;
      justify-content: center;
      align-items: center;
      @media (max-width: 768px) {
        align-items: flex-start;
      }
      .profile-img {
        width: 150px;
        height: 150px;
        object-fit: cover;
        border-radius: 50%;
        padding: 10px;
        box-sizing: border-box;
        @media (max-width: 768px) {
          width: 100px;
          height: 100px;
        }
      }
    }

    .profile-details {
      .profile-name {
        font-size: 50px;
        font-weight: bold;
        text-decoration: underline;
        padding: 10px;
        box-sizing: border-box;
        @media (max-width: 768px) {
          font-size: 24px;
        }
      }
      .user-name {
        color: #6e6e6e;
        padding: 0 10px;
        box-sizing: border-box;
      }
      .profile-bio {
        color: #6e6e6e;
        max-width: 80%;
        padding: 10px;
        box-sizing: border-box;
        font-size: 16px;
        font-style: italic;
        font-weight: lighter;
        @media (max-width: 768px) {
          max-width: 100%;
        }
      }
    }
  }

  .sidebar-left {
    margin: 30px 10px;
  }
  .sidebar-main {
    margin: 20px 10px;
  }
  // bottom section
}
</style>
