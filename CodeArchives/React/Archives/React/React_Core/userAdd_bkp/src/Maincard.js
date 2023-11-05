import './Maincard.css';
import { useState, useRef }from 'react';
import ErrorModal from './ErrorModel';

const Maincard = (props) => {
    const [defName, setName] = useState('');
    const [defAge, setAge] = useState('');
    const [error, setError] = useState();
    const nameInpRef = useRef();
    const ageInpRef = useRef();

    const submitHandler = (event) => {
        event.preventDefault();
        // console.log(nameInpRef.current.value);
        if(defName.trim().length===0 || defAge.trim().length===0){
            setError(
                {
                    title: 'Unexpected Value',
                    message: 'Please enter Valid Name and Age'
                }
            )    
        }

        if(+defAge < 0){
            setError(
                {
                    title: 'Negative value',
                    message: 'Please enter a valid Age'
                }
            )
        }
        props.getNameAge(defName, defAge);
        setName('');
        setAge('');
    }

    const nameChange = (event) => {
        setName(event.target.value);
    }

    const ageChange = (event) => {
        setAge(event.target.value);
    }

    function errorHandler(){
        setError(null);
    }

    return (
        <div>
            {/*  */}
            {error && <ErrorModal title={error.title} message={error.message} onConfirm={errorHandler} />}
            <div className='card'>
                <form onSubmit={submitHandler}>
                    <label>Username</label>
                    <input type='text' value={defName} ref={nameInpRef} onChange={nameChange} /><br />
                    <label>Age(Years)</label>
                    <input type='number' className='down' ref={ageInpRef} value={defAge} onChange={ageChange} />
                    {/* <input className='button' type='submit' value='submit' /> */}
                    <button className='button' type='submit'>Add User</button>
                </form>
            </div>
        </div>

    )
}

export default Maincard;
