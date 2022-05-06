import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';
import 'firebase/compat/firestore';
import 'firebase/compat/storage';

const firebaseConfig = {
  apiKey: 'AIzaSyBqC2NoH0CCs-FNQfOcfipdaKOR6pmxGtg',
  authDomain: 'nextfire-f38b2.firebaseapp.com',
  projectId: 'nextfire-f38b2',
  storageBucket: 'nextfire-f38b2.appspot.com',
  messagingSenderId: '169065203104',
  appId: '1:169065203104:web:4fca4cc9c11c4b2e7c10c5',
};

if (!firebase.apps.length) {
  firebase.initializeApp(firebaseConfig);
}

export const auth = firebase.auth();
export const firestore = firebase.firestore();
export const storage = firebase.storage();
