<template>
  <div class="user-info" v-if="isSignedIn">
    <v-list-tile avatar>
      <v-list-tile-avatar>
        <v-avatar>
          <img src="https://cdn.vuetifyjs.com/images/john.jpg" alt="John">
        </v-avatar>
      </v-list-tile-avatar>

      <v-list-tile-content>
        <v-list-tile-title>{{ currentUser.first_name }} {{ currentUser.last_name }}</v-list-tile-title>
        <router-link
          :to="{
        name: 'userprofile',
        params: {
          username: '@' + currentUser.username,
        }
      }"
        >
          <v-list-tile-sub-title>@{{ currentUser.username }}</v-list-tile-sub-title>
        </router-link>
      </v-list-tile-content>
    </v-list-tile>
    <div
      v-if="currentUser.following_tags && currentUser.following_tags.length > 0"
      class="following-tags-main"
    >
      <v-subheader class="tag-header">Your tags</v-subheader>
      <story-tags :tags="currentUser.following_tags"></story-tags>
    </div>
    <v-subheader v-else class="tag-header">You are not following any tags</v-subheader>
  </div>
</template>
<script>
import { mapGetters } from "vuex";
import StoryTags from "@/components/Blocks/StoryTags.vue";
export default {
  name: "UserInfo",
  components: {
    StoryTags
  },
  computed: {
    ...mapGetters({
      isSignedIn: "User/isSignedIn",
      currentUser: "User/currentUser"
    })
  }
};
</script>
<style lang="scss">
.user-info {
  // background: #cfefff;
  background: #fff;

  box-sizing: border-box;
  padding: 10px;
  margin: 0 0 30px 0;

  border-radius: 8px;
  border: 1px solid #2a7b9c;
  border-bottom: 4px solid #2a7b9c;
  // box-shadow: 0 10px 30px 0 #cfefff80;

  .chip-content {
    .v-chip.v-chip--label {
      background-color: #2a7b9c !important;
      border-color: #2a7b9c !important;
      color: #fff;
      .v-icon {
        color: #fff !important;
        caret-color: #fff !important;
        cursor: pointer;
      }
    }
  }
}
</style>

