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
              </div>
            </v-flex>
            <v-flex md8 xs12>
              <div class="story-poster">
                <img
                  class="poster"
                  src="https://res.cloudinary.com/practicaldev/image/fetch/s--yUyi4zBB--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://thepracticaldev.s3.amazonaws.com/i/pf9l84zqr2hpqg2nl6yi.jpg"
                  alt
                />
              </div>
              <div class="content-section">
                <div class="title-section">
                  <span class="date">
                    {{ getPublishedDate(story.datePublished) }}
                  </span>
                  <header>
                    <h1 class="main-title">{{ story.storyTitle }}</h1>
                    <v-layout class="mini-profile" align-center>
                      <v-flex xs12>
                        <v-avatar
                          class="profile-img"
                          size="30px"
                          :color="randomColor()"
                        >
                          <span class="white--text avatar-name">{{
                            story.userName[1]
                          }}</span>
                        </v-avatar>
                        <nuxt-link
                          class="user-profile"
                          :to="{
                            path: '/a/' + story.userName
                          }"
                        >
                          <span class="username">{{ story.userName }}</span>
                        </nuxt-link>
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
              </div>
            </v-flex>
            <v-flex
              class="sidebar-section sidebar-left hidden-sm-and-down"
              md3
              xs12
            >
              <key-links></key-links>
            </v-flex>
          </v-layout>
        </div>
      </div>
      <v-speed-dial
        v-model="fab"
        right
        bottom
        color="teal"
        flat
        :fixed="true"
        direction="top"
        transition="slide-y-reverse-transition"
        class="hidden-md-and-up"
      >
        <template v-slot:activator>
          <v-btn v-model="fab" color="white" light fab>
            <v-icon>share</v-icon>
            <v-icon>close</v-icon>
          </v-btn>
        </template>
        <share-story :url="storyUrl"></share-story>
      </v-speed-dial>
    </v-container>
  </div>
</template>

<script>
import KeyLinks from '@/components/Blocks/KeyLinks.vue'
// import AuthorInfo from '@/components/Blocks/AuthorInfo.vue'
import ShareStory from '@/components/Blocks/ShareStory.vue'

import { endpoints } from '@/api/endpoints.js'
import { getDate } from '@/helpers/dateHelper.js'

export default {
  components: {
    KeyLinks,
    ShareStory
  },
  data() {
    return {
      fab: false
    }
  },
  computed: {},
  asyncData({ app, store, route }) {
    return app.$axios
      .$post(endpoints.API_GET_STORY_DETAILS, {
        storyId: route.params.storyId
      })
      .then(res => {
        return {
          story: res.details[0],
          storyUrl: `${process.env.baseUrl}${route.path}`
        }
      })
  },
  methods: {
    getPublishedDate(date) {
      return getDate(date)
    },
    randomColor() {
      return '#' + Math.floor(Math.random() * 16777215).toString(16)
    }
  }
}
</script>

<style lang="scss" scoped>
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
    @media (max-width: 768px) {
      padding: 0;
    }
    .poster {
      width: 100%;
      border-radius: 8px;
      display: inherit;
    }
  }
  .content-section {
    padding: 35px 30px 30px;
    box-sizing: border-box;
    border-radius: 8px;
    margin: 0 20px;
    background: #fff;
    margin-top: -40px;
    @media (max-width: 768px) {
      margin: 0 10px;
      background: #fff;
      margin-top: -20px;
      padding: 25px 20px 20px;
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
        .avatar-name {
          text-transform: uppercase;
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
      &::after {
        content: '';
        width: 80%;
        margin: auto;
        background: #2e2e2e;
        height: 1px;
        display: block;
      }
      line-height: 2;
    }
  }
}
</style>
