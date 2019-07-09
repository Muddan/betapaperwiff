<template>
  <div class="author-info">
    <v-container>
      <v-layout justify-center main-layout wrap>
        <v-flex sm8 xs12 info-main>
          <router-link
            class="user-link"
            :to="{
              path: '/a/' + author.userName
            }"
          >
            <div class="user-img">
              <v-avatar size="100px">
                <img v-if="author.userImage" :src="author.userImage" />
                <v-avatar v-else size="80px" color="blue">
                  <span v-if="author.firstName" class="white--text ">{{
                    author.firstName[0]
                  }}</span>
                </v-avatar>
              </v-avatar>
            </div>
            <div class="user-info">
              <h3 class="name">{{ author.firstName }} {{ author.lastName }}</h3>

              {{ author.userName }}
              <div class="user-bio">
                {{ author.about }}
              </div>
            </div>
          </router-link>
        </v-flex>
        <v-flex sm4 xs12 class="follow-flex"> <slot /> </v-flex>
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
  margin: 0 0 30px 0;
  width: 100%;
  margin: auto;
  @media (max-width: 768px) {
    width: 100%;
  }

  .info-main {
    display: flex;
    border-right: 1px solid #c2c2c2;
    @media (max-width: 768px) {
      border: none;
    }
    a {
      display: flex;
      align-items: center;
    }
    @media (max-width: 768px) {
      flex-direction: column;
      a {
        padding-bottom: 20px;
        flex-direction: column;
      }
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
  .follow-flex {
    justify-content: center;
    align-items: center;
    display: flex;
  }
}
</style>
