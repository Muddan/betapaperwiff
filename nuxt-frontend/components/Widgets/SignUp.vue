<template>
  <div v-if="!isSignedIn" class="signup-popup">
    <div class="join-us-content">
      <div class="header">
        <h3 class="pop-up-title">Join Paperwiff</h3>
        <div class="desc">
          Sign in to get personalized story recommendations, follow authors and
          topics you love, and interact with stories.
        </div>
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
<style lang="scss" scoped>
.signup-popup {
  box-sizing: border-box;
  text-align: center;
  background: #fff;
  border-radius: 8px;
  .join-us-content {
    // background: url('~assets/signup/popup.jpeg');
    // background-size: 50%;
    // background-origin: padding-box;
    // background-repeat: no-repeat;
    // background-position: left center;
    box-sizing: border-box;
    padding: 50px;
    text-align: center;
    position: relative;
    .header {
      width: 100%;
      text-align: center;
      box-sizing: border-box;
      padding: 10px;
      .pop-up-title {
        font-size: 26px;
      }
      .desc {
        max-width: 80%;
        margin: auto;
        opacity: 0.8;
        box-sizing: border-box;
        padding: 10px 0;
        font-size: 18px;
        @media (max-width: 768px) {
          max-width: 100%;
          font-size: 16px;
        }
      }
    }
    .v-btn {
      text-transform: lowercase;
    }
    .social-btn {
      display: flex;
      align-items: center;
      justify-content: center;
      @media (max-width: 768px) {
        flex-direction: column;
      }
      .icon-img {
        padding: 0 5px;
      }
    }
  }
}
</style>
