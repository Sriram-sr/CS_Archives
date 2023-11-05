import React, { useState } from "react";
import './ExpenseForm.css';
const ExpenseForm = (props) => {
    const [enteredTitle, titleChanger] = useState('');
    const [enteredAmount, amountChanger] = useState('');
    let [enteredDate, dateChanger] = useState('');

    // for using single state for mulytiple components

    // const [userInput, setUserInput] = useState({
    //     enteredTitle: '',
    //     enteredAmount: '',
    //     enteredDate: '',
    // })

    const titleChangeHandler = (event) => {
        titleChanger(event.target.value);
    //     setUserInput({
    //         ...userInput,
    //         enteredTitle: event.target.value
    // });
    }

    const amountChangeHandler = (event) => {
        amountChanger(event.target.value);
    //     setUserInput({
    //         ...setUserInput,
    //         enteredAmount: event.target.value
    // });
    }

    const dateChangeHandler = (event) => {
        dateChanger(event.target.value);
        // setUserInput({
        //     ...userInput,
        //     enteredDate: event.target.value
        // });
    }

    const submitHandler = (event) => {
        event.preventDefault();
        const formData = {
            title: enteredTitle,
            amount: enteredAmount,
            date: enteredDate
        };
        enteredDate = new Date(enteredDate);
        props.onSaveExpensedata(formData);
        titleChanger('');
        amountChanger('');
        dateChanger('');
        
    }

    return (
        <form onSubmit={submitHandler}>
            <div className="new-expense__controls">
                <div className="new-expense__control">
                    <label>Title</label>
                    <input type="text" value={enteredTitle} onChange={titleChangeHandler} />
                </div>
                <div className="new-expense__control">
                    <label>Amount</label>
                    <input type="number" min="0.01" step="0.01" value={enteredAmount} onChange={amountChangeHandler} />
                </div>
                <div className="new-expense__control">
                    <label>Date</label>
                    <input type="date" min="2017-01-01" max="2022-12-31" value={enteredDate} onChange={dateChangeHandler} />
                </div>
                <div className="new-expense__actions">
                    <button type="submit">Add Expense</button>
                </div>
            </div>
        </form>
    )
}

export default ExpenseForm;