import Counter from './components/Counter';
// import { Provider } from 'react-redux';
// import store from './store/index';
import Auth from './components/Auth';
import Header from './components/Header';
import { Fragment } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { authActions } from './store/index';

function App() {
  const authenticationState = useSelector(state => state.auth.isAuthenticated);
  const dispatch = useDispatch();

  const logoutHandler = () => {
    dispatch(authActions.logout());
  };

  const loginHandler = () => {
    dispatch(authActions.login());
  };

  return (
    // <Provider store={store}>
    //     <Counter />
    // </Provider>
    <Fragment>
      {/* <Provider store={store}> */}
      {authenticationState && <Header logoutHandler={logoutHandler}/>}
      {!authenticationState && <Auth loginHandler={loginHandler}/>}
      <Counter />
      {/* </Provider> */}
    </Fragment>
  );
}

export default App;
