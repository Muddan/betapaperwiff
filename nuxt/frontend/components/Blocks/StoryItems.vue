<template>
  <v-container fluid grid-list-md>
    <v-layout row wrap>
      <div class="story-loader">
        <v-progress-circular
          v-if="stories && !stories.length"
          indeterminate
          color="#f45b69"
        ></v-progress-circular>
      </div>
      <v-flex
        v-for="(item, index) in stories"
        :key="index"
        class="story-items-main"
      >
        <v-list two-line>
          <template>
            <v-layout>
              <v-flex xs2 justify-center>
                <v-list-tile>
                  <v-list-tile-avatar size="70" avatar>
                    <img src="https://cdn.vuetifyjs.com/images/lists/2.jpg" />
                  </v-list-tile-avatar>
                  <!-- <v-btn
                    flat
                    :loading="loading"
                    :disabled="loading"
                    color="secondary"
                    @click="loader = 'loading'"
                  >
                    <v-icon left color="#f45b69">add</v-icon>Follow
                  </v-btn>-->
                </v-list-tile>
              </v-flex>
              <v-flex xs10>
                <v-subheader :key="item.userName">{{
                  item.userName
                }}</v-subheader>
                <p :key="item.datePublished">
                  {{ new Date(item.datePublished).toLocaleString() }}
                </p>
              </v-flex>
            </v-layout>
            <v-divider :key="Math.random()" :inset="true"></v-divider>
            <v-container class="story-content-main">
              <v-list-tile-content :key="Math.random()">
                <router-link
                  class="story-title"
                  :to="{
                    name: 'userprofile',
                    params: {
                      storyId: item.storyId,
                      userName: '@navaneeth'
                    }
                  }"
                >
                  <p>{{ item.storyTitle }}</p>
                </router-link>

                <p
                  class="summary"
                  v-html="item.content.substring(0, 460) + ' . . .'"
                ></p>
              </v-list-tile-content>
              <StoryTags :tags="item.tags"></StoryTags>
            </v-container>
            <v-divider :key="Math.random()" :inset="false"></v-divider>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn icon>
                <v-icon>favorite_border</v-icon>
              </v-btn>
              <!-- <v-btn icon>
                <v-icon>share</v-icon>
              </v-btn>-->
            </v-card-actions>
          </template>
        </v-list>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapGetters } from 'vuex'
import StoryTags from '@/components/Blocks/StoryTags.vue'
export default {
  name: 'StoryItems',
  components: {
    StoryTags
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
      filteredStories: 'Stories/filteredStories',
      allStories: 'Stories/allStories',
      isSignedIn: 'User/isSignedIn'
    }),
    getCurrentUserFeed() {
      if (this.filteredStories.length > 0) {
        return this.filteredStories
      } else {
        return this.allStories
      }
    }
  }
}
</script>
<style lang="scss" scoped>
.story-items-main {
  .v-list {
    border-radius: 8px;
    border: 1px solid #114b5f;
    border-bottom: 4px solid #114b5f;
    margin: 10px 0;

    .story-title {
      font-family: 'Cormorant Garamond', serif;
      font-size: 26px;
      color: #161616;
      text-decoration: underline;
    }
  }
}
</style>
