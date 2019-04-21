<template>
  <div class="user-profile-main">
    <v-layout fluid row class="user-profile-header" v-if="userProfile">
      <v-flex class="img-container" xs4>
        <img class="profile-img" :src="userProfile.userImage" alt>
      </v-flex>

      <v-flex xs8 class="profile-details">
        <v-layout fluid align-center justify-center fill-height>
          <v-flex xs8>
            <h1 class="profile-name">{{userProfile.userName}}</h1>
            <p class="profile-bio">{{ userProfile.about }}</p>
          </v-flex>
          <v-flex xs1>
            <v-divider class="mx-3" vertical></v-divider>
          </v-flex>
          <v-flex xs3 class="joined-details">
            <h3 class="label">Joined</h3>
            <p class="value">{{ new Date(userProfile.joined).toLocaleString() }}</p>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
    <v-layout>
      <v-flex xs3>
        <v-flex class="sidebar-section sidebar-left hidden-sm-and-down">
          <key-links></key-links>
        </v-flex>
      </v-flex>
      <v-flex xs9>
        <v-flex class="sidebar-section sidebar-main hidden-sm-and-down">
          <story-items :stories="allStories"></story-items>
        </v-flex>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import StoryItems from "@/components/Blocks/StoryItems.vue";
import KeyLinks from "@/components/Blocks/KeyLinks.vue";

export default {
  name: "Profile",
  components: {
    StoryItems,
    KeyLinks
  },
  computed: {
    ...mapGetters({
      getUserProfile: "User/getUserProfile",
      allStories: "Stories/allStories"
    }),
    userProfile() {
      return this.getUserProfile;
    }
  },
  beforeMount() {
    this.$store.dispatch("User/getUserDetails", "111704191453898225276");
  }
};
</script>
<style lang="scss">
.user-profile-main {
  .user-profile-header {
    border: 1px solid #3e3e3e;
    border-radius: 4px;
    border-bottom: 4px solid #3e3e3e;
    box-sizing: border-box;
    padding: 20px;
    .img-container {
      .profile-img {
        border-radius: 50%;
        padding: 10px;
      }
    }

    .profile-details {
      .profile-name {
        font-size: 50px;
        font-weight: bold;
        text-decoration: underline;
      }
      .profile-bio {
        max-width: 80%;
      }
    }
  }

  .sidebar-left {
    margin-top: 30px;
  }
  // bottom section
}
</style>

