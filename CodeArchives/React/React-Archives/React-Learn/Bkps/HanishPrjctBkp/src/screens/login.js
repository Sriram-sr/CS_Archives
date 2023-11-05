import React, { useState } from 'react'
import './screens.css'
import picture from '../assests/img/pricing-free.png'
import logo from '../assests/img/mprosystems_logo1.png'


const Login = () => {

    const [data, setData] = useState({
        name: '',
        email: '',
    })

    const onchangeHandler = (e) => {
        const { name, value } = e.target
        console.log(value);
        setData({ ...data, [name]: value })
    }

    const loginHandler = () => {
        console.log('logged in');
    }

    return (
        <div className='container cardbg' style={{}} >
            <div className='row' >
                <div className='col-5 align-self-center text-center' >
                    <img alt='leftpicture' src={picture} className='picture mt-5' />
                </div>
                <div className='col-7' >
                    <div className='text-center' >
                        <img alt='logo' src={logo} className='logo mt-5 mb-4' />
                        <h3>Log In</h3>
                    </div>
                    <form className='form mx-auto' onSubmit={loginHandler}>
                        <div className="mb-3 mt-5">
                            <label htmlFor="email" className="form-label ">Email address</label>
                            <input type="email" className="form-control" id="email" name='email' value={data.email} onChange={onchangeHandler} />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="password" className="form-label">Password</label>
                            <input type="password" className="form-control" id="password" name='password' value={data.password} onChange={onchangeHandler} />
                        </div>
                        <button type="submit" className="btn btn-primary mt-3">Login</button>
                        <div className='mt-2'>
                            <p>Don't have an account? <span><a href='/register' >Register</a></span></p>
                        </div>
                    </form>
                </div>

            </div>
        </div>
    )
}

export default Login