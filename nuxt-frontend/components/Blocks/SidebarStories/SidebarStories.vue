<template>
  <div class="sidebar-stories-main">
    <v-list three-line>
      <v-subheader>
        <slot name="title"></slot>
      </v-subheader>
      <v-divider></v-divider>

      <div class="text-xs-center">
        <v-progress-circular
          v-if="showStories && !showStories.length"
          indeterminate
          color="#f45b69"
        ></v-progress-circular>
      </div>

      <template v-for="(story, index) in showStories">
        <StoryTile :key="story.storyTitle" :story="story"></StoryTile>
        <v-divider
          v-show="index != showStories.length - 1"
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
  props: {
    storiesArray: {
      type: Array,
      default: null
    },
    isPopularStories: {
      type: Boolean,
      default: true
    }
  },
  data() {
    return {
      showStories: []
    }
  },
  computed: {
    ...mapGetters({
      popularStories: 'stories/popularStories'
    })
  },
  async beforeMount() {
    await this.$store.dispatch('stories/getPopularStories')
    if (this.isPopularStories) {
      this.showStories = this.popularStories
    } else {
      this.showStories = this.storiesArray
    }
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
