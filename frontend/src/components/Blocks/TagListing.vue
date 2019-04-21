<template>
  <div class="tags-main">
    <v-layout row justify-center>
      <v-dialog v-model="dialog" persistent max-width="290">
        <v-card>
          <v-card-text>
            <join-us></join-us>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="green darken-1" flat @click="dialog = false">Ok</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-layout>
    <v-subheader class="tag-header">Design your experience</v-subheader>
    <div class="chip-content">
      <v-list>
        <v-list-tile v-for="(tags, index) in currentTags" :key="index">
          <v-chip color="transparent" label text-color="white">
            <router-link
              :to="{
                name: 'tags',
                params: {
                  tagName: tags
                }
              }"
            ># {{ tags }}</router-link>
            <!-- <v-icon right color="#f45b69">check_circle</v-icon> -->
          </v-chip>
          <v-chip small @click.stop="chipHandler(tags)" label color="#ffeaec" text-color="#2e2e2e">
            <v-avatar>
              <v-icon right color="#f45b69">add</v-icon>
            </v-avatar>Follow
          </v-chip>
        </v-list-tile>
      </v-list>
    </div>
  </div>
</template>
<script>
import { mapGetters } from "vuex";
import JoinUs from "@/components/Blocks/JoinUs.vue";
export default {
  name: "TagListing",
  components: {
    JoinUs
  },
  data() {
    return {
      dialog: false,
      added: false,
      hover: false
    };
  },

  computed: {
    ...mapGetters({
      storyTagsAvailable: "Stories/availableTags",
      isSignedIn: "User/isSignedIn"
    }),
    currentTags() {
      return this.storyTagsAvailable;
    }
  },
  methods: {
    chipHandler(tag) {
      this.added = !this.added;
      if (!this.isSignedIn) {
        this.dialog = true;
      } else {
        this.$store.dispatch("User/addToFollowingFilters", { tag });
      }
    }
  }
};
</script>
<style lang="scss" scoped>
.tags-main {
  // background: #ffb3b9;
  background: #fff;
  box-sizing: border-box;
  padding: 10px;

  border-radius: 8px;
  // box-shadow: 0 10px 20px 0 #ffb3b978;
  border: 1px solid #ffb3b9;
  border-bottom: 4px solid #ffb3b9;

  .tag-header {
    color: #000;
    letter-spacing: 1px;
    font-size: 16px;
    border-radius: 8px;
    margin: 0 0 5px 0;
  }
  .v-icon {
    cursor: pointer;
  }
  .chip-content {
    max-height: 400px;
    overflow-y: scroll;
    overflow-x: hidden;
    a {
      color: #2e2e2e;
      text-decoration: none;
      transition: text-decoration 0.4s ease-in-out;
      &:hover {
        text-decoration: underline;
      }
    }
  }
}
</style>

