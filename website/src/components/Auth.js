import React from 'react'
import { firebase, auth } from '../firebase-config';

function SignIn() {

  const signInWithGoogle = () => {
    const provider = new firebase.auth.GoogleAuthProvider();
    auth.signInWithPopup(provider)
      .then(result => {
        const user = result.user;
        console.log(user);
      })
      .catch(error => {
        console.log(error);
      })
  }

  return (
    <>
      <button onClick={signInWithGoogle}>Sign in</button>
    </>
  )
}

function SignOut() {

  const signOut = () => {
    auth.signOut()
      .then(() => {
        console.log('signed out');
      })
      .catch(error => {
        console.log(error);
      })
  }

  return (
    <>
      <button onClick={signOut}>Sign out</button>
    </>
  )
}

export { SignIn, SignOut };