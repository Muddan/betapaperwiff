<template>
  <div class="sidebar-stories-main">
    <v-list three-line>
      <v-subheader>
        Popular Stories
      </v-subheader>
      <v-divider></v-divider>

      <div class="text-xs-center">
        <v-progress-circular
          v-if="getStories && !getStories.length"
          indeterminate
          color="#f45b69"
        ></v-progress-circular>
      </div>

      <template v-for="story in getStories">
        <StoryTile :key="story.storyTitle" :story="story"></StoryTile>
        <v-divider :key="story.storyId"></v-divider>
      </template>
    </v-list>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
import StoryTile from './StoryTile'

export default {
  components: {
    StoryTile
  },
  computed: {
    ...mapGetters({
      allStories: 'stories/allStories'
    }),
    getStories() {
      return this.allStories.slice(0, 6)
    }
  }
}
</script>
<style lang="scss">
.sidebar-stories-main {
  box-shadow: 0 10px 20px 0 rgba(0, 0, 0, 0.05);
  background: #fff;
  border-radius: 8px;
  padding-bottom: 20px;
  .v-list {
    border-radius: 8px;
  }
}
</style>
