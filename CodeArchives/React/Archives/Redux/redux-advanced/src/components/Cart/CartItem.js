import classes from './CartItem.module.css';
import { uiActions } from '../../store';
import { useDispatch } from 'react-redux';

const CartItem = (props) => {
  const { id, title, quantity } = props;
  const price = +props.price;
  const total = +props.total;
  const dispatch = useDispatch();
  const removeItemHandler = () => {
      // dispatch(cartActions.removeItem({
      //   id,
      //   quantity,
      //   total,
      //   price
      // }));
      const removeItem = async () => {
        const response = await fetch(`http://localhost:8000/remove/${id}`);
        dispatch(uiActions.removeCount());
        const result=await response.json()
        console.log(result);
      }
      removeItem();
  };

  const addItemHandler = () => {
    // dispatch(cartActions.addItem({
    //   id,
    //   title,
    //   quantity,
    //   total,
    //   price
    // }));
    dispatch(uiActions.addCount());
    const addItem = async () => {
      const response = await fetch(`http://localhost:8000/add/${id}/`);
      console.log(response);
    }
    addItem();
  };
  
  return (
    <li className={classes.item}>
      <header>
        <h3>{title}</h3>
        <div className={classes.price}>
          ${total.toFixed(2)}{' '}
          {/* {total} */}
          <span className={classes.itemprice}>(${price.toFixed(2)}/item)</span>
        </div>
      </header>
      <div className={classes.details}>
        <div className={classes.quantity}>
          x <span>{quantity}</span>
        </div>
        <div className={classes.actions}>
          <button onClick={removeItemHandler}>-</button>
          <button onClick={addItemHandler}>+</button>
        </div>
      </div>
    </li>
  );
};

export default CartItem;
