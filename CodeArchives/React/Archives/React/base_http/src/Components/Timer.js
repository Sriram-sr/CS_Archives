import { useState, useEffect, useContext } from "react";

function Timer() {
    const [count, setCount] = useState(0);
    // const ctx = useContext();
    useEffect(() => {
      setTimeout(() => {
        setCount((count) => count + 1);
      }, 1000);
    }, []);
  
    return <h1>My app is </h1>;
  }

  export default Timer;