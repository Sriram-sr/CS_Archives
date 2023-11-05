import Card from '../UI/Card';
import classes from './Cart.module.css';
import CartItem from './CartItem';
// import { useSelector } from 'react-redux';

const Cart = (props) => {
  // const items = useSelector(state => state.cart.items);
  const itemsTodisplay = props.items.map(item => <CartItem key={item.custom_id} id={item.custom_id} title={item.name} quantity={item.quantity} total={item.total_price} price={item.price} />);
  return (
    <Card className={classes.cart}>
      <h2>Your Shopping Cart</h2>
      <ul>
        {itemsTodisplay}
        {/* <CartItem
          item={{ title: 'Test Item', quantity: 3, total: 18, price: 6 }}
        /> */}
      </ul>
    </Card>
  );
};

export default Cart;
