import CartContext from "./cart-context";
import { useReducer } from 'react';

const defaultCartState = {items:[], totalAmount:0};

const cartReducer = (state, action) => {
    if (action.type === 'ADD'){
        const existingItemIndex = state.items.findIndex(
            (item) => item.id === action.item.id
        );
        const existingItem = state.items[existingItemIndex];
        let updatedItems;
        if (existingItem){
            const updatedItem = {
                ...existingItem,
                amount: existingItem.amount + action.item.amount
            };
            updatedItems = [...state.items]; 
            updatedItems[existingItemIndex] = updatedItem;
        }else {
            updatedItems = state.items.concat(action.item);
        }
        const updatedAmount = state.totalAmount + (action.item.price * action.item.amount)
            return ({
            items: updatedItems,
            totalAmount: updatedAmount
        });
    }

}

const CartProvider = (props) => {
    const [cartState, dispatchCart] = useReducer(cartReducer, defaultCartState);

    const addCartHandler = (item) => {
        dispatchCart({type: 'ADD', item: item});
    };
    const removeCartHandler = (item) => {
        dispatchCart({type: 'REMOVE', item: item})
    };

    const cartContext = {
        items: cartState.items,
        totalAmount: cartState.totalAmount,
        addItem: addCartHandler,
        removeItem: removeCartHandler
    }


    return (
        <CartContext.Provider value={cartContext}>
            {props.children}
        </CartContext.Provider>
    );
}

export default CartProvider;