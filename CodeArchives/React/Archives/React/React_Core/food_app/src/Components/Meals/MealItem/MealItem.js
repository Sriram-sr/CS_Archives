import './MealItem.css';
import MealItemForm from './MealItemForm';
import { useContext } from 'react';
import CartContext from '../../../store/cart-context';

const MealItem = (props) => {
    const cartContext = useContext(CartContext);
    // const price = `$${props.price.toFixed(2)}`;
    const price = props.price;
    const addToCart = amount => {
        cartContext.addItem({
            id: props.id,
            name: props.name,
            amount: amount,
            price: props.price
        })
    }

    return (
        <li className="meal">
            <div>
                <h3>{props.meal}</h3>
                <div className="description">{props.description}</div>
                <div className="price">${price}</div>
            </div>
            <div><MealItemForm addToCart={addToCart}/></div>
        </li>
    );
}

export default MealItem;