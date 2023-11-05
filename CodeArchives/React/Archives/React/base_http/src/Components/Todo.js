import { memo } from "react";
import React from "react";

const Todo = (props) => {
    console.log('Child rerenders');
    return (
        <div>
        <h1>Hello</h1>
        {
            props.todos.map((item, idx)=> <p key={idx}>{item}</p>)      
        }
        </div>
    );
};

export default memo(Todo);