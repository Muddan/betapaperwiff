<template>
  <v-container class="padding-0" fluid>
    <no-ssr>
      <v-layout column wrap>
        <!-- Story items listing -->
        <v-card
          v-for="(story, index) in stories"
          :key="index"
          v-ripple="{ class: `blue-grey--text` }"
          flat
          class="story-items-main"
        >
          <div class="story-items-content">
            <div class="item-header">
              <div class="item-subheader">
                <div class="flex items-left">
                  <v-avatar class="avatar-main" size="50px">
                    <img :src="story.userImage" />
                  </v-avatar>
                  <v-subheader class="username-header">
                    <nuxt-link
                      class="user-link"
                      :to="{
                        path: '/a/' + story.userName
                      }"
                      no-prefetch
                    >
                      <span class="username">
                        {{ story.firstName }}
                      </span>
                    </nuxt-link>

                    <span class="published-date">
                      <span class="full-date">
                        {{
                          new Date(story.datePublished).toLocaleString(
                            'en-us',
                            {
                              month: 'long',
                              day: 'numeric'
                            }
                          )
                        }}
                      </span>
                      <span>&#9733;</span>
                      <span class="relative-date">
                        {{ getPublishedDate(story.datePublished) }}
                        <span>ago</span>
                      </span>
                    </span>
                  </v-subheader>
                  <div class="save-later">
                    <v-btn
                      flat
                      icon
                      color="grey darken-5"
                      @click="saveStory(story.storyId)"
                    >
                      <v-icon>{{
                        savedStory(story.storyId)
                          ? 'bookmarks'
                          : 'bookmark_border'
                      }}</v-icon>
                    </v-btn>
                  </div>
                </div>
              </div>
              <div class="chip-container">
                <nuxt-link
                  v-for="(tag, tagIndex) in story.tags"
                  :key="tagIndex"
                  :to="{
                    path: '/tags/' + tag
                  }"
                >
                  <span class="chip"> #{{ tag }}</span>
                </nuxt-link>
              </div>
              <nuxt-link
                :to="{
                  path: '/a/' + story.userName + '/' + story.storyId
                }"
              >
                <div v-if="story.headerImage" class="post-header">
                  <img class="header-img" :src="story.headerImage" />
                </div>
              </nuxt-link>

              <nuxt-link
                class="story-title"
                :to="{
                  path: '/a/' + story.userName + '/' + story.storyId
                }"
              >
                <h3 class="story-title">
                  {{ story.storyTitle }}
                </h3>
              </nuxt-link>
              <p class="story-desc" v-html="story.summary"></p>
            </div>
            <div class="item-footer">
              <div class="actions-main">
                <v-layout>
                  <v-flex xs6>
                    <span class="read-time">
                      {{
                        Math.floor(story.content.split(' ').length / 160)
                          ? Math.floor(story.content.split(' ').length / 160)
                          : 'less than a'
                      }}
                      min read
                    </span>
                  </v-flex>
                  <v-flex info-icons xs6>
                    <v-tooltip top>
                      <template v-slot:activator="{ on }">
                        <div class="label">
                          <v-btn
                            small
                            flat
                            icon
                            color="grey darken-5"
                            v-on="on"
                          >
                            <v-icon small>favorite</v-icon>
                          </v-btn>
                          <span class="value">{{ story.likes }}</span>
                        </div>
                      </template>
                      <span>likes</span>
                    </v-tooltip>
                    <v-tooltip top>
                      <template v-slot:activator="{ on }">
                        <div class="label">
                          <v-btn small flat icon color="#9b9b9b" v-on="on">
                            <v-icon small>fas fa-eye</v-icon>
                          </v-btn>
                          <span class="value">{{ story.views }}</span>
                        </div>
                      </template>
                      <span>Views</span>
                    </v-tooltip>
                  </v-flex>
                </v-layout>
              </div>
            </div>
          </div>
        </v-card>
        <!-- Infinite loading component -->
      </v-layout>
    </no-ssr>
  </v-container>
</template>

<script>
import { mapGetters } from 'vuex'
import { getDate } from '@/helpers/dateHelper.js'
import { SocialFeatures } from '@/mixins/SocialFeatures.js'
export default {
  name: 'StoryItems',
  mixins: [SocialFeatures],
  props: {
    stories: {
      type: Array,
      default: null
    }
  },
  data() {
    return {
      loader: null,
      loading: false
    }
  },
  computed: {
    ...mapGetters({
      filteredStories: 'stories/filteredStories',
      allStories: 'stories/allStories',
      isSignedIn: 'user/isSignedIn',
      likedStories: 'user/likedStories',
      followingAuthors: 'user/followingAuthors',
      savedStories: 'user/savedStories'
    }),
    getCurrentUserFeed() {
      if (this.filteredStories.length > 0) {
        return this.filteredStories
      } else {
        return this.allStories
      }
    }
  },

  methods: {
    getPublishedDate(date) {
      return getDate(new Date(date))
    },
    savedStory(storyId) {
      if (this.isSignedIn && this.savedStories) {
        return this.savedStories.includes(storyId)
      } else {
        return false
      }
    }
  }
}
</script>
<style lang="scss">
a {
  text-decoration: none;
  color: inherit;
}
</style>

<style lang="scss" scoped>
.padding-0 {
  padding: inherit 0;
  padding-top: 0;
}
.story-items-main {
  border-radius: 8px;
  margin: 10px 0;
  background: #fff;
  padding: 10px 15px 0 15px;
  box-sizing: border-box;
  border-bottom: 4px solid #5199c3 !important;
  box-shadow: 0 10px 20px 0 rgba(0, 0, 0, 0.05);
  @media (max-width: 1024px) {
    padding-bottom: 0;
  }
  .published-date {
    color: #b1b1b1;
    font-size: 12px;
    padding: 0 5px;
    @media (max-width: 768px) {
      font-size: 12px;
    }
    .full-date {
      padding-right: 5px;
    }
    .relative-date {
      padding-left: 5px;
      > span {
        padding-left: 5px;
      }
    }
  }
  .item-header {
    .post-header {
      box-sizing: border-box;
      padding-top: 10px;
      .header-img {
        width: 100%;
        height: 250px;
        object-fit: cover;
        border-radius: 8px;
        @media (max-width: 768px) {
          height: 150px;
        }
      }
    }
    .story-title {
      font-family: 'Cormorant Garamond', serif;
      font-style: normal;
      font-weight: normal;
      font-size: 26px;
      color: #161616;
      text-decoration: none;
      padding-top: 10px;
      @media (max-width: 1024px) {
        font-size: 22px;
      }
    }
    .story-desc {
      color: #161616;
      opacity: 0.5;
      max-height: 50px;
      overflow: hidden;
      font-size: 16px;
      @media (max-width: 1024px) {
        font-size: 14px;
      }
    }
    .chip-container {
      padding: 5px;
      > a {
        text-decoration: none;
      }
      .chip {
        border-radius: 4px;
        padding: 0 2px;
        color: #9b9b9b;
        margin-right: 5px;
        font-size: 14px;
        &:hover {
          text-decoration: underline;
          cursor: pointer;
        }
      }
    }
    .item-subheader {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      padding: 5px 0;
      .items-left {
        display: flex;
        align-items: center;
        position: relative;
        .save-later {
          position: absolute;
          right: 0;
        }
      }
      .avatar-main {
        border-top: 1px solid #337fb5;
        border-bottom: 1px solid #337fb5;
        img {
          padding: 5px;
        }
      }
      .avatar-name {
        text-transform: uppercase;
      }
      .username-header {
        display: inline-block;
        padding: 0 10px;
        .user-link {
          text-decoration: none;
          display: inherit;
          color: #2e2e2e;
          width: 100%;
        }
        .username {
          font-weight: bold;
          padding-left: 5px;
        }
      }
    }
  }
  .item-footer {
    border-top: 1px solid #dfdfdf;
    box-sizing: border-box;
    margin: 5px 0;
    .actions-main {
      display: flex;
      align-items: center;
      .read-time {
        font-size: 12px;
        color: #9b9b9b;
        height: 100%;
        display: flex;
        align-items: center;
        padding: 12px 5px;
      }
      .info-icons {
        display: flex;
        justify-content: flex-end;
      }
      .label {
        box-sizing: border-box;
        padding: 0 5px;
        display: flex;
        justify-content: center;
        align-items: center;
        color: #8b8b8b;
        button {
          margin: 6px 0;
        }
      }
    }
  }
}
</style>
