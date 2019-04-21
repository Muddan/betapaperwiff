<template>
  <v-container>
    <v-content>
      <v-layout>
        <v-flex class="content-section" xs12>
          <component :is="activeComponent"></component>
        </v-flex>
      </v-layout>
    </v-content>
  </v-container>
</template>

<script>
import StoryDetails from "@/components/StoryDetails.vue";
import Profile from "@/components/Profile.vue";
export default {
  name: "UserProfile",
  components: {
    StoryDetails,
    Profile
  },
  computed: {
    activeComponent() {
      if (this.$route.params.storyId) {
        return "story-details";
      } else {
        return "profile";
      }
    }
  },
  mounted() {
    if (this.$route.params.storyId) {
      this.$store.dispatch(
        "Stories/getCurrentStory",
        this.$route.params.storyId
      );
    } else {
      this.$store.dispatch("User/getUserDetails", this.$route.params.userName);
    }
  }
};
</script>

<style>
</style>
