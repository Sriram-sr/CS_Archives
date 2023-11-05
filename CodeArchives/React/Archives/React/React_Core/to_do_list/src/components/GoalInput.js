import { useState } from 'react';
import './GoalInput.css';

const GoalInput = (props) => {
    const [currText, changeText] = useState('');

    const textChange = (event) => {
        changeText(event.target.value);
    }

    const afterSubmit = (event) => {
        event.preventDefault();
        props.addNewInput(currText);
        changeText('');
    }

  return (
    <form onSubmit={afterSubmit}>
      <div className="form-control">
        <label>Course Goal</label>
        <input type="text" value={currText} onChange={textChange}></input>
      </div>
      <button className="button" type="submit">Add Goal</button>
    </form>
  );
};

export default GoalInput;
