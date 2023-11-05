import Welcome from "./pages/Welcome";
import Product from "./pages/Products";
import { Redirect, Route } from 'react-router-dom';
import MainHeader from "./components/MainHeader";

function App() {
  return (
    <div>
      <MainHeader />
      <main>
        <Route path='/'>
          <Redirect to='/home' />
        </Route>
        <Route path='/home'>
          <Welcome />
        </Route>
        <Route path='/products'>
          <Product />
        </Route>
      </main>
    </div>
  );
}

export default App;
