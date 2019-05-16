<template>
  <v-container class="padding-0" fluid>
    <no-ssr>
      <v-layout column wrap>
        <div class="story-loader">
          <v-progress-circular
            v-if="stories && !stories.length"
            indeterminate
            color="#f45b69"
          ></v-progress-circular>
        </div>

        <!-- Story items listing -->
        <v-card
          v-for="(story, index) in stories"
          :key="index"
          flat
          ripple
          class="story-items-main"
          :to="{
            path: '/a/' + story.userName + '/' + story.storyId
          }"
        >
          <div class="story-items-content">
            <div class="item-header">
              <span class="published-date">
                {{ getPublishedDate(story.datePublished) }}
              </span>
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
            </div>
            <div class="item-subheader">
              <div class="flex items-left">
                <v-avatar class="avatar-main" size="45px" color="red">
                  <span class="white--text avatar-name">{{
                    story.userName[1]
                  }}</span>
                </v-avatar>
                <v-subheader class="username-header">
                  <nuxt-link
                    class="story-title"
                    :to="{
                      path: '/a/' + story.userName
                    }"
                  >
                    <span class="username">
                      {{ story.userName }}
                    </span>
                  </nuxt-link>

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
                </v-subheader>
              </div>
              <div class="footer">
                <div class="actions-main">
                  <v-btn flat color="pink">
                    <v-icon left>favorite</v-icon>
                    <span>{{ story.likes }}</span>
                  </v-btn>
                </div>
              </div>
            </div>
          </div>
        </v-card>
      </v-layout>
    </no-ssr>
  </v-container>
</template>

<script>
import { mapGetters } from 'vuex'
// import StoryTags from '@/components/Blocks/StoryTags.vue'
import { getDate } from '@/helpers/dateHelper.js'
export default {
  name: 'StoryItems',
  components: {
    // StoryTags
  },
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
      isSignedIn: 'user/isSignedIn'
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
      return getDate(date)
    }
  }
}
</script>
<style lang="scss" scoped>
.padding-0 {
  padding: initial 0;
}
.story-items-main {
  border-radius: 8px;
  border: 1px solid #114b5f;
  border-bottom: 4px solid #114b5f;
  margin: 10px 0;
  background: #fff;
  padding: 10px 15px;
  box-sizing: border-box;
  @media (max-width: 1024px) {
    padding-bottom: 0;
  }
  .published-date {
    color: #114b5f;
    font-size: 12px;
    @media (max-width: 768px) {
      font-size: 10px;
    }
  }
  .item-header {
    .story-title {
      font-family: 'EB Garamond', serif;
      font-style: normal;
      font-weight: 200;
      font-size: 32px;
      color: #161616;
      text-decoration: underline;
      text-transform: capitalize;
      @media (max-width: 1024px) {
        font-size: 22px;
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
    }
    .avatar-name {
      text-transform: uppercase;
    }
    .username-header {
      display: block;
      padding: 0 5px;
      a {
        text-decoration: none;
        color: #2e2e2e;
      }
      .username {
        font-weight: bold;
        padding-left: 5px;
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
  }
  .footer {
    box-sizing: border-box;
    padding: 10px 0;
    display: flex;
    justify-content: flex-end;
    align-items: center;
  }
}
</style>
