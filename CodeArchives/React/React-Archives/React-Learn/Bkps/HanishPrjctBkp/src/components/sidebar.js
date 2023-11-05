import { Menu } from 'antd';
import React from 'react'
import { MailOutlined, SettingOutlined } from '@ant-design/icons';



function getItem(label, key, icon, children, type) {
    return {
        key,
        icon,
        children,
        label,
        type,
    };
}

const items = [
    getItem('Home', 'sub1', <MailOutlined />,),
    {
        type: 'divider',
    },
    getItem('Attendance', 'sub4', <SettingOutlined />)
];


const Sidebar = () => {

    const onClick = (e) => {
        console.log('click ', e);
    }


    return (
        <div>
            <Menu
                onClick={onClick}
                style={{
                    width: 256,
                    height: 728
                }}
                defaultSelectedKeys={['1']}
                defaultOpenKeys={['sub1']}
                mode="inline"
                items={items}
            />
        </div>
    )
}

export default Sidebar