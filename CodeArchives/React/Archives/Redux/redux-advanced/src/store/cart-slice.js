import { createSlice } from '@reduxjs/toolkit';

const initialState = {
    items: [],
    totalQuantity: 0,
    totalPrice: 0
};

const cartSlice = createSlice({
    name: 'cart',
    initialState,
    reducers: {
        addItem(state, action){
            state.totalQuantity++;
            const newItem = action.payload;
            const existingItem = state.items.find(item=>item.id === newItem.id);
            if (!existingItem){
                state.items.push({
                    id: newItem.id,
                    name: newItem.title,
                    price: newItem.price,
                    quantity: 1,
                    totalPrice: newItem.price
                })
            }else{
                existingItem.quantity++;
                existingItem.totalPrice += newItem.price;
            }
        },
        removeItem(state, action){
            state.totalQuantity--;
            const removeItem = action.payload;
            const existingItem = state.items.find(item => item.id=== removeItem.id);
            if(existingItem.quantity===1){
               const temp = [];
               for(const item of state.items){
                if(item.id!==removeItem.id){
                    temp.push(item);
                }
               }
               state.items = temp;
            }else{
                existingItem.quantity--;
                existingItem.totalPrice-=removeItem.price;
            }
        }
    }
});

export default cartSlice;
