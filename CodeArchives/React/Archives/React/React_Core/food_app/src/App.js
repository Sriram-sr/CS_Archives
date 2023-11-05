import { useState } from "react";
import Cart from "./Components/Cart/Cart";
import Header from "./Components/Layout/Header";
import Meals from "./Components/Meals/Meals";
import CartProvider from "./store/cart-provider";

function App() {
  const [noOverlay, setOverlay] = useState(false);

  const hideCart = () => {
    setOverlay(false);
  }

  const showCart = () => {
    setOverlay(true);
  }

  return (
    <CartProvider>
      {noOverlay && <Cart closeHandler={hideCart} />}
      <Header showCart={showCart} />
      <main>
        <Meals />
      </main>
      </CartProvider>
  );
}

export default App;
