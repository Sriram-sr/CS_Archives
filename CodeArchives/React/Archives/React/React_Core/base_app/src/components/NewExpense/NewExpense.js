import React from 'react';
import './NewExpense.css';
import ExpenseForm from './ExpenseForm';

const NewExpense = (props) => {
        const saveExpenseDataHandler = (enteredExpenseData) => {
            const expenseData = {
                ...enteredExpenseData, 
                id: Math.random().toString()
            };
            props.afterAdded(expenseData);
        }
        return (
            <div className='new-expense'>
                <ExpenseForm onSaveExpensedata={saveExpenseDataHandler} />
            </div>
        );
    }
    

export default NewExpense;