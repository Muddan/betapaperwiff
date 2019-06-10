<template>
  <div class="tags-main">
    <h3 class="tag-header">Design your experience</h3>
    <no-ssr>
      <div class="chip-content">
        <v-list>
          <div class="text-xs-center">
            <v-progress-circular
              v-if="storyTagsAvailable && !storyTagsAvailable.length"
              indeterminate
              color="#f45b69"
            ></v-progress-circular>
          </div>
          <v-list-tile v-for="(tag, index) in storyTagsAvailable" :key="index">
            <TagTile :key="index" :tag="tag"></TagTile>
          </v-list-tile>
        </v-list>
      </div>
    </no-ssr>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
import TagTile from '@/components/Blocks/TagListing/TagTile'
export default {
  name: 'TagListing',
  components: {
    TagTile
  },
  data() {
    return {
      added: false,
      hover: false
    }
  },

  computed: {
    ...mapGetters({
      storyTagsAvailable: 'stories/availableTags'
    })
  }
}
</script>
<style lang="scss">
.tags-main {
  // background: #ffb3b9;
  background: #fff;
  box-sizing: border-box;
  padding: 10px;
  border-radius: 8px;
  // border: 1px solid #ffb3b9;
  border-bottom: 4px solid #ffb3b9;
  box-shadow: 0 10px 20px 0 rgba(0, 0, 0, 0.05);
  .tag-header {
    border-bottom: 1px solid #f2f2f2;
    color: #161616;
    font-size: 16px;
    font-weight: bold;
    margin: 5px;
    padding: 10px;
    z-index: 1;
  }
  .v-icon {
    cursor: pointer;
  }
  .chip-content {
    height: 400px;
    overflow-y: scroll;
    overflow-x: hidden;
    transition: all 0.5s ease-in-out;
    a {
      color: #2e2e2e;
      text-decoration: none;
      transition: text-decoration 0.4s ease-in-out;
      &:hover {
        text-decoration: underline;
      }
    }
    .v-list {
      .v-list__tile {
        padding: 0 5px;
        display: flex;
        justify-content: space-between;
      }
    }
  }
}
</style>
