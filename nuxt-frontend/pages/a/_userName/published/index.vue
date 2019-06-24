<template>
  <div class="saved-later-wrapper">
    <v-container>
      <v-layout>
        <v-flex md3 class="hidden-md-and-down"></v-flex>
        <v-flex md6 class="main-layout">
          <div class="saved-wrapper">
            <v-subheader>
              Stories by {{ this.$route.params.userName }}
            </v-subheader>
            <PublishedStories
              v-if="publishedStories.length > 0"
              :stories="publishedStories"
            ></PublishedStories>
            <div v-else class="readinglist-empty">
              <h1 class="info-text">You have not posted any stories</h1>
              <h3>
                Hit the <strong>write button</strong> to start your Collection
              </h3>
            </div>
          </div>
        </v-flex>
        <v-flex md3 class="hidden-md-and-down"></v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import { endpoints } from '@/api/endpoints.js'
import { SocialFeatures } from '@/mixins/SocialFeatures.js'
import PublishedStories from '@/components/Blocks/PublishedStories.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'SavedStories',
  transition: 'slidedown',
  components: {
    PublishedStories
  },
  mixins: [SocialFeatures],
  computed: {
    ...mapGetters({
      publishedStories: 'user/userArticlesStories'
    })
  },
  async asyncData({ route, store, params, error, app }) {
    let savedStories = {}

    await app
      .$axios({
        method: 'GET',
        url: `${endpoints.API_GET_AUTHOR_STOREIS}?userName=${
          route.params.userName
        }`
      })
      .then(res => {
        savedStories = res.data.result.items
        store.commit('user/SET_PUBLISHED_STORIES', savedStories)
      })
      .catch(() => {
        error({ statusCode: 404 })
      })
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
}
</style>
