<template>
  <div class="homepage-main">
    <v-container>
      <v-layout column justify-center align-center>
        <v-flex xs12 sm8 md6>
          <div class="text-xs-center">paperwiff</div>
        </v-flex>
      </v-layout>
      <v-layout>
        <v-flex
          class="sidebar-section sidebar-left hidden-sm-and-down"
          md3
          xs12
        >
          <TagListing></TagListing>
        </v-flex>
        <v-flex class="content-section" md6 xs12>
          <StoryListing></StoryListing>
        </v-flex>
        <v-flex
          class="sidebar-section sidebar-right hidden-sm-and-down"
          md3
          xs12
        ></v-flex>
      </v-layout>
      <button @click="authenticate('github')">auth Github</button>
      <button @click="authenticate('facebook')">auth Facebook</button>
      <button @click="authenticate('google')">auth Google</button>
      <button @click="authenticate('twitter')">auth Twitter</button>
    </v-container>
  </div>
</template>

<script>
import StoryListing from '@/components/Blocks/StoryListing.vue'
import TagListing from '@/components/Blocks/TagListing.vue'
export default {
  components: {
    StoryListing,
    TagListing
  },
  methods: {
    authenticate: function(provider) {
      this.$auth.authenticate(provider).then(function() {
        // Execute application logic after successful social authentication
      })
    }
  }
}
</script>
<style lang="scss" scoped>
.homepage-main {
  max-width: 1400px;
  margin: auto;
}
</style>
