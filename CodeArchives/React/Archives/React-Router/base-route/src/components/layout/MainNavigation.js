import { NavLink } from "react-router-dom";
import './MainNavigation.css';

const MainNavigation = () => {
    return (
         <header className='header'>
            <div className='logo'>Great Quotes</div>
            <nav className='nav'>
                <ul>
                    <li>
                        <NavLink to='/quotes' activeClassName='active'>All Quotes</NavLink>
                    </li>
                    <li>
                        <NavLink to='/new-quote' activeClassName='active'>New Quote</NavLink>
                    </li>   
                </ul>
            </nav>
         </header>
    )
};

export default MainNavigation;