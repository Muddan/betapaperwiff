<template>
  <div class="story-chips">
    <div class="chip-content">
      <v-chip
        v-for="(tags, index) in storyTags"
        :key="index"
        label
        color="white"
      >
        <router-link
          :to="{
            name: 'tags',
            params: {
              tagName: tags
            }
          }"
          >#{{ tags }}</router-link
        >
        <v-icon v-if="tagFollow" right color="#f45b69">check_circle</v-icon>
        <!-- <v-icon :if="tagFollow"right color="#f45b69">add</v-icon> -->
      </v-chip>
    </div>
  </div>
</template>

<script>
export default {
  name: 'StoryTags',
  props: {
    storyTags: {
      type: Array,
      default: null
    },
    tagFollow: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    chipHandler(tag) {
      this.$store.dispatch('user/addToFollowingFilters', { tag })
    }
  }
}
</script>
<style lang="scss">
.story-chips {
  .chip-content {
    .v-chip.v-chip--label {
      .v-chip__content {
        background: #f2f2f2;
        a {
          color: #2e2e2e;
        }
      }
    }
  }
}
</style>
