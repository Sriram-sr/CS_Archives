import React, { useState } from 'react';
import './ExpenseForm.css';

const ExpenseForm = () => {
  const [newExpenseData, setNewExpense] = useState({
    enteredTitle: '',
    enteredAmount: '',
    enteredDate: '',
  });

  const titleChangeHandler = (event) => {
    setNewExpense((prevState) => {
      return {
        ...prevState,
        enteredTitle: event.target.value,
      };
    });
  };

  const amountChangeHandler = (event) => {
    setNewExpense((prevState) => {
      return {
        ...prevState,
        enteredAmount: event.target.value,
      };
    });
  };

  const dateChangeHandler = (event) => {
    setNewExpense((prevState) => {
      return {
        ...prevState,
        enteredDate: event.target.value,
      };
    });
  };

  const getOverallData = (event) => {
    event.preventDefault();
    console.log(newExpenseData);
  }

  return (
    <form>
      <div className='new-expense__controls'>
        <div className='new-expense__control'>
          <label>Title</label>
          <input onChange={titleChangeHandler} type='text' value={newExpenseData.enteredTitle} />
        </div>
        <div className='new-expense__control'>
          <label>Amount</label>
          <input
            type='number'
            onChange={amountChangeHandler}
            min='0.01'
            step='0.01'
            value={newExpenseData.enteredAmount}
          />
        </div>
        <div className='new-expense__control'>
          <label>Date</label>
          <input
            type='date'
            onChange={dateChangeHandler}
            min='2021-09-01'
            max='2023-12-31'
            value={newExpenseData.enteredDate}
          />
        </div>
      </div>
      <div className='new-expense__actions'>
        <button type='submit' onClick={getOverallData}>Add Expense</button>
      </div>
    </form>
  );
};

export default ExpenseForm;
