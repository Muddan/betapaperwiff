<template>
  <div class="tag-list-normal">
    <div class="chip-content">
      <v-chip
        v-for="(tag, index) in storyTagsAvailable"
        :key="index"
        label
        flat
      >
        <nuxt-link
          :to="{
            path: '/tags/' + tag.value
          }"
          ># {{ tag.name }}</nuxt-link
        >
      </v-chip>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'TagListNormal',
  computed: {
    ...mapGetters({
      storyTagsAvailable: 'stories/availableTags'
    })
  }
}
</script>
<style lang="scss">
.tag-list-normal {
  .chip-content {
    .v-chip {
      background: #f1f1f1;
      border-radius: 8px;
    }
  }
}
</style>
