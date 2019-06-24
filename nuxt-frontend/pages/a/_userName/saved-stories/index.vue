<template>
  <div class="saved-later-wrapper">
    <v-container>
      <v-layout>
        <v-flex md3 class="hidden-md-and-down left-sidebar">
          <TagListing></TagListing
        ></v-flex>
        <v-flex md8 class="main-layout">
          <div class="saved-wrapper">
            <v-subheader>
              Your reading list
            </v-subheader>
            <v-list v-if="readingListStories.length > 0" two-line subheader>
              <v-list-tile
                v-for="story in readingListStories"
                :key="story.storyTitle"
                avatar
              >
                <v-list-tile-content>
                  <nuxt-link
                    class="story-link-main"
                    :to="{
                      path: '/a/' + story.userName + '/' + story.storyId
                    }"
                  >
                    <v-list-tile-title>{{
                      story.storyTitle
                    }}</v-list-tile-title>
                    <v-list-tile-sub-title>{{
                      story.summary
                    }}</v-list-tile-sub-title>
                  </nuxt-link>

                  <v-list-tile-sub-title class="story-footer">
                    <v-list-tile-avatar :size="30">
                      <img :src="story.userImage" />
                    </v-list-tile-avatar>
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
                    <span>&#9733;</span>
                    <span class="full-date">
                      {{
                        new Date(story.datePublished).toLocaleString('en-us', {
                          month: 'long',
                          day: 'numeric'
                        })
                      }}
                    </span>
                    <span>&#9733;</span>
                    <span class="read-time">
                      {{
                        Math.floor(story.content.split(' ').length / 160)
                          ? Math.floor(story.content.split(' ').length / 160)
                          : 'less than a'
                      }}
                      min read
                    </span>
                  </v-list-tile-sub-title>
                </v-list-tile-content>

                <v-list-tile-action>
                  <v-btn
                    flat
                    icon
                    ripple
                    color="grey darken-5"
                    @click="saveStory(story.storyId)"
                  >
                    <v-icon>{{
                      savedStory(story.storyId)
                        ? 'bookmarks'
                        : 'bookmark_border'
                    }}</v-icon>
                  </v-btn>
                </v-list-tile-action>
              </v-list-tile>
            </v-list>
            <div v-else class="readinglist-empty">
              <h1 class="info-text">Your Reading List is Lonely</h1>
              <h3>
                Hit the <strong>Bookmark</strong> to start your Collection
              </h3>
            </div>
          </div>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import { endpoints } from '@/api/endpoints.js'
import TagListing from '@/components/Blocks/TagListing/TagListing.vue'
import { SocialFeatures } from '@/mixins/SocialFeatures.js'
import { mapGetters } from 'vuex'
export default {
  name: 'SavedStories',
  transition: 'slidedown',

  components: {
    TagListing
  },
  mixins: [SocialFeatures],
  computed: {
    ...mapGetters({
      readingListStories: 'user/readingListStories',
      isSignedIn: 'user/isSignedIn',
      savedStories: 'user/savedStories'
    })
  },
  async asyncData({ route, store, params, error, app }) {
    let savedStories = {}
    if (
      store.state.user.isSignedIn &&
      store.state.user.current.userName === route.params.userName
    ) {
      await app.$axios
        .$post(endpoints.API_GET_USER_SAVED_STORIES, {
          userId: store.state.user.current.userId
        })
        .then(res => {
          if (res.result.status === 200) {
            savedStories = res.result.items
            store.commit('user/SET_READINGLIST', savedStories)
          }
        })
    } else {
      error({ statusCode: 404 })
    }
  },
  methods: {
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
.saved-later-wrapper {
  max-width: 1400px;
  margin: auto;
  .main-layout {
    margin: 0 20px;
    @media (max-width: 768px) {
      margin: 0 0;
    }
  }
  .saved-wrapper {
    box-sizing: border-box;
    background: none;

    .v-list {
      border-radius: 10px;
      background: none;
      .v-list__tile {
        background: #fff;
        margin-bottom: 20px;
        box-shadow: 0 10px 20px 0 rgba(0, 0, 0, 0.05);
        border-radius: 10px;
        box-sizing: border-box;
        padding: 15px;
      }
    }
    .story-link-main {
      width: 100%;
    }
    .story-footer {
      margin: 10px 0;
      .v-list__tile__avatar {
        display: inline-block;
        min-width: max-content;
        padding-right: 10px;
      }
    }
  }
  .v-list__tile.v-list__tile--avatar {
    height: auto;
  }
  .readinglist-empty {
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    background: #fff;
    border-radius: 10px;
    padding: 30px 0;
    box-shadow: 0 10px 20px 0 rgba(0, 0, 0, 0.05);
    .info-text {
      @media (max-width: 768px) {
        font-size: 20px;
      }
    }
  }
  .left-sidebar {
    margin-top: 50px;
  }
}
</style>
