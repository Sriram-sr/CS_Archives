import { useRef, useState } from 'react';

const PostForm = (props) => {
    const [textField, setText] = useState('');
    const taskField = useRef();
    const submitHandler = event => {
        event.preventDefault();
        props.sendHttp(taskField.current.value);
        setText('');
    }

    const textChange = e => {
        setText(e.target.value);
    }

    return(
        <form onSubmit={submitHandler}>
            <label>Add Post: </label>
            <input type='text' ref={taskField} value={textField} onChange={textChange} placeholder='Enter a task' />
            <button type='submit'>Submit</button> 
        </form>
    );
};

export default PostForm;