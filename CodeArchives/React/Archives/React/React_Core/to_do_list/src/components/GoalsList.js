import GoalItem from './GoalItem';
import React from 'react';
import './GoalsList.css';

const GoalsList = props => {
    return (
        <ul className='goal-list'>
        {props.goals.map( goal => (
                <GoalItem 
                key = {goal.id}
                id = {goal.id}
                deleteFunction={props.deleteFunction}
                >
                    {goal.text}   
                </GoalItem>
            )
        )}
        </ul>
    )
}

export default GoalsList;