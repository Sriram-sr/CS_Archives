import Modal from "../UI/Modal";
import './Cart.css';
import CartContext from "../../store/cart-context";
import { useContext, useState } from "react";
import CartItem from "./CartItem";
import Checkout from './Checkout';

const Cart = (props) => {
    const [isCheckout, setCheckout] = useState(false);

    const cartContext = useContext(CartContext);
    const totalAmount = `$${cartContext.totalAmount.toFixed(2)}`;
    const hasItems = cartContext.items.length > 0;
    const cartItems = (
        <ul className='cart-items'>
            {cartContext.items.map((item) => (
                <CartItem key={item.id}
                    name={item.name}
                    amount={item.amount}
                    price={item.price}
                // onAdd = {cartItemAddHandler.bind(null, item)}
                // onRemove = {cartItemRemoveHandler.bind(null, item.id)}
                />
            ))}
        </ul>
    );

    const clickHandler = () => {
        setCheckout(true);
    };

    const placeOrder = (order) => {
        const sendOrder = async () => {
            await fetch('https://react-http-8b743-default-rtdb.firebaseio.com/orders.json', {
                method: 'POST',
                body: JSON.stringify(order),
                headers: {
                    'Content-Type': 'application/json'
                }
            });
        };
        sendOrder();
    }

    return (
        <Modal >
            {cartItems}
            <div className='total'>
                <span>Total Amount</span>
                <span>{totalAmount}</span>
            </div>
            {isCheckout && <Checkout onConfirm={placeOrder} />}
            <div className='actions'>
                <button onClick={props.closeHandler} className='button--alt'>Close</button>
                {hasItems && <button onClick={clickHandler} className='button'>Order</button>}
            </div>
        </Modal>
    );
};

export default Cart;