<template>
  <div class="user-info">
    <v-list-tile avatar>
      <v-list-tile-avatar>
        <v-avatar>
          <img :src="author.userImage" alt="John">
        </v-avatar>
      </v-list-tile-avatar>

      <v-list-tile-content>
        <v-list-tile-title>{{ author.firstName }} {{ author.lastName }}</v-list-tile-title>
        <router-link
          :to="{
        name: 'userprofile',
        params: {
          userName: author.userName,
        }
      }"
        >
          <v-list-tile-sub-title>{{ author.userName }}</v-list-tile-sub-title>
        </router-link>
      </v-list-tile-content>
    </v-list-tile>
  </div>
</template>
<script>
import StoryTags from "@/components/Blocks/StoryTags.vue";
export default {
  name: "UserInfo",
  props: {
    author: {
      type: Object,
      default: {}
    }
  },
  components: {
    StoryTags
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

