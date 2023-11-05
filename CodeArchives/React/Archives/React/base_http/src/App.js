import React from 'react';
import { createContext } from 'react';
import Base from './Components/Base';
import Todos from './Components/Todos';

function App() {
  const AppContext = createContext();
  const value = {value: 'base_app'};
  return (
    <React.Fragment>
        <Base />
        <Todos />
    </React.Fragment>
  );
}

export default App;
