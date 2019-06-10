<template>
  <div class="sidebar-stories-wrapper">
    <nuxt-link
      :to="{
        path: '/a/' + story.userName + '/' + story.storyId
      }"
    >
      <v-list-tile :key="story.storyTitle" avatar>
        <div class="content-wrapper">
          <v-list-tile-content>
            <v-list-tile-title class="story-title">
              {{ story.storyTitle }}
            </v-list-tile-title>
            <!-- <v-list-tile-sub-title class="story-summary">
              {{ story.summary }}
            </v-list-tile-sub-title> -->
            <v-list-tile-title class="author-name">
              By <strong>{{ story.firstName }}</strong>
            </v-list-tile-title>
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
              <span class="read-time">
                {{ Math.floor(story.content.split(' ').length / 160) }}
                min read
              </span>
            </span>
          </v-list-tile-content>
        </div>
        <div class="image-wrapper">
          <img class="story-header" :src="story.headerImage" />
        </div>
      </v-list-tile>
    </nuxt-link>
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
<style lang="scss">
.sidebar-stories-wrapper {
  padding: 10px 0;
  margin: 10px 0;
  .content-wrapper {
    width: 70%;
    padding-right: 10px;
    .author-name {
      font-weight: normal;
      font-size: 12px;
      opacity: 0.5;
      color: #f82537;
    }
    .story-title {
      font-family: 'Cormorant Garamond', serif;
      font-style: normal;
      font-weight: normal;
      font-size: 18px;
      @media (max-width: 1024px) {
        font-size: 16px;
      }
    }
    .published-date {
      font-size: 12px;
      opacity: 0.8;
    }
  }
  .image-wrapper {
    width: 30%;
    height: 100%;
    img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      border-radius: 8px;
    }
  }
  .chip-container {
    padding: 0;
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
}
</style>
