<template>
  <div class="profile-content-main">
    <v-container>
      <v-window v-model="onboarding">
        <v-window-item>
          <v-container v-bind="{ [`grid-list-lg`]: true }" fluid>
            <header>
              <h3>Please select atleast 3 Tags to follow</h3>
            </header>
            <v-layout row wrap>
              <v-flex
                v-for="(tags, index) in storyTagsAvailable"
                :key="index"
                xs2
              >
                <v-card
                  flat
                  ripple
                  tile
                  class="tag-card-main"
                  @click="followTag(tags)"
                >
                  <v-list-tile class="d-flex align-center">
                    <span class="tagname"> # {{ tags }} </span>
                  </v-list-tile>
                </v-card>
              </v-flex>
            </v-layout>
          </v-container>
        </v-window-item>
        <v-window-item>
          TELL US MORE ABOUT YOU
        </v-window-item>
      </v-window>

      <v-card-actions class="justify-space-between">
        <v-btn flat @click="prev">
          <v-icon>fa fa-chevron-left</v-icon>
        </v-btn>
        <v-btn flat @click="next">
          <v-icon>fa fa-chevron-right</v-icon>
        </v-btn>
      </v-card-actions>
    </v-container>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'

export default {
  data() {
    return {
      followingTags: [],
      length: 3,
      onboarding: 0
    }
  },
  computed: {
    ...mapGetters({
      storyTagsAvailable: 'stories/availableTags',
      isSignedIn: 'user/isSignedIn'
    }),
    currentTags() {
      return this.storyTagsAvailable
    }
  },
  methods: {
    next() {
      this.onboarding =
        this.onboarding + 1 === this.length ? 0 : this.onboarding + 1
    },
    prev() {
      this.onboarding =
        this.onboarding - 1 < 0 ? this.length - 1 : this.onboarding - 1
    },
    randomColor() {
      return '#' + Math.floor(Math.random() * 16777215).toString(16)
    },
    followTag(tag) {
      if (this.followingTags.includes(tag)) {
        this.followingTags = this.followingTags.filter(item => {
          return item !== tag
        })
      } else if (this.followingTags.length <= 3) {
        this.followingTags.push(tag)
        if (this.followingTags.length >= 3) {
          this.next()
        }
      }
    }
  }
}
</script>
<style lang="scss">
.profile-content-main {
  max-width: 1400px;
  margin: auto;
  .tag-card-main {
    cursor: pointer;
    &:hover {
      background: rgb(219, 241, 255);
    }
  }
}
</style>
