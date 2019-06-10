<template>
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
                  new Date(story.datePublished).toLocaleString('en-us', {
                    month: 'long',
                    day: 'numeric'
                  })
                }}
              </span>
              <span>&#9733;</span>
              <!-- <span class="relative-date">
                {{ getPublishedDate(story.datePublished) }}
                <span>ago</span>
              </span> -->
            </span>
          </v-subheader>
          <!-- <div class="save-later">
            <v-btn
              flat
              icon
              color="grey darken-5"
              @click="saveStory(story.storyId)"
            >
              <v-icon>{{
                savedStory(story.storyId) ? 'bookmarks' : 'bookmark_border'
              }}</v-icon>
            </v-btn>
          </div> -->
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
    <!-- <div class="item-footer">
      <div class="actions-main">
        <v-layout>
          <v-flex xs6>
            <span class="read-time">
              {{ Math.floor(story.content.split(' ').length / 160) }}
              min read
            </span>
          </v-flex>
          <v-flex info-icons xs6>
            <v-tooltip top>
              <template v-slot:activator="{ on }">
                <div class="label">
                  <v-btn small flat icon color="grey darken-5" v-on="on">
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
    </div> -->
  </div>
</template>

<script>
export default {
  props: {
    story: {
      type: Object,
      default: null
    }
  }
}
</script>

<style></style>
