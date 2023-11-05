import { configureStore } from '@reduxjs/toolkit';   
import { createSlice } from '@reduxjs/toolkit';

const initialState = {
    counter: 0,
    showCounter: true
}

const counterSlice = createSlice({
    name: 'counter',
    // initialState: initialState,
    initialState,
    reducers: {
        increment(state) {
            state.counter++;
            // state.counter = Number(state.counter) + 1;
        },
        decrement(state) {
            state.counter--;
        },
        increase(state, action){
            state.counter = state.counter+action.payload;
        },
        toggle(state){
            state.showCounter = !state.showCounter;
        }
    }
});

const initialAuthState = { isAuthenticated: true };

const authSlice = createSlice({
    name: 'auth',
    initialState: initialAuthState,
    reducers: {
        login(state){
            state.isAuthenticated = true;
        },
        logout(state){
            state.isAuthenticated = false;
        }
    }
});

const counterReducer = (state = initialState, action) => {
    switch(action.type){
        case 'increment':
            return { counter: state.counter+1, showCounter: state.showCounter };
        case 'decrement':
            return { counter: state.counter-1, showCounter: state.showCounter };
        case 'toggle':
            return { counter: state.counter, showCounter: !state.showCounter };
        case 'increase':
            return { counter: state.counter+5, showCounter: state.showCounter };
        default:
            return state;  
    }
};

// const store = configureStore(counterReducer); // this won't work...
// const store = configureStore({ reducer: counterReducer });
const store = configureStore({reducer: {
    counter: counterSlice.reducer,
    auth: authSlice.reducer,
}});

export const counterActions = counterSlice.actions;
export const authActions = authSlice.actions;
export default store;