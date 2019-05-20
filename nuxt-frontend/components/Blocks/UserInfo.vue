<template>
  <div v-if="isSignedIn" class="user-info">
    <v-list-tile avatar>
      <v-list-tile-avatar>
        <nuxt-link
          class="user-link"
          :to="{
            path: '/a/' + currentUser.userName
          }"
        >
          <v-avatar>
            <img :src="currentUser.userImage" alt="John" />
          </v-avatar>
        </nuxt-link>
      </v-list-tile-avatar>

      <v-list-tile-content>
        <v-list-tile-title
          >{{ currentUser.firstName }}
          {{ currentUser.lastName }}</v-list-tile-title
        >
        <nuxt-link
          class="user-link"
          :to="{
            path: '/a/' + currentUser.userName
          }"
        >
          {{ currentUser.userName }}
        </nuxt-link>
      </v-list-tile-content>
    </v-list-tile>
    <div v-if="userTags.length > 0" class="following-tags-main">
      <v-subheader class="tag-header">Your tags</v-subheader>
      <StoryTags :story-tags="userTags"></StoryTags>
    </div>
    <v-subheader v-else class="tag-header"
      >You are not following any tags</v-subheader
    >
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
import StoryTags from '@/components/Blocks/StoryTags.vue'
export default {
  name: 'UserInfo',
  components: {
    StoryTags
  },
  computed: {
    ...mapGetters({
      isSignedIn: 'user/isSignedIn',
      currentUser: 'user/currentUser',
      currentTags: 'stories/availableTags'
    }),
    userTags() {
      return this.currentUser.followingTags
    }
  }
}
</script>
<style lang="scss" scoped>
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
