<template>
  <div v-if="!isSignedIn" class="join-us">
    <div class="join-us-content">
      <div class="header">
        <v-subheader>Join Paperwiff</v-subheader>
      </div>
      <!-- <v-btn outline round @click="authenticate('twitter')">
        Sign in with Twitter
        <v-icon size="18px" dark right>fab fa-twitter</v-icon>
      </v-btn> -->
      <v-btn outline round @click="authenticate('google')">
        Sign in with Google
        <v-icon size="18px" dark right>fab fa-google</v-icon>
      </v-btn>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'JoinUs',
  computed: {
    ...mapGetters({
      isSignedIn: 'user/isSignedIn'
    })
  },
  methods: {
    authenticate: function(provider) {
      this.$auth.authenticate(provider).then(authResponse => {
        if (authResponse) {
          this.$store.dispatch('user/loginUser', authResponse.data)
          this.$store.dispatch('notification/success', {
            title: 'Logged In',
            message: 'Successfully logged in to paperwiff'
          })
          if (authResponse.data.newUser) {
            this.$router.push('/profile')
          }
        } else {
          this.$store.dispatch('notification/error', {
            title: 'Failed',
            message: 'Something went wrong, please try again'
          })
        }
      })
    }
  }
}
</script>
<style lang="scss">
.join-us {
  box-sizing: border-box;
  padding: 10px 0;
  .join-us-content {
    background: #fff;
    border-radius: 8px;
    border: 1px solid #3e3e3e;
    border-bottom: 4px solid #3e3e3e;
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
  }
}
</style>
