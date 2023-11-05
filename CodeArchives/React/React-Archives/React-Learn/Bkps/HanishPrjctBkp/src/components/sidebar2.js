import React from 'react'
import './components.css'
import profile from '../assests/img/team-4.jpg'

const Sidebar2 = () => {
    return (
        <div className='side-menu'>
            <img src={profile} className='avatar' />
            <div className='side-menu-content' >
                <ul>
                    <li>
                        Home
                    </li>
                    <li>
                        Attendance
                    </li>
                </ul>
            </div>
        </div>
    )
}

export default Sidebar2