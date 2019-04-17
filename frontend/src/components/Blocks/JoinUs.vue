<template>
  <div class="join-us">
    <div class="join-us-content">
      <div class="header">
        <v-subheader>Join Paperwiff</v-subheader>
      </div>
      <v-btn outline round>
        Sign in with Twitter
        <v-icon size="18px" dark right>fab fa-twitter</v-icon>
      </v-btn>
      <v-btn @click="signIn" outline round>
        Sign in with Google
        <v-icon size="18px" dark right>fab fa-google</v-icon>
      </v-btn>
    </div>
  </div>
</template>

<script>
export default {
  name: "JoinUs",
  mounted() {
    window.gapi.load("auth2", () => {
      const auth2 = window.gapi.auth2.init({
        client_id:
          "430441876577-gpsarrij27132ir90dqb493hanfrn0og.apps.googleusercontent.com"
      });
    });
  },
  methods: {
    signIn() {
      var auth2 = window.gapi.auth2.getAuthInstance();
      auth2.signIn().then(
        function() {
          var profile = auth2.currentUser.get().getBasicProfile();
          let user = {
            user_id: profile.getId(),
            first_name: profile.getGivenName(),
            last_name: profile.getFamilyName(),
            username: profile.getGivenName(),
            email: profile.getEmail()
          };
          this.$store.dispatch("User/loginUser", user);
        }.bind(this)
      );
    }
  }
};
</script>
<style lang="scss">
.join-us {
  box-sizing: border-box;
  padding: 10px 0;
  .join-us-content {
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

