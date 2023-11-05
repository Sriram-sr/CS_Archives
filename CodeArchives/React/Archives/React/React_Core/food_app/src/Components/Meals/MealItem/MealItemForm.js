import './MealItemForm.css';
import Input from '../../UI/Input';
import '../../UI/Input.css';
import { useRef, useState } from 'react';

const MealItemForm = (props) => {
    const amountInputRef = useRef();
    const [amountIsValid, setAmountValid] = useState(true);
    const submitHandler = (event) => {
        event.preventDefault();
        const enteredAmount = amountInputRef.current.value;
        const enteredAmountNumber = +enteredAmount;

        if(
            enteredAmount.trim().length === 0 ||
            enteredAmountNumber < 1 || 
            enteredAmountNumber > 5
        ){
            setAmountValid(false);
            return;
        }
        props.addToCart(enteredAmountNumber);
    }

    return (
        <form className="form" onSubmit={submitHandler}>
            <Input label='Amount' ref={amountInputRef} input={
                {
                    id: 'amount',
                    type: 'number',
                    min: '1',
                    max: '5',
                    step: '1',
                    defaultValue: '1'
                }
            }/>
            <button type='submit'>+ Add</button>
            {!amountIsValid && <p>Enter a valid amount(1-5).</p>}
        </form>
    );
}

export default MealItemForm;