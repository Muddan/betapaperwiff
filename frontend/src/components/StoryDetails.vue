<template>
  <v-container>
    <div class="story-loader">
      <v-progress-circular v-if="!getStoryDetails" indeterminate color="#f45b69"></v-progress-circular>
    </div>
    <div class="story-details" v-if="getStoryDetails">
      <div class="main-content">
        <v-layout>
          <v-flex md1 xs12 class="hidden-sm-and-down">
            <share-story v-if="storyUrl" :url="storyUrl"></share-story>
          </v-flex>
          <v-flex md8 xs12>
            <div class="story-poster">
              <img
                class="poster"
                src="https://res.cloudinary.com/practicaldev/image/fetch/s--yUyi4zBB--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://thepracticaldev.s3.amazonaws.com/i/pf9l84zqr2hpqg2nl6yi.jpg"
                alt
              >
            </div>
            <div class="content-section">
              <div class="title-section">
                <header>
                  <h1 class="main-title">{{ getStoryDetails.storyTitle }}</h1>
                  <v-layout class="mini-profile" align-center row spacer>
                    <v-flex xs4 sm2 md1>
                      <v-avatar class="profile-img" size="36px">
                        <img :src="author.userImage" alt="Avatar">
                      </v-avatar>
                    </v-flex>
                    <v-flex xs4 sm2 md1>
                      <router-link
                        class="story-title"
                        :to="{
                        name: 'userprofile',
                        params: {
                          userName: getStoryDetails.userName,
                        }
                      }"
                      >
                        <span class="username">{{getStoryDetails.userName}}</span>
                      </router-link>
                    </v-flex>
                  </v-layout>
                  <p class="date">{{ new Date(getStoryDetails.datePublished).toLocaleString() }}</p>
                  <story-tags :tags="getStoryDetails.tags"></story-tags>
                </header>
              </div>
              <div class="story-content" v-html="getStoryDetails.content"></div>
            </div>
          </v-flex>
          <v-flex class="sidebar-section sidebar-left hidden-sm-and-down" md3 xs12>
            <author-info :author="author"></author-info>
            <key-links></key-links>
          </v-flex>
        </v-layout>
      </div>
    </div>
  </v-container>
</template>

<script>
import { mapGetters } from "vuex";
import KeyLinks from "@/components/Blocks/KeyLinks.vue";
import AuthorInfo from "@/components/Blocks/AuthorInfo.vue";
import StoryTags from "@/components/Blocks/StoryTags.vue";
import ShareStory from "@/components/Blocks/ShareStory.vue";

export default {
  name: "StoryDetails",
  data() {
    return {
      author: {}
    };
  },
  components: {
    KeyLinks,
    AuthorInfo,
    StoryTags,
    ShareStory
  },
  computed: {
    ...mapGetters({
      getCurrentStory: "Stories/currentStory"
    }),
    getStoryDetails() {
      return this.getCurrentStory;
    },
    storyUrl() {
      if (window.location.href) {
        return window.location.href;
      }
    }
  },
  async mounted() {
    await this.$store.dispatch(
      "Stories/getCurrentStory",
      this.$route.params.storyId
    );

    await this.$store
      .dispatch("User/getUserDetails", this.$route.params.userName)
      .then(res => {
        if (res.status == 200) {
          this.author = res.data;
        } else {
          console.log("Error fetching author details");
        }
      });
  }
};
</script>

<style lang="scss" scoped>
.story-details {
  .story-poster {
    padding: 0 30px;
    box-sizing: border-box;
    .poster {
      width: 100%;
      border-radius: 8px;
      display: inherit;
    }
  }
  .content-section {
    padding: 35px 30px 30px;
    box-sizing: border-box;
    border-radius: 8px;
    margin: 0 20px;
    background: #fff;
    margin-top: -40px;
    .title-section {
      padding-bottom: 20px;
      max-width: 90%;
      margin: auto;
      .main-title {
        font-family: "Cormorant Garamond", serif;
        font-size: 57px;
        text-align: left;
        text-decoration: underline;
      }
      .date {
        padding-top: 10px;
        font-size: 12px;
        color: #b1b1b1;
      }
    }
    .story-content {
      font-size: 16px;
      max-width: 90%;
      margin: auto;
      padding-bottom: 20px;
      &::after {
        content: "";
        width: 80%;
        margin: auto;
        background: #2e2e2e;
        height: 1px;
        display: block;
      }
    }
  }
}
</style>

