import './GoalItem.css';

const GoalItem = (props) => {
    const afterClicked = (event) => {
        props.deleteFunction(props.id);
    }

    return (
        <li className="goal-item" onClick={afterClicked}>
            {props.children}
        </li>
    );
}

export default GoalItem;