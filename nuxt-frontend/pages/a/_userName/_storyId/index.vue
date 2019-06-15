<template>
  <div class="story-details">
    <no-ssr>
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
              <v-flex md1></v-flex>
              <v-flex md1 xs12 class="hidden-sm-and-down">
                <div class="sticky-main">
                  <share-story :url="storyUrl"></share-story>
                  <div class="action-btns">
                    <v-btn
                      flat
                      icon
                      :class="{ likedStory: savedStory }"
                      color="grey darken-4"
                      @click="saveStory(story.storyId)"
                    >
                      <v-icon>
                        {{ savedStory ? 'bookmarks' : 'bookmark_border' }}
                      </v-icon>
                    </v-btn>
                    <div class="like-btn">
                      <v-btn
                        flat
                        icon
                        color="grey darken-4"
                        :class="{ likedStory: likedStatus }"
                        @click="likeStory(story.storyId)"
                      >
                        <v-icon>favorite</v-icon>
                      </v-btn>
                      <!-- <span class="like-counter">{{ likeCount }}</span> -->
                    </div>
                  </div>
                </div>
              </v-flex>
              <v-flex content-layout md8 xs12>
                <div class="story-poster">
                  <img class="poster" :src="story.headerImage" alt />
                </div>
                <div class="content-section">
                  <div class="title-section">
                    <header>
                      <v-layout class="mini-profile" align-center>
                        <v-flex xs8 class="details-flex">
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
                              {{
                                new Date(story.datePublished).toLocaleString(
                                  'en-us',
                                  {
                                    month: 'long',
                                    day: 'numeric'
                                  }
                                )
                              }}
                              <v-icon class="dot-icon" size="8px"
                                >fas fa-star</v-icon
                              >
                              <span class="ago-time">
                                {{
                                  getPublishedDate(
                                    new Date(story.datePublished)
                                  )
                                }}
                              </span>
                              <span>ago</span>
                            </span>
                          </div>
                        </v-flex>
                        <v-flex xs4>
                          <div class="reading">
                            <v-btn small flat icon color="#9b9b9b">
                              <v-icon small>fas fa-book-reader</v-icon>
                            </v-btn>
                            <span class="value">
                              {{
                                Math.floor(
                                  story.content.split(' ').length / 160
                                )
                                  ? Math.floor(
                                      story.content.split(' ').length / 160
                                    )
                                  : 'less than a'
                              }}
                              min read
                            </span>
                          </div>
                        </v-flex>
                      </v-layout>
                      <h1 class="main-title">{{ story.storyTitle }}</h1>
                      <span class="summary">
                        <p>{{ story.summary }}</p>
                      </span>
                      <div class="chip-container">
                        <span
                          v-for="(tag, tagIndex) in story.tags"
                          :key="tagIndex"
                          class="chip"
                          ># {{ tag }}</span
                        >
                      </div>
                    </header>
                  </div>
                  <div class="story-content" v-html="story.content"></div>
                  <div class="footer-share">
                    <v-subheader>Share</v-subheader>
                    <share-story :url="storyUrl"></share-story>
                  </div>
                  <div class="footer-author">
                    <author-info :author="user">
                      <v-btn
                        outline
                        color="#5199c3"
                        @click="followAuthor(story.userId)"
                      >
                        <v-icon left>{{
                          followedAuthor ? 'group' : 'group_add'
                        }}</v-icon>
                        {{ followedAuthor ? 'Following' : 'Follow' }}
                      </v-btn>
                    </author-info>
                  </div>
                </div>
              </v-flex>
            </v-layout>
            <v-flex md12>
              <!-- <SidebarStories></SidebarStories> -->
            </v-flex>
            <!-- <comments-listing></comments-listing> -->
          </div>
        </div>
        <div class="bottom-nav-mobile hidden-md-and-up">
          <v-btn
            flat
            icon
            color="grey darken-4"
            @click="saveStory(story.storyId)"
          >
            <v-icon>{{ savedStory ? 'bookmarks' : 'bookmark_border' }}</v-icon>
          </v-btn>
          <v-btn icon flat value="nearby">
            <v-icon>comment</v-icon>
          </v-btn>
          <v-btn
            flat
            icon
            color="grey darken-4"
            :class="{ likedStory: likedStatus }"
            @click="likeStory(story.storyId)"
          >
            <v-icon>favorite</v-icon>
          </v-btn>
        </div>
      </v-container>
    </no-ssr>
  </div>
</template>

<script>
import AuthorInfo from '@/components/Blocks/AuthorInfo.vue'
import ShareStory from '@/components/Blocks/ShareStory.vue'
// import SidebarStories from '@/components/Blocks/SidebarStories.vue'

// import commentsListing from '@/components/Blocks/comments/commentsListing.vue'
import { SocialFeatures } from '@/mixins/SocialFeatures.js'

import { endpoints } from '@/api/endpoints.js'
import { getDate } from '@/helpers/dateHelper.js'
import { mapGetters } from 'vuex'
export default {
  transition: 'slidedown',
  head() {
    return {
      title: this.story.storyTitle
    }
  },
  components: {
    ShareStory,
    AuthorInfo
    // SidebarStories,
    // commentsListing
  },
  mixins: [SocialFeatures],
  data() {
    return {
      fab: false,
      likeCount: 0,
      bottomNav: '',
      storyUrl: ''
    }
  },

  computed: {
    ...mapGetters({
      isSignedIn: 'user/isSignedIn',
      likedStories: 'user/likedStories',
      followingAuthors: 'user/followingAuthors',
      savedStories: 'user/savedStories'
    }),
    likedStatus() {
      if (this.isSignedIn) {
        return this.likedStories.includes(this.story.storyId)
      } else {
        return false
      }
    },
    followedAuthor() {
      if (this.isSignedIn) {
        return this.followingAuthors.includes(this.story.userId)
      } else {
        return false
      }
    },
    savedStory() {
      if (this.isSignedIn) {
        return this.savedStories.includes(this.story.storyId)
      } else {
        return false
      }
    }
  },

  async asyncData({ app, store, route, redirect, error, context }) {
    let storyDetails
    let userDetails
    if (process.browser && !store.state.user.isSignedIn) {
      if (window.localStorage.getItem('stories-viewed')) {
        let count =
          JSON.parse(window.localStorage.getItem('stories-viewed')) || {}
        if (count > 5) {
          store.commit('ui/SET_SHOW_POPUP', {
            status: true,
            component: 'SignUp'
          })
        }
        count++
        window.localStorage.setItem('stories-viewed', count)
      } else {
        window.localStorage.setItem('stories-viewed', 1)
      }
    }

    await app.$axios
      .$post(endpoints.API_GET_STORY_DETAILS, {
        storyId: route.params.storyId
      })
      .then(res => {
        if (res.result.status === 200) {
          storyDetails = res.result.item
        }
      })
      .catch(() => {
        error({ statusCode: 404 })
      })

    await app.$axios
      .$post(endpoints.API_GET_AUTHOR_DETAILS, {
        userName: route.params.userName
      })
      .then(res => {
        if (res.result.status === 200) {
          userDetails = res.result.details
        }
      })
      .catch(() => {
        error({ statusCode: 404 })
      })

    return {
      story: storyDetails,
      user: userDetails
    }
  },
  mounted() {
    this.likeCount = this.story.likes
    this.liked = this.likedStatus
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

<style lang="scss">
.story-details {
  max-width: 1400px;
  margin: auto;
  padding-top: 20px;
  @media (max-width: 767px) {
    padding-top: 10px;
  }
  .sticky-main {
    overflow: hidden;
    position: sticky;
    top: 150px;
    text-align: center;
    .action-btns {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: center;
      border-top: 1px solid #d7d7d7;
      width: 60%;
      padding-top: 20px;
    }
  }
  .content-layout {
    background: #fff;
    box-shadow: 0 10px 20px 0 rgba(0, 0, 0, 0.05);
    border-radius: 8px;
  }
  .story-poster {
    padding: 0 25px;
    box-sizing: border-box;
    max-height: 500px;
    height: 500px;
    transform: translateY(-25px);
    img {
      height: 500px;
      object-fit: cover;
    }
    @media (max-width: 768px) {
      padding: 15px 15px 0px 15px;
      max-height: 200px;
      height: 200px;
    }
    .poster {
      width: 100%;
      border-radius: 8px;
      display: inherit;
      height: 100%;
    }
  }
  .content-section {
    padding: 20px 10px 30px 10px;
    box-sizing: border-box;
    margin: 0 20px;
    margin-top: -40px;

    @media (max-width: 768px) {
      margin: 0 0;
      background: #fff;
      margin-top: -20px;
      padding: 0px 20px 20px;
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
        padding-top: 0;
      }
      .user-profile {
        text-decoration: none;
        color: #2e2e2e;
        font-size: 16px;
      }
      .main-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 47px;
        text-align: left;
        line-height: 1.5;
        font-weight: normal;
        @media (max-width: 768px) {
          font-size: 24px;
        }
      }
      .mini-profile {
        margin: 10px 0;
        .details-flex {
          display: flex;
          position: relative;
          .profile-img {
            border-top: 1px solid #337fb5;
            border-bottom: 1px solid #337fb5;
            img {
              padding: 5px;
            }
          }
          .reading {
            position: absolute;
            right: 0;
            top: 5px;
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
        .reading {
          display: flex;
          align-items: center;
        }
      }
      .date {
        font-size: 12px;
        color: #b1b1b1;
        display: flex;
        align-items: center;
        .dot-icon {
          padding: 0 10px;
          color: #b1b1b1;
        }
        .ago-time {
          padding-right: 5px;
        }
      }
    }
    .summary {
      p {
        margin: 10px 0;
        line-height: 1.5;
        padding: 0;
        font-size: 18px;
        opacity: 0.6;
        letter-spacing: 0.5px;
      }
    }
    .chip-container {
      padding: 5px 0;
      border-bottom: 1px solid #f2f2f2;
      padding-bottom: 20px;
      .chip {
        border-radius: 4px;
        padding: 5px;
        background: #f7fafc;
        color: #337fb5;
        margin-right: 5px;
        font-size: 14px;
        text-transform: capitalize;
        cursor: pointer;
        @media (max-width: 768px) {
          font-size: 12px;
        }
        &:hover {
          background: #fafafa;
        }
      }
      .read-time {
        float: right;
        font-size: 12px;
        color: #b1b1b1;
      }
    }
    .story-content {
      font-size: 18px;
      max-width: 90%;
      margin: auto;
      padding-bottom: 20px;
      @media (max-width: 768px) {
        max-width: 100%;
      }
      line-height: 2;
    }
    .footer-share {
      max-width: 90%;
      margin: auto;
      box-sizing: border-box;
      padding: 20px 0;
      display: flex;
      align-items: center;
      justify-content: flex-end;
      .links-main {
        i {
          color: #3d3d3d;
          &:hover {
            color: #1d1d1d;
          }
        }
      }
    }
    .footer-author {
      border-top: 1px solid #f2f2f2;
    }
  }
  .likedStory {
    &:hover {
      background: #deedf8;
    }
    .v-icon {
      color: #d50122;
    }
  }
  .savedStory {
    &:hover {
      background: #deedf8;
    }
    .v-icon {
      color: #141414;
    }
  }
  .bottom-nav-mobile {
    width: 100%;
    background: #fff;
    position: fixed;
    bottom: 0;
    left: 0;
    display: flex;
    justify-content: space-between;
    box-shadow: 0 3px 14px 2px rgba(0, 0, 0, 0.12);
    box-sizing: border-box;
    padding: 0 30px;
  }
}
</style>
