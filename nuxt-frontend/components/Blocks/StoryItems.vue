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
                class="story-title"
                :to="{
                  path: '/a/' + story.userName + '/' + story.storyId
                }"
              >
                <h3 class="story-title">
                  {{ story.storyTitle }}
                </h3>
              </nuxt-link>
              <!-- <p
                class="story-desc"
                v-html="
                  story.content
                    .split(' ')
                    .splice(0, 20)
                    .join(' ')
                "
              ></p> -->
            </div>
            <div class="item-subheader">
              <div class="flex items-left">
                <v-avatar class="avatar-main" size="50px">
                  <img :src="story.userImage" />
                </v-avatar>
                <v-subheader class="username-header">
                  <nuxt-link
                    class="story-title"
                    :to="{
                      path: '/a/' + story.userName
                    }"
                  >
                    <span class="username">
                      {{ story.firstName }}
                    </span>
                  </nuxt-link>
                  <span class="published-date">
                    {{ getPublishedDate(story.datePublished) }}
                  </span>
                </v-subheader>
              </div>
              <div class="footer">
                <div class="actions-main">
                  <v-btn small flat icon color="pink">
                    <v-icon small>favorite</v-icon>
                  </v-btn>
                  <span>{{ story.likes }}</span>
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
<style lang="scss">
a {
  text-decoration: none;
  color: inherit;
}
</style>

<style lang="scss" scoped>
.padding-0 {
  padding: initial 0;
}
.story-items-main {
  border-radius: 8px;
  margin: 10px 0;
  background: #fff;
  padding: 10px 15px;
  box-sizing: border-box;
  border-bottom: 4px solid #5199c3;
  box-shadow: 0 10px 20px 0 rgba(0, 0, 0, 0.05);
  @media (max-width: 1024px) {
    padding-bottom: 0;
  }
  .published-date {
    color: #b1b1b1;
    font-size: 12px;
    @media (max-width: 768px) {
      font-size: 10px;
    }
  }
  .item-header {
    .story-title {
      font-family: 'Cormorant Garamond', serif;
      font-style: normal;
      font-weight: normal;
      font-size: 34px;
      color: #161616;
      text-decoration: none;
      @media (max-width: 1024px) {
        font-size: 22px;
      }
    }
    .story-desc {
      color: #757575;
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

  .item-subheader {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    padding: 5px 0;
    .items-left {
      display: flex;
      align-items: center;
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
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding: 0 10px;
      a {
        text-decoration: none;
        color: #2e2e2e;
      }
      .username {
        font-weight: bold;
        padding-left: 5px;
      }
    }
  }
  .footer {
    box-sizing: border-box;
    padding: 10px 0;
    display: flex;
    justify-content: flex-end;
    align-items: center;
    .actions-main {
      display: flex;
      align-items: center;
      button {
        margin: 0;
      }
    }
  }
}
</style>
