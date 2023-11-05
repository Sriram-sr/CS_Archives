import './MainHeader.css';
import { NavLink } from 'react-router-dom';


const MainHeader = () => {
    return (
        <header className='header'>
            <nav>
                <ul>
                    <li>
                        <NavLink activeClassName='active' to='/home'>Welcome</NavLink>
                    </li>
                    <li>
                        <NavLink activeClassName='active' to='/products'>Products</NavLink>
                    </li>
                </ul>
            </nav>
        </header>
    )
};

export default MainHeader;