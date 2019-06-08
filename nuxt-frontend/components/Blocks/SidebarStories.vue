<template>
  <div class="sidebar-stories-main">
    <v-list three-line>
      <template v-for="(item, index) in items">
        <v-subheader v-if="item.header" :key="item.header">
          Popular Stories
        </v-subheader>

        <v-divider
          v-else-if="item.divider"
          :key="index"
          :inset="item.inset"
        ></v-divider>

        <v-list-tile v-else :key="item.title" avatar>
          <v-list-tile-content>
            <v-list-tile-title v-html="item.title"></v-list-tile-title>
            <v-list-tile-sub-title
              v-html="item.subtitle"
            ></v-list-tile-sub-title>
          </v-list-tile-content>
          <v-list-tile-avatar>
            <img :src="item.avatar" />
          </v-list-tile-avatar>
        </v-list-tile>
      </template>
    </v-list>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'

export default {
  computed: {
    ...mapGetters({
      allStories: 'stories/allStories'
    })
  }
}
</script>
<style lang="scss">
.sidebar-stories-main {
  box-shadow: 0 10px 20px 0 rgba(0, 0, 0, 0.05);
  background: #fff;
  border-radius: 8px;
  .v-list {
    border-radius: 8px;
  }
}
</style>
