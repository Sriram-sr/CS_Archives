import React from 'react'
import './components.css'
import logo from '../assests/img/logo.png'
import { Avatar, Dropdown } from 'antd';
import { blue } from '@mui/material/colors';


const items = [
    {
        label: "Profile",
        key: '0',
    },
    {
        type: 'divider',
    },
    {
        label: "Logout",
        key: '1',
    },
];


const Appbar = () => {



    return (
        <div className='appHeader' >
            <img src={logo} />
            <h3>mieuPro Systems</h3>
            <Dropdown menu={{
                items,
            }}
                trigger={['click']}
                size='large'
                style={{ width: '50px' }}
            >
                <Avatar style={{ backgroundColor: '#0d47a1', verticalAlign: 'middle' }} size='large'>
                    HK
                </Avatar>
            </Dropdown>
        </div>
    )
}

export default Appbar