import React, { useState } from 'react';
import './App.css';
import Home from './components/Home';
import { auth } from './firebase-config';
import { SignIn, SignOut } from './components/Auth';
import { useAuthState } from 'react-firebase-hooks/auth';

function App() {

  const [user, loading, error] = useAuthState(auth);
  
  return (
    <div className="App">
      <header className="App-header">
        <img width="100" src="/logo.png" alt="logo" />
        <h1>eTrash</h1>
        { user && <SignOut /> }
      </header>
      <section>
        { user ? <Home /> : <SignIn /> }
      </section>
    </div>
  );
}

export default App;
