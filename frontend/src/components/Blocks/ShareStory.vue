<template>
  <social-sharing :url="url" inline-template>
    <div class="links-main">
      <v-list>
        <!-- <v-list-tile-title>Share</v-list-tile-title> -->
        <v-list-tile>
          <network network="facebook">
            <v-icon size="24px">fab fa-facebook</v-icon>
          </network>
        </v-list-tile>
        <v-list-tile>
          <network network="linkedin">
            <v-icon size="24px">fab fa-twitter</v-icon>
          </network>
        </v-list-tile>
        <v-list-tile>
          <network network="reddit">
            <v-icon size="24px">fab fa-instagram</v-icon>
          </network>
        </v-list-tile>
        <v-list-tile>
          <network network="twitter">
            <v-icon size="24px">fab fa-linkedin</v-icon>
          </network>
        </v-list-tile>
      </v-list>
    </div>
  </social-sharing>
</template>

<script>
export default {
  name: "ShareStory",
  props: {
    url: {
      type: String
    }
  }
};
</script>
<style lang="scss">
.links-main {
  border-radius: 8px;
  background: #fff;
  overflow: hidden;
  position: sticky;
  top: 100px;
  .v-list__tile__title {
    text-align: center;
  }
  .v-list__tile {
    justify-content: center;
    cursor: pointer;
  }
}
</style>

