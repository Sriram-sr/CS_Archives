import { useState } from 'react';
import UserFinder from './components/UserFinder';

function App() {
  const [showFinder, setStatus] = useState(true);

  const changeStatus = () => {
    setStatus(!showFinder);
  }

  return (
    <div>
      {showFinder && <UserFinder />}
      <button onClick={changeStatus}>Take Away</button>
    </div>
  );
}

export default App;
