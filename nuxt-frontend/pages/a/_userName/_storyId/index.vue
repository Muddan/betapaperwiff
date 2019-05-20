<template>
  <div class="story-details">
    <v-container>
      <div class="story-loader">
        <v-progress-circular
          v-if="!story"
          indeterminate
          color="#f45b69"
        ></v-progress-circular>
      </div>
      <div v-if="story" class="story-details">
        <div class="main-content">
          <v-layout>
            <v-flex md1 xs12 class="hidden-sm-and-down">
              <div class="sticky-main">
                <share-story :url="storyUrl"></share-story>
                <v-btn
                  :disabled="disableLike"
                  flat
                  icon
                  color="pink"
                  @click="likeStory(story)"
                >
                  <v-icon>favorite</v-icon>
                </v-btn>
                <span>{{ likeCount }}</span>

                <!-- <v-btn flat icon>
                  <v-icon>bookmarks</v-icon>
                </v-btn> -->
              </div>
            </v-flex>
            <v-flex md8 xs12>
              <div class="story-poster">
                <img class="poster" :src="story.headerImage" alt />
              </div>
              <div class="content-section">
                <div class="title-section">
                  <header>
                    <h1 class="main-title">{{ story.storyTitle }}</h1>
                    <v-layout class="mini-profile" align-center>
                      <v-flex xs12 class="details-flex">
                        <v-avatar class="profile-img" size="55px">
                          <img :src="user.userImage" />
                        </v-avatar>
                        <div class="details">
                          <nuxt-link
                            class="user-profile"
                            :to="{
                              path: '/a/' + story.userName
                            }"
                          >
                            <span class="username">{{ user.firstName }}</span>
                          </nuxt-link>
                          <span class="date">
                            {{ getPublishedDate(story.datePublished) }}
                          </span>
                        </div>
                      </v-flex>
                    </v-layout>

                    <div class="chip-container">
                      <span
                        v-for="(tag, tagIndex) in story.tags"
                        :key="tagIndex"
                        class="chip"
                        >#{{ tag }}</span
                      >
                    </div>
                  </header>
                </div>
                <div class="story-content" v-html="story.content"></div>
                <author-info :author="user"></author-info>
              </div>
            </v-flex>
          </v-layout>
        </div>
      </div>
    </v-container>
  </div>
</template>

<script>
import AuthorInfo from '@/components/Blocks/AuthorInfo.vue'
import ShareStory from '@/components/Blocks/ShareStory.vue'

import { endpoints } from '@/api/endpoints.js'
import { getDate } from '@/helpers/dateHelper.js'

export default {
  transition: 'slidedown',
  components: {
    ShareStory,
    AuthorInfo
  },
  data() {
    return {
      fab: false,
      likeCount: 0,
      disableLike: false
    }
  },
  async asyncData({ app, store, route }) {
    const storyDetails = await app.$axios.$post(
      endpoints.API_GET_STORY_DETAILS,
      {
        storyId: route.params.storyId
      }
    )
    const userProfile = await app.$axios.$post(endpoints.API_GET_USER_DETAILS, {
      userName: route.params.userName
    })
    return {
      story: storyDetails.result.item,
      storyUrl: `${process.env.baseUrl}${route.path}`,
      user: userProfile.result
    }
  },
  beforeMount() {
    this.likeCount = this.story.likes
  },
  methods: {
    getPublishedDate(date) {
      return getDate(date)
    },
    randomColor() {
      return '#' + Math.floor(Math.random() * 16777215).toString(16)
    },
    likeStory(story) {
      this.likeCount++
      this.$store.dispatch('stories/like', story.storyId)
    }
  }
}
</script>
<style lang="scss">
.preloader {
  position: absolute;
  top: 0;
  left: 0;
  background-color: #000;
  opacity: 0.8;
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
  overflow: hidden;
}
.loader {
  height: 4rem;
  width: 4rem;
  border-bottom: 5px solid #66bbf8;
  border-left: 5px solid #337fb5;
  border-right-color: transparent;
  border-top-color: transparent;
  border-radius: 50%;
  animation: rotate 0.5s infinite;
}
@keyframes rotate {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(359deg);
  }
}
</style>

<style lang="scss">
.story-details {
  max-width: 1400px;
  margin: auto;
  .sticky-main {
    overflow: hidden;
    position: sticky;
    top: 100px;
    text-align: center;
  }
  .story-poster {
    padding: 0 30px;
    box-sizing: border-box;
    max-height: 500px;
    height: 500px;
    img {
      height: 500px;
      object-fit: cover;
    }
    @media (max-width: 768px) {
      padding: 0;
      max-height: 200px;
      height: 200px;
      margin: 0 10px;
    }
    .poster {
      width: 100%;
      border-radius: 8px;
      display: inherit;
      height: 100%;
    }
  }
  .content-section {
    padding: 35px 10px 30px;
    box-sizing: border-box;
    border-radius: 8px;
    margin: 0 20px;
    background: #fff;
    margin-top: -40px;
    @media (max-width: 768px) {
      margin: 0 0;
      background: #fff;
      margin-top: -20px;
      padding: 25px 20px 20px;
    }
    .links-main {
      text-align: center;
      ul {
        li {
          display: inline-block;
        }
      }
    }
    .title-section {
      padding: 20px 0;
      max-width: 90%;
      margin: auto;
      @media (max-width: 768px) {
        max-width: 100%;
      }
      .user-profile {
        text-decoration: none;
        color: #2e2e2e;
        font-size: 16px;
      }
      .main-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 57px;
        text-align: left;
        line-height: 1.5;
        @media (max-width: 768px) {
          font-size: 24px;
        }
      }
      .mini-profile {
        margin: 10px 0;
        .details-flex {
          display: flex;
          .profile-img {
            border-top: 1px solid #337fb5;
            border-bottom: 1px solid #337fb5;
            img {
              padding: 5px;
            }
          }
        }
        .avatar-name {
          text-transform: uppercase;
        }
        .details {
          display: flex;
          flex-direction: column;
          box-sizing: border-box;
          padding: 0 10px;
        }
      }
      .date {
        font-size: 12px;
        color: #b1b1b1;
      }
    }
    .chip-container {
      padding: 5px;
      .chip {
        border-radius: 4px;
        padding: 5px;
        background: #2e2e2e;
        color: #f2f2f2;
        margin-right: 5px;
        font-size: 12px;
        @media (max-width: 768px) {
          font-size: 10px;
        }
        &:hover {
          text-decoration: underline;
          cursor: pointer;
        }
      }
    }
    .story-content {
      font-size: 16px;
      max-width: 90%;
      margin: auto;
      padding-bottom: 20px;
      @media (max-width: 768px) {
        max-width: 100%;
      }
      line-height: 2;
    }
  }
}
</style>
