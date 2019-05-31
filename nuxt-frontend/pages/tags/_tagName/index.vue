<template>
  <div class="tag-view-main">
    <div>
      <div v-if="tagExits.length > 0">
        <div class="tagDetails">
          <div class="tagname-section">
            <header>
              <p class="label">Stories in</p>
              <h3 class="main-title">{{ tagName }}</h3>
              <div class="follow-tag-wrapper">
                <v-btn
                  small
                  round
                  outline
                  color="#337fb5"
                  @click.stop="followTag()"
                  >{{ !followedTags ? 'Follow' : 'Following' }}</v-btn
                >
              </div>
              <!-- <div class="tag-stats">
                <span class="stat-value">{{ stories.length }} </span>
                <span class="stat-label">posts</span>
              </div> -->
            </header>
          </div>
          <div class="main-content">
            <v-layout>
              <v-flex
                class="sidebar-section sidebar-left hidden-sm-and-down"
                md3
                xs12
              >
                <h3 class="available-tags">Available tags</h3>
                <TagListNormal></TagListNormal>
              </v-flex>
              <v-flex class="content-section" md6 xs12>
                <story-items
                  v-if="stories.length > 0"
                  :stories="stories"
                ></story-items>
                <div v-else class="nopost">
                  <h3 class="text">
                    No posts available!
                  </h3>
                </div>
              </v-flex>
            </v-layout>
          </div>
        </div>
      </div>
      <div v-else>
        <div class="nf-content">
          <v-layout>
            <div class="nf-section">
              <h2 class="oops">Oops!</h2>
              <h3 class="msg">This tag is not available.</h3>
              <div class="homelink">
                <router-link to="/">Let's go Home</router-link>
              </div>
            </div>
          </v-layout>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import StoryItems from '@/components/Blocks/StoryItems.vue'
import TagListNormal from '@/components/Blocks/TagListing/TagListNormal.vue'
import { endpoints } from '@/api/endpoints.js'

export default {
  head() {
    return {
      title: 'Paperwiff | Tags'
    }
  },
  components: {
    StoryItems,
    TagListNormal
  },
  data() {
    return {
      followed: false,
      tagName: ''
    }
  },
  computed: {
    ...mapGetters({
      availableTagNames: 'stories/availableTags',
      isSignedIn: 'user/isSignedIn',
      allStories: 'stories/allStories',
      followingTags: 'user/followingTags'
    }),
    tagExits() {
      const currentTagName = this.$route.params.tagName
      return this.availableTagNames.map(tag => {
        return tag.name === currentTagName
      })
    },
    followedTags() {
      if (this.isSignedIn) {
        return this.followingTags.includes(this.$route.params.tagName)
      } else {
        return false
      }
    }
  },
  async asyncData({ app, store, route }) {
    const allStories = await app.$axios.$get(
      `${endpoints.API_GET_TAG_STORIES}?tag=${route.params.tagName}`
    )
    return {
      stories: allStories.result.items,
      tagName: route.params.tagName
    }
  },
  mounted() {
    this.followed = this.followedTags
  },
  methods: {
    followTag() {
      if (!this.isSignedIn) {
        this.$store.commit('ui/SET_SHOW_POPUP', {
          status: true,
          component: 'SignUp'
        })
      } else {
        this.snackbar = true
        this.$store.dispatch('stories/addToFollowingFilters', {
          name: this.tagName
        })
      }
    }
  }
}
</script>

<style lang="scss">
$logosection-color: #043344;
.tag-view-main {
  max-width: 1400px;
  margin: auto;
  .tagname-section {
    margin: 20px 0 0;
    padding: 20px;
    box-sizing: border-box;
    text-align: left;
    // color: #36789a;
    .label {
      margin: 10px 0 0 8px;
      text-transform: capitalize;
      opacity: 0.5;
    }
    .main-title {
      margin: 10px 0 0 8px;
      font-size: 40px;
      font-weight: bold;
      text-transform: capitalize;
      line-height: normal;
    }
    .follow-tag-wrapper {
      margin: 10px 0 0 0;
    }
  }
  .nf-content {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    .oops {
      font-size: 5rem;
    }
    .msg {
      text-transform: uppercase;
    }
    .homelink {
      text-align: center;
      box-sizing: border-box;
      padding: 15px;
      margin: 20px 0;
      a {
        font-size: 26px;
        font-weight: bold;
        text-decoration: underline;
        color: #043344;
      }
    }
  }
  .tagDetails {
    .keylinks-main {
      margin-top: 35px;
    }
  }
  .main-content {
    .sidebar-section {
      margin: 10px 10px 0 10px;
      border-top: 1px solid #e3e3e3;

      .available-tags {
        padding-left: 12px;
        margin: 20px 0;
      }
    }
    .content-section {
      margin: 10px 10px 0 10px;
      .nopost {
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
      }
    }
  }
}
</style>
