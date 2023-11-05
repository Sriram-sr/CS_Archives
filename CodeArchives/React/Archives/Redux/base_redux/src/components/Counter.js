import classes from './Counter.module.css';
import { useSelector, useDispatch } from 'react-redux';
import { useState } from 'react';
import { counterActions } from '../store';

const Counter = () => {
  const counter = useSelector(state => state.counter.counter);
  const noToggle = useSelector(state=> state.counter.showCounter);
  const dispatch = useDispatch();

  const toggleCounterHandler = () => { 
      // dispatch({type: 'toggle'});
      dispatch(counterActions.toggle());
  };
 
  const incrementHandler = () =>{
    // dispatch({type: 'increment'});
    dispatch(counterActions.increment());
  }

  const decrementHandler = () =>{
    // dispatch({type: 'decrement'});
    dispatch(counterActions.decrement());
  }

  const increaseHandler = () =>{
    // dispatch({type: 'increase'});
    dispatch(counterActions.increase(7));
  }

  const countShow = <div className={classes.value}>{counter}</div>;

  return (
    <main className={classes.counter}>
      <h1>Redux Counter</h1>
      {!noToggle && countShow}
      <div>
        <button onClick={incrementHandler}>Increment</button>
        <button onClick={decrementHandler}>Decrement</button>
        <button onClick={increaseHandler}>Increase</button>
      </div>
      <button onClick={toggleCounterHandler}>Toggle Counter</button>
    </main>
  );
};

export default Counter;
