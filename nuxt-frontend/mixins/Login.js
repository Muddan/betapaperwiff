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
              this.$store.dispatch('user/authenticate', idToken)
            })
          if (res.additionalUserInfo.isNewUser) {
            this.$router.push('/profile')
          }
        })
    },
    twitter(name) {
      const provider = new firebase.auth.TwitterAuthProvider()
      firebase
        .auth()
        .signInWithPopup(provider)
        .then(res => {
          firebase
            .auth()
            .currentUser.getIdToken(/* forceRefresh */ true)
            .then(function(idToken) {
              // eslint-disable-next-line no-console
              console.log(idToken)
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
    }
  }
}
