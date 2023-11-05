import './Data.css';

const Data = (props) => {
    return(
        <div className="data">
            <h3>{props.name} {props.age}</h3>
        </div>
    )
}

export default Data;