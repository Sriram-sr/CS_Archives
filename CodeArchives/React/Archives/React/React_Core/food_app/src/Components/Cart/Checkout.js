import { useRef } from 'react';
import './Checkout.css';

const Checkout = (props) => {
    const nameInput = useRef();
    const streetInput = useRef();
    const postalInput = useRef();
    const cityInput = useRef();

    const submitHandler = (event) => {
        event.preventDefault();
        const order = {
            id: Math.random().toString(),
            name: nameInput.current.value,
            street: streetInput.current.value,
            postal_code: postalInput.current.value,
            city: cityInput.current.value
        };
        props.onConfirm(order);
    };

    return (
        <form onSubmit={submitHandler}>
            <div className='control'>
                <label htmlFor='name'>Your Name</label>
                <input type='text' id='name' ref={nameInput} />
            </div>
            <div className='control'>
                <label htmlFor='street'>Street</label>
                <input type='text' id='street' ref={streetInput} />
            </div>
            <div className='control'>
                <label htmlFor='postal'>Postal Code</label>
                <input type='text' id='postal' ref={postalInput} />
            </div>
            <div className='control'>
                <label htmlFor='city'>City</label>
                <input type='text' id='city' ref={cityInput} />
            </div>
            <div className='actions'>
                <button type='button'>Cancel</button>
                <button type='submit'>Confirm</button>
            </div>
        </form>
    );
};

export default Checkout;