import './Data.css';
import './Maincard.css';

const ListData = (props) => {
    const empty = <div></div>
    const retData = 
    <div className='users'>
        <ul className='data'>
            {props.items.map(
                (data) => {
                    return (
                        <li key={data.id}>{data.name} ({data.age} years old)</li>
                    );
                }
            )}
        </ul>
    </div>

    return (
        <div className='card'>
               {
            props.items.length === 0 ? empty : retData
        }
        </div>
     
    );
}

export default ListData;