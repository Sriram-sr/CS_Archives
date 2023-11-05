import { useState } from 'react';
import './App.css';
import ListData from './ListData';
import Maincard from './Maincard';

 const defArray = [];

function App() {
  const [array, changeArray] = useState(defArray);

  const getNameAge = (name, age) => {
    const temp = {
      id: Math.random().toString(),
      name: name,
      age: age
    }
    
    changeArray ( (oldData) => {
      return [...oldData, temp];
    })
    
  }

  return (
    // <section className='app'>
    <>
      <Maincard getNameAge={getNameAge} />
      <ListData items={array} />
    </>
      
    // </section>
  );
}

export default App;
