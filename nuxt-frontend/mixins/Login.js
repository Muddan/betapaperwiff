/* eslint-disable no-console */
import firebase from 'firebase'
import 'firebase/auth'
export const Login = {
  methods: {
    google(name) {
      const provider = new firebase.auth.GoogleAuthProvider()
      firebase
        .auth()
        .signInWithPopup(provider)
        .then(async res => {
          // eslint-disable-next-line no-console
          await firebase
            .auth()
            .currentUser.getIdToken(/* forceRefresh */ true)
            .then(idToken => {
              this.$store.dispatch('user/authenticate', { idToken: idToken })
            })

          if (res.additionalUserInfo.isNewUser) {
            this.$router.push('/profile')
          }
          this.$store.commit('ui/SET_SHOW_POPUP', {
            status: false,
            component: ''
          })
        })
    },
    twitter(name) {
      const provider = new firebase.auth.TwitterAuthProvider()
      firebase
        .auth()
        .signInWithPopup(provider)
        .then(async res => {
          await firebase
            .auth()
            .currentUser.getIdToken(/* forceRefresh */ true)
            .then(idToken => {
              this.$store.dispatch('user/authenticate', { idToken: idToken })
            })
          if (res.additionalUserInfo.isNewUser) {
            this.$router.push('/profile')
          }
          this.$store.commit('ui/SET_SHOW_POPUP', {
            status: false,
            component: ''
          })
        })
        .catch(error => {
          if (error.code === 'auth/invalid-credential') {
            this.$store.dispatch('notification/error', {
              title: 'Try again!',
              message: 'Something went wrong.'
            })
            return
          }
          this.$store.dispatch('notification/error', {
            title: '',
            message: error.message
          })
        })
    },
    emailSignUp(email, password, fullName) {
      firebase
        .auth()
        .createUserWithEmailAndPassword(email, password)
        .then(async res => {
          await firebase
            .auth()
            .currentUser.getIdToken(/* forceRefresh */ true)
            .then(idToken => {
              this.$store.dispatch('user/authenticate', {
                idToken: idToken,
                fullName: fullName
              })
            })
          if (res.additionalUserInfo.isNewUser) {
            this.$router.push('/profile')
          }
        })
        .catch(error => {
          this.$store.dispatch('notification/error', {
            title: '',
            message: error.message
          })
        })
    },

    emailLogin(email, password) {
      firebase
        .auth()
        .signInWithEmailAndPassword(email, password)
        .then(async res => {
          const userId = await firebase.auth().currentUser.uid
          await firebase
            .auth()
            .currentUser.getIdToken(/* forceRefresh */ true)
            .then(idToken => {
              this.$store.dispatch('user/authenticateEmailUser', userId)
            })
          this.$store.commit('ui/SET_SHOW_POPUP', {
            status: false,
            component: ''
          })
        })
        .catch(error => {
          if (error.code === 'auth/user-not-found') {
            this.$store.dispatch('notification/info', {
              title: '',
              message:
                'No account with the email ID exists, please create an account'
            })
          }
          if (error.code === 'auth/invalid-email') {
            this.$store.dispatch('notification/error', {
              title: '',
              message: 'Invalid email ID, please try again.'
            })
          }
          if (error.code === 'auth/wrong-password') {
            this.$store.dispatch('notification/error', {
              title: '',
              message:
                'You have entered an incorrect password, please try again.'
            })
          }
        })
    },
    resetPassword(email) {
      firebase
        .auth()
        .sendPasswordResetEmail(email)
        .then(res => {
          this.$store.dispatch('notification/success', {
            title: '',
            message: 'Please check your mail for password reset link.'
          })
          this.$store.commit('ui/SET_SHOW_POPUP', {
            status: false,
            component: ''
          })
        })
    }
  }
}
