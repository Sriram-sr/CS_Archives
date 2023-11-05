import classes from './CartButton.module.css';
import { uiActions } from '../../store/index';
import { useDispatch, useSelector } from 'react-redux';

const CartButton = (props) => {
  const dispatch = useDispatch();
  // const itemsInCart = useSelector(state=> state.cart.totalQuantity);
  const itemsInCart = useSelector(state=> state.ui.count);
  const clickHandler = () => {
    dispatch(uiActions.toggle());
  };

  return (
    <button className={classes.button} onClick={clickHandler}>
      <span>My Cart</span>
      <span className={classes.badge}>{itemsInCart}</span>
    </button>
  );
};

export default CartButton;
