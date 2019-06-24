import firebase from 'firebase'
import 'firebase/app'
// Initialize Firebase

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: 'AIzaSyDbTsqs5Q-xhwCKh4OGuUIYGsCKMj5zKSg',
  authDomain: 'paperwiff.firebaseapp.com',
  databaseURL: 'https://paperwiff.firebaseio.com',
  projectId: 'paperwiff',
  storageBucket: 'paperwiff.appspot.com',
  messagingSenderId: '430441876577',
  appId: '1:430441876577:web:b977ab9b0fe0607b'
}

// DEV ACCOUNT
// const firebaseConfig = {
//   apiKey: 'AIzaSyAzehTY4NzaBI_Y5VvbqclGA-5OPxoOEUU',
//   authDomain: 'paperwiff-dev.firebaseapp.com',
//   databaseURL: 'https://paperwiff-dev.firebaseio.com',
//   projectId: 'paperwiff-dev',
//   storageBucket: 'paperwiff-dev.appspot.com',
//   messagingSenderId: '645001837531',
//   appId: '1:645001837531:web:96544d74fdf976c3'
// }
// Initialize Firebase
if (!firebase.apps.length) {
  firebase.initializeApp(firebaseConfig)
}
