import './App.css';
import Home from './components/Home';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img width="100" src="/logo.png" alt="logo" />
        <h1>eTrash</h1>
      </header>
      <section>
        <Home />
      </section>
    </div>
  );
}

export default App;
