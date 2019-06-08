<template>
  <v-carousel hide-controls>
    <v-carousel-item v-for="(item, i) in allStories" :key="i">
      <StoryCard :story="item"></StoryCard>
    </v-carousel-item>
  </v-carousel>
</template>
<script>
import { mapGetters } from 'vuex'
import StoryCard from '@/components/Blocks/StoryCard.vue'

export default {
  components: {
    StoryCard
  },
  computed: {
    ...mapGetters({
      allStories: 'stories/allStories'
    })
  }
}
</script>
