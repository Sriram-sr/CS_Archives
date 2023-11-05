import React from 'react';
import './ErrorModel.css';
import './Maincard.css';

const ErrorModal = (props) => {
    return (
        <div className='card'>
            <div className='backdrop' onClick={props.onConfirm} />
            <div className='modal'>
                <header className='header'>
                    <h2>{props.title}</h2>
                </header>
                <div className='content'>
                    <p>{props.message}</p>
                </div>
                <footer className='actions'>
                    <button type='submit' onClick={props.onConfirm} className='button'>Okay</button>
                </footer>
            </div>
        </div>
    );
};

export default ErrorModal