import { useState } from "react";
import Todo from "./Todo";

const Todos = () => {
    const [todos, setTodos] = useState(['Do work', 'Do the first']);
    const [count, setCount] = useState(0);
    console.log(count);
    return (
        <>
            <Todo todos={todos} />
            <button onClick={() => setCount((prevCount)=>prevCount+1)}>Increment</button>
        </>

    );
};

export default Todos;