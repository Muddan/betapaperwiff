<template>
  <div class="tags-main">
    <h3 class="tag-header">Design your experience</h3>
    <no-ssr>
      <div class="chip-content">
        <v-list>
          <v-list-tile v-for="(tag, index) in storyTagsAvailable" :key="index">
            <v-chip color="transparent" label text-color="white">
              <nuxt-link
                :to="{
                  path: '/tags/' + tag.name
                }"
              >
                <span class="tagname"> # {{ tag.name }} </span>
              </nuxt-link>
              <!-- <v-icon right color="#f45b69">check_circle</v-icon> -->
            </v-chip>
            <v-chip
              small
              label
              color="#ffeaec"
              text-color="#2e2e2e"
              @click.stop="chipHandler(tag)"
            >
              <v-avatar>
                <v-icon right color="#f45b69">{{
                  !followedTags(tag.name) ? 'add' : 'check'
                }}</v-icon>
              </v-avatar>
              {{ !followedTags(tag.name) ? 'Follow' : 'Following' }}
            </v-chip>
          </v-list-tile>
        </v-list>
      </div>
    </no-ssr>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  name: 'TagListing',
  data() {
    return {
      added: false,
      hover: false
    }
  },

  computed: {
    ...mapGetters({
      storyTagsAvailable: 'stories/availableTags',
      isSignedIn: 'user/isSignedIn',
      followingTags: 'user/followingTags'
    })
  },
  methods: {
    followedTags(tag) {
      if (this.isSignedIn) {
        return this.followingTags.includes(tag)
      } else {
        return false
      }
    },
    chipHandler(tag) {
      this.added = !this.added
      if (!this.isSignedIn) {
        this.$store.commit('ui/SET_SHOW_POPUP', {
          status: true,
          component: 'SignUp'
        })
      } else {
        this.$store.dispatch('stories/addToFollowingFilters', tag)
      }
    }
  }
}
</script>
<style lang="scss">
.tags-main {
  // background: #ffb3b9;
  background: #fff;
  box-sizing: border-box;
  padding: 10px;
  border-radius: 8px;
  // border: 1px solid #ffb3b9;
  border-bottom: 4px solid #ffb3b9;
  box-shadow: 0 10px 20px 0 rgba(0, 0, 0, 0.05);
  .tag-header {
    border-bottom: 1px solid #f2f2f2;
    color: #161616;
    font-size: 16px;
    font-weight: bold;
    margin: 5px;
    padding: 10px;
    z-index: 1;
  }
  .v-icon {
    cursor: pointer;
  }
  .chip-content {
    height: 400px;
    overflow-y: scroll;
    overflow-x: hidden;
    transition: all 0.5s ease-in-out;
    a {
      color: #2e2e2e;
      text-decoration: none;
      transition: text-decoration 0.4s ease-in-out;
      &:hover {
        text-decoration: underline;
      }
    }
    .v-list {
      .v-list__tile {
        padding: 0 5px;
        display: flex;
        justify-content: space-between;
      }
    }
  }
}
</style>
