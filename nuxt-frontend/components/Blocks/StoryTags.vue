<template>
  <div class="story-chips">
    <div class="chip-content">
      <v-chip v-for="(tag, index) in storyTags" :key="index" small label>
        <nuxt-link
          :to="{
            path: '/tags/' + tag
          }"
          >#{{ tag }}</nuxt-link
        >
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
    }
  }
}
</script>
<style lang="scss">
.story-chips {
  .chip-content {
    .v-chip.v-chip--label {
      border-radius: 8px;
      overflow: hidden;
      .v-chip__content {
        background: #f4faff;
        a {
          color: #2e2e2e;
          font-size: 13px;
        }
      }
    }
  }
}
</style>
