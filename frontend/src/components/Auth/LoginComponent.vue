<template>
  <div class="login">
    <div class="form-container">
      <v-form class="form" ref="signupform" v-model="valid" lazy-validation>
        <div class="form-content">
          <div class="form-header">
            <header>
              <h2 class="ftitle">paperWiff</h2>
              <p class="desc">welcome to our community</p>
            </header>
          </div>
          <div class="input-control">
            <v-text-field
              class="input"
              v-model="name"
              :counter="10"
              :rules="nameRules"
              placeholder="Name"
              solo
            ></v-text-field>
          </div>
          <div class="input-control">
            <v-text-field
              class="input"
              v-model="password"
              placeholder="Password"
              :append-icon="showPassword ? 'visibility' : 'visibility_off'"
              :rules="[rules.required, rules.min]"
              :type="showPassword ? 'text' : 'password'"
              name="input-10-1"
              hint="At least 8 characters"
              counter
              solo
              @click:append="showPassword = !showPassword"
            ></v-text-field>
          </div>
          <div class="input-control">
            <v-text-field
              class="input"
              v-model="email"
              :rules="emailRules"
              placeholder="E-mail"
              solo
              required
            ></v-text-field>
          </div>
          <div class="input-control">
            <v-btn dark color="#114b5f" @click="validate">Let's Go</v-btn>
          </div>
        </div>
      </v-form>
      <div class="other-content">
        <div class="input-control">
          <v-btn outline color="#114b5f">SignIn</v-btn>
        </div>
        <div class="social-text">
          <span class="subheading">In case you can not remember.</span>
        </div>
        <div class="social-logins">
          <div class="social">
            <v-btn @click="signIn" fab dark small color="#114b5f">
              <v-icon dark>fab fa-google</v-icon>
            </v-btn>
          </div>
          <div class="social">
            <v-btn fab dark small color="#114b5f">
              <v-icon dark>fab fa-facebook</v-icon>
            </v-btn>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "LoginComponent",
  data() {
    return {
      valid: true,
      showPassword: false,
      name: "",
      nameRules: [
        v => !!v || "Name is required",
        v => (v && v.length <= 10) || "Name must be less than 10 characters"
      ],
      password: "",
      email: "",
      emailRules: [
        v => !!v || "E-mail is required",
        v => /.+@.+/.test(v) || "E-mail must be valid"
      ],
      password: "",
      rules: {
        required: value => !!value || "Required.",
        min: v => v.length >= 8 || "Min 8 characters",
        emailMatch: () => "The email and password you entered don't match"
      }
    };
  },
  mounted() {
    window.gapi.load("auth2", () => {
      const auth2 = window.gapi.auth2.init({
        client_id:
          "430441876577-gpsarrij27132ir90dqb493hanfrn0og.apps.googleusercontent.com"
      });
    });
  },

  methods: {
    validate() {
      if (this.$refs.signupform.validate()) {
        this.snackbar = true;
        let user = {
          username: "@" + this.name,
          password: this.password,
          email: this.email
        };
        this.$router.push(`/a/${user.username}`);
      }
    },
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
.input-control {
  max-width: 450px;
  margin: 20px auto;
  padding: 10px 0;
  .v-btn {
    width: 96%;
  }
}
.input {
  padding: 10px;
  border: 1px solid #2e2e2e;
  box-shadow: 8px 8px 0 #2e2e2e;
  width: 320px;
  height: 50px;
  .v-text-field__details {
    margin: 10px 0;
  }
}
.form-header {
  .ftitle {
    font-size: 46px;
    text-transform: capitalize;
    font-family: "Marck Script", cursive;
    font-weight: normal;
  }
  .desc {
    font-size: 18px;
    text-transform: lowercase;
  }
}
.login {
  width: 100%;
  height: 100%;

  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;

  box-sizing: border-box;
  padding: 20px 0;
  &::after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url(https://visme.co/blog/wp-content/uploads/2017/07/50-Beautiful-and-Minimalist-Presentation-Backgrounds-033.jpg);
    background-size: cover;
  }
  .form-container {
    max-width: 1200px;
    margin: 100px auto auto auto;
    z-index: 1;
  }
}
.other-content {
  .input-control {
    text-align: center;
    .v-btn {
      width: 50%;
    }
  }
  .social-text {
    text-align: center;
    box-sizing: border-box;
    padding: 10px 0;
  }
  .social-logins {
    display: flex;
    justify-content: center;
  }
}
</style>
