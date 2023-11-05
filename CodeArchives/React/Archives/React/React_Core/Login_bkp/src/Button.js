import React from 'react';

const Button = (props) => {
    console.log('BUTTON RUNNING');
    return (
        <button onClick={props.clicked}>{props.children}</button>
    );
};

export default React.memo(Button);