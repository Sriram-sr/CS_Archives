const Card = (props) => {
    return (
        <div className="bg-light-green dib br3 pa3 ma2 grow shadow-5">
            <img src={`https://robohash.org/${props.id}?150x50`} alt="robo" />
            <div>
                <h2>{props.name}</h2>
                <p>davidcisco@yahoo.com</p>
            </div>
        </div>
    );
}

export default Card;