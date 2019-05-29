<template>
  <div v-if="!isSignedIn" class="join-us">
    <div class="join-us-content">
      <div class="header">
        <v-subheader>Join Paperwiff</v-subheader>
      </div>
      <div class="social-btn">
        <v-btn outline round @click="twitter()">
          Sign in with Twitter
          <img src="https://img.icons8.com/color/25/000000/twitter.png" />
        </v-btn>
        <v-btn outline round @click="google()">
          Sign in with Google
          <img
            class="icon-img"
            src="https://img.icons8.com/color/25/000000/google-logo.png"
          />
        </v-btn>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { Login } from '@/mixins/Login'
export default {
  name: 'JoinUs',
  mixins: [Login],
  computed: {
    ...mapGetters({
      isSignedIn: 'user/isSignedIn'
    })
  }
}
</script>
<style lang="scss">
.join-us {
  box-sizing: border-box;
  .join-us-content {
    background: #fff;
    border-radius: 8px;
    // border: 1px solid #3e3e3e;
    border-bottom: 4px solid #1f1f1f;
    box-shadow: 0 10px 20px 0 rgba(0, 0, 0, 0.05);

    box-sizing: border-box;
    padding: 10px 0;
    padding-bottom: 25px;
    text-align: center;
    .header {
      width: 100%;
      text-align: center;
      .v-subheader {
        justify-content: center;
        font-size: 18px;
      }
    }
    .v-btn {
      text-transform: lowercase;
    }
    .social-btn {
      display: flex;
      align-items: center;
      flex-direction: column;
      justify-content: center;
      .icon-img {
        padding: 0 5px;
      }
    }
  }
}
</style>
