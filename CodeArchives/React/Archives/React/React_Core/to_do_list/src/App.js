import "./App.css";
import GoalsList from "./components/GoalsList";
import GoalInput from './components/GoalInput';
import { useState } from "react";

const tempGoals = [
  {
    text: "Do all exercises!",
    id: "g1",
  },
  {
    text: "Finish the course!",
    id: "g2",
  },
];

function App() {
  const [courseGoals, addGoal] = useState(tempGoals);

  const getInput = (newGoal) => {
    const newlyCreated = {
      text: newGoal,
      id : Math.random().toString()
    };
  
    const newGoalsArray = [
      newlyCreated,
      ...courseGoals,
    ];

    addGoal(newGoalsArray);
  }

  const deleteFunction = (deleteId) =>{
    const newArray = courseGoals.filter(
      goal => {
        return goal.id !== deleteId;
      }
    )
    addGoal(newArray);
  }

  // if (const)

  return (
    <div>
      <section id="goal-form">
        <GoalInput addNewInput={getInput}/>
      </section>
      <section id="goals">
        <GoalsList goals={courseGoals} deleteFunction={deleteFunction}/>
      </section>
    </div>
  );
}

export default App;
