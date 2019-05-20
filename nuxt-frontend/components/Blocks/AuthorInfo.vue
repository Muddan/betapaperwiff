<template>
  <div class="author-info">
    <v-container>
      <v-layout justify-center main-layout>
        <v-flex sm6 xs12 info-main>
          <div class="user-img">
            <v-avatar size="80px">
              <img :src="author.userImage" :alt="author.userName" />
            </v-avatar>
          </div>
          <div class="user-info">
            <h3 class="name">{{ author.firstName }} {{ author.lastName }}</h3>
            <router-link
              class="user-link"
              :to="{
                path: '/a/' + author.userName
              }"
            >
              {{ author.userName }}
            </router-link>
            <div class="user-bio">
              {{ author.about }}
            </div>
          </div>
        </v-flex>
        <v-flex>
          <!-- <v-btn outline color="indigo">Follow</v-btn> -->
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>
<script>
export default {
  name: 'UserInfo',
  props: {
    author: {
      type: Object,
      default: null
    }
  }
}
</script>
<style lang="scss" scoped>
.author-info {
  background: #fff;

  box-sizing: border-box;
  padding: 10px;
  margin: 0 0 30px 0;
  border-top: 1px solid #2e2e2e;
  width: 80%;
  margin: auto;
  @media (max-width: 768px) {
    width: 100%;
  }

  .info-main {
    display: flex;
    border-right: 1px solid #c2c2c2;
    @media (max-width: 768px) {
      flex-direction: column;
    }
    .user-info {
      padding: 0 10px;
    }
  }

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
