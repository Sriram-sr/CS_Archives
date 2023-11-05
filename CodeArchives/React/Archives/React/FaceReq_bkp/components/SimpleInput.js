import { useRef, useState } from 'react';

const SimpleInput = (props) => {
  const [enteredValue, setEnteredValue] = useState('');
  const [textValid, setTextValid] = useState(false);
  const textValue = useRef();

  const onTextChange = (event) => {
    setEnteredValue(event.target.value);
  }

  const submitHandler = (event) => {
    event.preventDefault();
    if (enteredValue.trim().length === 0){
      return;
    }
    setTextValid(true);
    console.log(textValue.current.value);
  }
  const textClasses = textValid ? 'form-control' : 'form-control invalid';

  return (
    <form onSubmit={submitHandler}> 
      <div className={textClasses}>
        <label htmlFor='name'>Your Name</label>
        <input type='text' ref={textValue} value={enteredValue} id='name' onChange={onTextChange} />
        {!textValid && <p className='error-text'>Entered text is invalid</p>}
      </div>
      <div className="form-actions">
        <button>Submit</button>
      </div>
    </form>
  );
};

export default SimpleInput;
