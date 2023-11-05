import React, { useState, useCallback, useMemo } from 'react';
import Button from './Button';
import DemoComp from './DemoComp';
// import AuthContext from './Contexts/auth_context';
// import Login from './components/Login/Login';
// import Home from './components/Home/Home';
// import MainHeader from './components/MainHeader/MainHeader';

// const AuthContext = React.createContext(
//   {
//     isLoggedIn: false
//   }
// );

// function App() {
//   const [isLoggedIn, setIsLoggedIn] = useState(false);

//   useEffect(
//     () => {
//       console.log('useeffect runs');
//       const storedValue = localStorage.getItem('isLoggedIn');
//       if (storedValue === '1'){
//         setIsLoggedIn(true);
//       }
//     }, []
//   )


//   const loginHandler = (email, password) => {
//     // We should of course check email and password
//     // But it's just a dummy/ demo anyways
//     localStorage.setItem('isLoggedIn', '1');
//     setIsLoggedIn(true);
//   };

//   const logoutHandler = () => {
//     setIsLoggedIn(false);
//   };

//   return (
//     <AuthContext.Provider value={
//       {
//         isLoggedIn: isLoggedIn,
//     }
//     }>
//       <MainHeader onLogout={logoutHandler} />
//       <main>
//         {!isLoggedIn && <Login onLogin={loginHandler} />}
//         {isLoggedIn && <Home onLogout={logoutHandler} />}
//       </main>
//     </AuthContext.Provider>
//   );
// }

const App = () => {
  const [isActive, activate] = useState(false);
  const clickFunction = useCallback(() =>{
    activate( (prevState) => {
      return !prevState;
    } )
  }, [])

  console.log('APP RUNNING');
  const demoItems = useMemo(() => ['hello', 'world', 'java', 'javascript', 'map'], []);
  return (
    <div>
      <h1>Hello Js</h1>
      <DemoComp items={demoItems} />
      <Button clicked={clickFunction}>Button</Button>
    </div>  
  );
};

export default App;
