import { useState } from 'react';
import React from 'react';
import classes from './base.module.css';
import Timer from './Timer';

const Base = (props) => {
    const [name, setName] = useState('');
    const initialData = {
        name: 'Sriram',
        age: 22,
        place: 'Tm'
    };
    const [userData, setUserData] = useState(initialData);
    const submitHandler = (event) => {
        event.preventDefault();
        console.log(name);
    };

    const changeAddress = () => {
        if (userData.place === 'Tm') {
            setUserData((prevState) => {
                return {
                    ...prevState, place: 'Cpt'
                }
            })
        }else{
            setUserData((prevState) => {
                return {
                    ...prevState, place: 'Tm'
                }
            })
        }   

    }

    return (
        <React.Fragment>
            <form onSubmit={submitHandler} className={classes.form}>
                <label htmlFor='name'>Name: </label>
                <input type='text' onChange={(event) => setName(event.target.value)}></input><br />
                <textarea>Dummy text</textarea>
                <button type='submit'>Over</button>
            </form>
            <ol>
                <li>{userData.name}</li>
                <li>{userData.age}</li>
                <li>{userData.place}</li>
            </ol>
            <button onClick={changeAddress} type='button'>Change</button>
            <Timer />
        </React.Fragment>
    );
};

export default Base;