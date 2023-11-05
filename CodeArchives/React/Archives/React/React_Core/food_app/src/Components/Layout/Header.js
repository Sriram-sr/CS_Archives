import mealImage from '../../assets/meals.jpg';
import './Header.css';
import HeaderCartButton from './HeaderCartButton';
import { Fragment } from 'react';

const Header = (props) => {
    const clickHandler = () => {

    };

    return(
        <Fragment>
            <button className='meal' type='button' onclick={clickHandler}>Save Meal</button>
            
            <header className='header'>
                <h1>Ragul Meals</h1>
                <HeaderCartButton showCart={props.showCart} />
            </header>
            <div className='main-image'>
                <img src={mealImage} alt='a table of delicious foods' />
            </div>
        </Fragment>
    );
}

export default Header;