import CartIcon from '../Cart/CartIcon';
import './HeaderCartButton.css';
import CartContext from '../../store/cart-context';
import { useContext } from 'react';

const HeaderCartButton = (props) => {
    const cartContext = useContext(CartContext);
    const numberOfCartItems = cartContext.items.reduce((curNumber, item) => {
      return curNumber + item.amount;
    }, 0);

    return (
        <div>
            <button className='button' onClick={props.showCart}>
                <span className='icon'>
                    <CartIcon />
                </span>
                <span>Your Cart</span>
                <span className='badge'>
                    {numberOfCartItems}
                </span>
            </button>
        </div>
    );
}

export default HeaderCartButton;