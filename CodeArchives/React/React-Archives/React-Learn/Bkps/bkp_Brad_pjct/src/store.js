import { configureStore } from '@reduxjs/toolkit';
import { applyMiddleware } from '@reduxjs/toolkit';
// import { composeWithDevTools } from '@reduxjs/toolkit/dist/devtoolsExtension';
import { composeWithDevTools } from 'redux-devtools-extension';
import thunk from 'redux-thunk';
import rootReducer from './reducers';

const middleware = [thunk];
const initialState = {};

const store = configureStore(rootReducer, initialState, composeWithDevTools(applyMiddleware(...middleware)));

export default store;