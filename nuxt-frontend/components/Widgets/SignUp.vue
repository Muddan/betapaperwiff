<template>
  <div v-if="!isSignedIn" class="signup-popup">
    <div class="join-us-content">
      <div class="header">
        <h3 class="pop-up-title">Join Paperwiff</h3>
        <div class="desc">
          {{ formText }} in to get personalized story recommendations, follow
          authors and topics you love, and interact with stories.
        </div>
      </div>
      <div class="social-btn">
        <v-btn outline round @click="twitter()">
          {{ formText }} with Twitter
          <img src="https://img.icons8.com/color/25/000000/twitter.png" />
        </v-btn>
        <v-btn outline round @click="google()">
          {{ formText }} with Google
          <img
            class="icon-img"
            src="https://img.icons8.com/color/25/000000/google-logo.png"
          />
        </v-btn>
      </div>

      <div v-if="isForgotPassword" class="forgot-password-form">
        <v-text-field
          v-model="email"
          :rules="emailRules"
          label="E-mail"
          prepend-icon="email"
          required
        ></v-text-field>
        <v-btn color="#2e2e2e" dark @click="resetPassword(email)">
          Send Reset Link
        </v-btn>
        <v-btn
          outline
          color="#2e2e2e"
          dark
          @click="
            () => {
              isForgotPassword = false
            }
          "
        >
          Cancel
        </v-btn>
      </div>
      <div v-else class="form-wrapper">
        <div class="signup-form-wrapper">
          <v-form
            ref="sign-up-form"
            v-model="valid"
            class="sign-up-form"
            lazy-validation
          >
            <v-scroll-y-transition>
              <v-text-field
                v-if="showSignUp"
                v-model="fullName"
                :rules="nameRules"
                prepend-icon="account_circle"
                label="Full Name"
              ></v-text-field>
            </v-scroll-y-transition>

            <v-text-field
              v-model="email"
              :rules="emailRules"
              label="E-mail"
              prepend-icon="email"
              required
            ></v-text-field>

            <v-text-field
              v-model="password"
              :append-icon="show1 ? 'visibility' : 'visibility_off'"
              :rules="[rules.required, rules.min]"
              :type="show1 ? 'text' : 'password'"
              name="input-10-1"
              label="Password"
              prepend-icon="lock"
              hint="At least 8 characters"
              counter
              @click:append="show1 = !show1"
            ></v-text-field>

            <!--
              <v-checkbox
                v-model="checkbox"
                :rules="[v => !!v || 'You must agree to continue!']"
                label="Do you agree?"
                required
              ></v-checkbox> -->

            <v-btn color="#2e2e2e" dark @click="validate">
              {{ formText }}
            </v-btn>
            <span v-if="!showSignUp" class="forgot-password">
              Forgot
              <strong class="link-text" @click="forgotPassword()"
                >password ?</strong
              >
            </span>
            <div v-show="!showSignUp" class="form-switcher">
              <span>
                No account?
                <strong class="link-text" @click="createAccount()"
                  >Create one.</strong
                >
              </span>
            </div>
            <div v-show="showSignUp" class="form-switcher">
              <span>
                Aready have an account?
                <strong class="link-text" @click="loginAccount()"
                  >Take me to login</strong
                >
              </span>
            </div>
            <v-subheader class="notice-text">
              <span> Click “{{ formText }}” above to accept Paperwiff's</span>
              <span class="accepting-links">
                <strong class="link-text">
                  <nuxt-link to="/privacy-policy"
                    >Privacy Policy</nuxt-link
                  ></strong
                >
              </span>
            </v-subheader>
          </v-form>
        </div>
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
  data: () => ({
    showSignUp: false,
    formText: 'Sign In',
    show1: false,
    valid: true,
    fullName: '',
    password: '',
    nameRules: [v => !!v || 'Name is required'],
    email: '',
    emailRules: [
      v => !!v || 'E-mail is required',
      v => /.+@.+/.test(v) || 'E-mail must be valid'
    ],
    rules: {
      required: value => !!value || 'Required.',
      min: v => v.length >= 8 || 'Min 8 characters',
      emailMatch: () => "The email and password you entered don't match"
    },
    checkbox: false,
    isForgotPassword: false
  }),
  computed: {
    ...mapGetters({
      isSignedIn: 'user/isSignedIn'
    })
  },
  methods: {
    validate() {
      if (this.formText === 'Sign Up') {
        this.emailSignUp(this.email, this.password, this.fullName)
      } else {
        this.emailLogin(this.email, this.password)
      }
    },
    createAccount() {
      this.formText = 'Sign Up'
      this.showSignUp = true
    },
    forgotPassword() {
      this.isForgotPassword = true
    },
    loginAccount() {
      this.showSignUp = false
      this.formText = 'Sign In'
    }
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
    // background: url('~assets/signup/popupbg.jpg');
    // background-size: cover;
    // background-origin: padding-box;
    // background-repeat: no-repeat;
    // background-position: left center;
    box-sizing: border-box;
    padding: 50px;
    text-align: center;
    position: relative;
    @media (max-width: 768px) {
      padding: 30px 20px;
    }
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
          font-size: 14px;
        }
      }
    }
    .v-btn {
      text-transform: capitalize;
    }
    .social-btn {
      display: flex;
      align-items: center;
      justify-content: center;
      flex-direction: column;
      @media (max-width: 768px) {
        flex-direction: column;
      }
      .icon-img {
        padding: 0 5px;
      }
    }
  }
  .footer-header {
    .v-subheader {
      justify-content: center;
    }
  }
  .form-wrapper {
    .sign-up-form {
      width: 50%;
      margin: auto;
      @media (max-width: 768px) {
        width: 100%;
      }
    }
    .notice-text {
      display: flex;
      flex-direction: column;
      box-sizing: border-box;
      padding: 10px 0;
    }
    .form-switcher {
      box-sizing: border-box;
      padding: 10px 0;
    }
    .link-text {
      cursor: pointer;
    }
  }
}
</style>
