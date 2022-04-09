import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';
import 'firebase/compat/storage';
import 'firebase/compat/firestore';

firebase.initializeApp({
  apiKey: "AIzaSyBqtHyA0Dmh8l0prbsKmcF5atbIwGRZiew",
  authDomain: "etrash-35222.firebaseapp.com",
  projectId: "etrash-35222",
  storageBucket: "etrash-35222.appspot.com",
  messagingSenderId: "873316243260",
  appId: "1:873316243260:web:f006f5e6cd3d8a06a0b039",
  measurementId: "G-K5ZLCNS4KE"
})

const auth = firebase.auth();
const storage = firebase.storage();
const firestore = firebase.firestore();

export { firebase, auth, storage, firestore };

/*

authentication for each user and their eTrash
firestore document database holds 'historical garbage'
storage holds images of garbage, is referenced by firestore

*/