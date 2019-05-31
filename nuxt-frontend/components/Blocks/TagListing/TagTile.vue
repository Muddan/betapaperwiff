<template>
  <div class="chip-wrapper">
    <v-chip color="transparent" label text-color="white">
      <nuxt-link
        :to="{
          path: '/tags/' + tag.name
        }"
      >
        <span class="tagname"> # {{ tag.name }} </span>
      </nuxt-link>
    </v-chip>
    <v-chip
      small
      label
      color="#ffeaec"
      text-color="#2e2e2e"
      @click.stop="chipHandler()"
    >
      <v-avatar>
        <v-icon right color="#f45b69">{{
          !followedTags ? 'add' : 'check'
        }}</v-icon>
      </v-avatar>
      {{ !followedTags ? 'Follow' : 'Following' }}
    </v-chip>
    <v-snackbar v-model="snackbar">
      Processing...
      <v-btn dark flat @click="snackbar = false">
        Close
      </v-btn>
    </v-snackbar>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'TagTile',
  props: {
    tag: {
      type: Object,
      default: null
    }
  },
  data() {
    return {
      added: false,
      snackbar: false
    }
  },
  computed: {
    ...mapGetters({
      isSignedIn: 'user/isSignedIn',
      followingTags: 'user/followingTags'
    }),
    followedTags() {
      if (this.isSignedIn && this.followingTags) {
        return this.followingTags.includes(this.tag.name)
      } else {
        return false
      }
    }
  },
  methods: {
    chipHandler() {
      if (!this.isSignedIn) {
        this.$store.commit('ui/SET_SHOW_POPUP', {
          status: true,
          component: 'SignUp'
        })
      } else {
        this.added = !this.added
        this.snackbar = true
        this.$store.dispatch('stories/addToFollowingFilters', this.tag)
      }
    }
  }
}
</script>

<style></style>
