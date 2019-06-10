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

      <template v-for="(story, index) in getStories">
        <StoryTile :key="story.storyTitle" :story="story"></StoryTile>
        <v-divider
          v-show="index != getStories.length - 1"
          :key="story.storyId"
        ></v-divider>
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
      popularStories: 'stories/popularStories'
    }),
    getStories() {
      return this.popularStories.slice(0, 4)
    }
  },
  beforeMount() {
    this.$store.dispatch('stories/getPopularStories')
  }
}
</script>
<style lang="scss">
.sidebar-stories-main {
  box-shadow: 0 10px 20px 0 rgba(0, 0, 0, 0.05);
  background: #fff;
  border-radius: 8px;
  border-bottom: 4px solid #ffb3b9;
  .v-list {
    border-radius: 8px;
  }
  .v-list__tile.v-list__tile--avatar {
    height: max-content;
  }
}
</style>
