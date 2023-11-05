import Card from '../UI/Card';
import classes from './ProductItem.module.css';
import { useDispatch } from 'react-redux';
import { cartActions, uiActions } from '../../store/index';

const ProductItem = (props) => {
  const dispatch = useDispatch();
  const { id, title, description } = props;
  const price = +props.price;
  const AddCartHandler = (event) => {
    dispatch(cartActions.addItem({
      id,
      title,
      price
    }));
  };

  const toBackendHandler = () => {
    const addToCart = async () => {
      dispatch(uiActions.addCount());
      dispatch(uiActions.showNotification({
        status: 'success',
        title: 'Sucess!!!',
        message: 'Adding To Cart.....'
      }));
      const response = await fetch('http://localhost:8000/cart/', {
        method: 'POST',
        body: JSON.stringify({
          id: id,
          name: title,
          price: price,
          quantity: 1,
          total_price: price
        }),
        headers: {
          'Content-Type': 'application/json'
        }
      });
      dispatch(uiActions.showNotification({
        status: 'success',
        title: 'Sucess!!!',
        message: 'Added Item to Cart.....'
      }));
    };
    addToCart().catch(error=> console.log(error));
  };

  return (
    <li className={classes.item}>
      <Card>
        <header>
          <h3>{title}</h3>
          <div className={classes.price}>${price.toFixed(2)}</div>
        </header>
        <p>{description}</p>
        <div className={classes.actions}>
          <button onClick={AddCartHandler}>Add to Cart</button>
          <button onClick={toBackendHandler}>To Backend</button>
        </div>
      </Card>
    </li>
  );
};

export default ProductItem;
