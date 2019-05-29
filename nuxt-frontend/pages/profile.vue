<template>
  <div class="profile-content-main">
    <v-container>
      <v-window v-model="onboarding" class="window-container">
        <v-window-item class="follow-tags-main">
          <v-card class="form-card">
            <header class="form-header">
              <h3 class="header-title">
                Please select 3 topics, so that we can personalized your feed :)
              </h3>
            </header>
            <v-layout row wrap>
              <v-flex
                v-for="(tag, index) in storyTagsAvailable"
                :key="index"
                xs12
                sm4
                md3
              >
                <v-card
                  flat
                  ripple
                  tile
                  class="tag-card-main"
                  :class="{ active: tag.status }"
                  @click="followTag(tag, $event)"
                >
                  <v-list-tile class="tag-list align-center">
                    <span class="tagname"> # {{ tag.name }} </span>
                  </v-list-tile>
                </v-card>
              </v-flex>
            </v-layout>
          </v-card>
        </v-window-item>
        <v-window-item>
          <v-card class="form-card">
            <div class="form-container">
              <header class="form-header">
                <h3 class="header-title">Tell us about yourself</h3>
              </header>
              <v-form ref="profileUpdate" class="profile-form" lazy-validation>
                <v-layout row wrap class="form-content">
                  <v-flex xs12 md6 class="input-control">
                    <v-text-field
                      v-model="user.location"
                      label="Location"
                      class="input"
                      name="location"
                      hint="Ex: 'Bangalore'"
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12 md6 class="input-control">
                    <v-text-field
                      v-model="user.skills"
                      label="Skills"
                      class="input"
                      name="location"
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12 md6 class="input-control">
                    <v-text-field
                      v-model="user.languages"
                      label="Languages"
                      class="input"
                      name="location"
                      hint="Ex: 'kannada', 'hindi'"
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12 md6 class="input-control">
                    <v-text-field
                      v-model="user.availableFor"
                      label="Available For"
                      class="input"
                      name="location"
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs12 md6 class="input-control">
                    <v-textarea
                      v-model="user.about"
                      label="About"
                      name="bio"
                      hint="Enter about yourself."
                    ></v-textarea>
                  </v-flex>

                  <v-flex xs12 class="input-control">
                    <v-btn dark color="#337fb5" @click="validate">Submit</v-btn>
                  </v-flex>
                </v-layout>
              </v-form>
            </div>
          </v-card>
        </v-window-item>
      </v-window>

      <v-card-actions class="justify-space-between">
        <v-btn flat @click="prev">
          <v-icon>fa fa-chevron-left</v-icon>
        </v-btn>
        <v-btn flat @click="next">
          <v-icon>fa fa-chevron-right</v-icon>
        </v-btn>
      </v-card-actions>
    </v-container>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
import _ from 'lodash'
export default {
  // middleware: 'auth',

  data() {
    return {
      followingTags: [],
      length: 3,
      onboarding: 0,
      user: {
        about: '',
        location: '',
        skills: '',
        languages: '',
        availableFor: ''
      }
    }
  },
  computed: {
    ...mapGetters({
      storyTagsAvailable: 'stories/availableTags',
      isSignedIn: 'user/isSignedIn',
      currentUser: 'user/currentUser'
    }),
    currentTags() {
      return this.storyTagsAvailable
    }
  },
  methods: {
    next() {
      this.onboarding =
        this.onboarding + 1 === this.length ? 0 : this.onboarding + 1
    },
    prev() {
      this.onboarding =
        this.onboarding - 1 < 0 ? this.length - 1 : this.onboarding - 1
    },
    randomColor() {
      return '#' + Math.floor(Math.random() * 16777215).toString(16)
    },
    followTag(tag, event) {
      // eslint-disable-next-line no-console
      if (this.followingTags.includes(tag)) {
        event.target.classList.remove('active')
        this.followingTags = this.followingTags.filter(item => {
          return item !== tag
        })
      } else if (this.followingTags.length <= 3) {
        event.target.classList.add('active')
        this.followingTags.push(tag)
        if (this.followingTags.length >= 3) {
          this.next()
        }
      }
    },
    validate() {
      const currentUserData = _.cloneDeep(this.currentUser)
      const updatedUserData = _.merge(currentUserData, this.user)
      this.$store
        .dispatch('user/updateUserDetails', updatedUserData)
        .then(res => {
          if (res) {
            this.$store.dispatch('notification/success', {
              title: 'Saved!',
              message:
                'we have saved your information, you can change it anytime'
            })
            window.location.replace('/')
          } else {
            this.$store.dispatch('notification/error', {
              title: 'Oh Snap!',
              message:
                'Something went wrong while saving your data, please try again'
            })
          }
        })
      this.followingTags.map(tag => {
        this.$store.dispatch('stories/addToFollowingFilters', tag)
      })
    }
  }
}
</script>
<style lang="scss">
.profile-content-main {
  max-width: 1400px;
  margin: auto;
  .tag-card-main {
    cursor: pointer;
    margin: 10px;
    background: #fcfcfc;
    &:hover {
      background: rgb(219, 241, 255);
    }
    &.active {
      background: rgb(219, 241, 255);
    }
    .tag-list {
      text-align: center;
    }
    .tag-list,
    .tagname {
      pointer-events: none;
      width: 100%;
      font-size: 14px;
    }
  }
  .follow-tags-main {
    .profile-header {
      text-align: center;
      box-sizing: border-box;
      padding: 0 20px 20px;
      font-size: 20px;
      @media (max-width: 768px) {
        font-size: 18px;
      }
    }
  }
  .form-container {
    .input-control {
      padding: initial 10px;
    }
  }
  .form-card {
    margin-top: 20px;
    padding: 20px;
    border-radius: 8px;
  }
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
</style>
