<template>
  <v-container>
    <v-content>
      <v-layout>
        <v-flex class="sidebar-section sidebar-left hidden-sm-and-down" md3 xs12>left sidebar</v-flex>
        <v-flex class="content-section" md9 xs12>
          <component :is="activeComponent"></component>
        </v-flex>
      </v-layout>
    </v-content>
  </v-container>
</template>

<script>
import StoryDetails from "@/components/StoryDetails.vue";
export default {
  name: "UserProfile",
  components: {
    StoryDetails
  },
  computed: {
    activeComponent() {
      if (this.$route.params.story_id) {
        return "story-details";
      }
    }
  },
  mounted() {
    if (this.$route.params.story_id) {
      this.$store.dispatch(
        "Stories/getCurrentStory",
        this.$route.params.story_id
      );
    }
  }
};
</script>

<style>
</style>
