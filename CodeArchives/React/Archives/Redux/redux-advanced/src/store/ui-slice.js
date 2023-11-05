import { createSlice } from "@reduxjs/toolkit";

const uiSlice = createSlice({
    name: 'ui',
    initialState: {isCartVisible: false, count: 0, notification: null},
    reducers: {
        toggle(state){
            state.isCartVisible = !state.isCartVisible;
        },
        Count(state, action){
            state.count = action.payload;
        },
        addCount(state){
            state.count++;
        },
        removeCount(state){
            state.count--;
        },
        showNotification(state, action){
            state.notification = {
               status: action.payload.status,
               title: action.payload.title,
               message:  action.payload.message
            }
        }
    }
});

export default uiSlice;