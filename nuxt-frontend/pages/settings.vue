<template>
  <div class="settings-main">
    <v-container>
      <div class="form-header">
        <header>
          <h2 class="ftitle">Settings for your paperwiff account</h2>
        </header>
        {{ user }}
      </div>
      <v-layout wrap class="settings-content">
        <v-flex class="navigation-links" xs12 md3>
          <v-list
            v-for="(settingslist, settingindex) in settingsLists"
            :key="settingindex"
            xs12
            md12
          >
            <v-list-tile
              class="d-flex align-center"
              @click.stop="toggleSection(settingslist.title)"
            >
              <v-icon color="#337fb5" left>{{ settingslist.icon }}</v-icon>
              {{ settingslist.title }}
            </v-list-tile>
          </v-list>
        </v-flex>
        <v-flex xs12 md7>
          <v-scroll-y-transition>
            <div v-if="profileActive" class="profile-section">
              <v-card class="form-card">
                <div class="form-container">
                  <header class="form-header">
                    <h3 class="header-title">Edit your profile</h3>
                  </header>
                  <v-form
                    ref="profileUpdate"
                    v-model="valid"
                    class="profile-form"
                    lazy-validation
                  >
                    <v-layout column class="form-content">
                      <v-flex class="form-control">
                        <image-input v-model="avatar">
                          <div slot="activator">
                            <v-avatar
                              v-if="!avatar"
                              v-ripple
                              size="150px"
                              class="grey lighten-3 mb-3"
                            >
                              <span>Click to add avatar</span>
                            </v-avatar>
                            <v-avatar v-else v-ripple size="150px" class="mb-3">
                              <img :src="avatar.imageURL" alt="avatar" />
                            </v-avatar>
                          </div>
                        </image-input>
                      </v-flex>
                      <v-flex class="input-control">
                        <v-text-field
                          v-model="user.email"
                          class="input"
                          label="Email"
                          :rules="emailRules"
                          type="email"
                          name="email"
                          required
                        ></v-text-field>
                      </v-flex>
                      <v-flex class="input-control">
                        <v-text-field
                          v-model="user.userName"
                          label="Username"
                          class="input"
                          :rules="nameRules"
                          name="userName"
                        ></v-text-field>
                      </v-flex>
                      <v-flex md3 class="input-control">
                        <v-text-field
                          v-model="user.firstName"
                          label="Firstname"
                          class="input"
                          :rules="nameRules"
                          name="firstName"
                        ></v-text-field>
                      </v-flex>
                      <v-flex md3 class="input-control">
                        <v-text-field
                          v-model="user.lastName"
                          class="input"
                          :rules="nameRules"
                          label="Lastname"
                          name="lastName"
                        ></v-text-field>
                      </v-flex>
                      <v-flex class="input-control">
                        <v-textarea
                          v-model="user.about"
                          label="About"
                          name="bio"
                          hint="Enter about yourself."
                        ></v-textarea>
                      </v-flex>

                      <v-flex class="input-control">
                        <v-btn dark color="#337fb5" @click="validate"
                          >Submit</v-btn
                        >
                      </v-flex>
                    </v-layout>
                  </v-form>
                </div>
              </v-card>
            </div>
          </v-scroll-y-transition>
        </v-flex>
        <v-flex md2>
          <v-card class="profile-card">
            <div class="img-main">
              <v-img
                class="profile-img"
                src="https://cdn.vuetifyjs.com/images/cards/desert.jpg"
                aspect-ratio="2.75"
              ></v-img>
            </div>

            <v-card-title primary-title>
              <div>
                <div class="username">
                  {{ currentUser.firstName }} {{ currentUser.lastName }}
                </div>
                <p class="bio">{{ currentUser.about }}</p>
              </div>
            </v-card-title>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>
<script>
import ImageInput from '@/components/Blocks/ImageInput'
import { mapGetters } from 'vuex'
export default {
  components: {
    ImageInput
  },
  data() {
    return {
      user: {
        email: '',
        userName: '',
        firstName: '',
        lastName: '',
        about: ''
      },
      avatar: {
        imageURL: null
      },
      saving: false,
      saved: false,
      active: false,
      valid: true,
      nameRules: [
        v => !!v || 'Name is required',
        v => (v && v.length <= 10) || 'Name must be less than 10 characters'
      ],
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid'
      ],
      rules: {
        required: value => !!value || 'Required.',
        min: v => v.length >= 8 || 'Min 8 characters',
        emailMatch: () => "The email and password you entered don't match"
      },
      profileActive: true,
      settingsLists: [
        {
          title: 'Profile',
          icon: 'fa fa-users-cog'
        }
        // {
        //   title: 'Account',
        //   icon: 'account_balance_wallet'
        // },
        // {
        //   title: 'Misc',
        //   icon: 'settings_ethernet'
        // }
      ]
    }
  },
  computed: {
    ...mapGetters({
      currentUser: 'user/currentUser'
    })
  },
  watch: {
    avatar: {
      handler: function() {
        this.saved = false
      },
      deep: true
    }
  },
  beforeMount() {
    this.user = { ...this.currentUser }
    this.avatar.imageURL = this.currentUser.userImage
  },
  methods: {
    validate() {
      this.snackbar = true
      // eslint-disable-next-line no-console
      console.log(this.$refs.profileUpdate)
      if (this.$refs.profileUpdate.validate()) {
      }
    },
    toggleSection(section) {
      if (section === 'Profile') {
        this.profileActive = !this.profileActive
      }
    },
    uploadImage() {
      this.saving = true
      setTimeout(() => this.savedAvatar(), 1000)
    },
    savedAvatar() {
      this.saving = false
      this.saved = true
    }
  }
}
</script>
<style lang="scss">
.settings-main {
  max-width: 1400px;
  margin: auto;
  .settings-content {
    box-sizing: border-box;
    padding: 10px 0;
    margin-top: 20px;
    .navigation-links {
      .link-active {
        background: rgb(219, 241, 255);
      }
      .v-list {
        border-radius: 8px;
        padding: 0;
        margin: 10px 0;
        overflow: hidden;
        a {
          &:hover {
            background: rgb(219, 241, 255);
          }
        }
      }
    }
    .profile-section {
      margin: 0 20px;
      .form-card {
        padding: 20px;
        border-radius: 8px;
        .form-container {
          .form-header {
            background: #5199c3;
            box-sizing: border-box;
            padding: 20px;
            border-radius: 8px;
            color: #fff;
            transform: translateY(-40px);
            box-shadow: 0 12px 20px -10px rgba(81, 153, 195, 0.562);
            .header-title {
              font-weight: normal;
              display: inherit;
              font-size: 22px;
            }
          }
        }
      }
    }
    .profile-card {
      border-radius: 8px;
      .img-main {
        transform: translateX(25%) translateY(-40px);
        .profile-img {
          width: 100px;
          height: 100px;
          overflow: hidden;
          border-radius: 50%;
        }
      }
    }
  }
}
</style>
