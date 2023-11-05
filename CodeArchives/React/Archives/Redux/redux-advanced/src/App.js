import Cart from './components/Cart/Cart';
import Layout from './components/Layout/Layout';
import Products from './components/Shop/Products';
import { useSelector, useDispatch } from 'react-redux';
import { useEffect, useState, useCallback, Fragment } from 'react';
import { uiActions } from './store/index';
import Notification from './components/UI/Notification';

function App() {
  const showCart = useSelector(state => state.ui.isCartVisible);
  const notification = useSelector(state=> state.ui.notification);
  const cartItemsCount = useSelector(state => state.ui.count);
  const [items, setItems] = useState([]);
  const dispatch = useDispatch();
  const fetchCartItems = useCallback(async () => {
    const response = await fetch('http://localhost:8000/cart/');
    const data = await response.json();
    let count = 0;
    data.map(item => count += item.quantity);
    dispatch(uiActions.Count(count));
    setItems(data);
  }, [dispatch]);
  useEffect(() => {
    fetchCartItems();
  }, [cartItemsCount, fetchCartItems]);

  return (
    <Fragment>
      {notification && <Notification status={notification.status} title={notification.title} message={notification.message} /> }
      <Layout>
        {showCart && <Cart items={items} />}
        <Products />
      </Layout>
    </Fragment>

  );
}

export default App;

