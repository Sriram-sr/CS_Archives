import React, { useState } from 'react'
import './screens.css'
import picture from '../assests/img/pricing-free.png'
import logo from '../assests/img/mprosystems_logo1.png'
import { useRegisterUserMutation } from '../api/apiservice'

const Register = () => {

    const [data, setData] = useState({
        name: '',
        email: '',
        password: '',
        password2: ''
    })

    const onchangeHandler = (e) => {
        const { name, value } = e.target
        console.log(value);
        setData({ ...data, [name]: value })
    }

    const { registerUser } = useRegisterUserMutation()



    return (
        <div className='container cardbg' style={{}} >
            <div className='row' >
                <div className='col-5 align-self-center text-center' >
                    <img alt='leftpicture' src={picture} className='picture' />
                </div>
                <div className='col-7' >
                    <div className='text-center' >
                        <img alt='logo' src={logo} className='logo mt-5 mb-4' />
                        <h3>Register</h3>
                    </div>
                    <form className='form mx-auto' >
                        <div class="mb-3 mt-5">
                            <label for="name" className="form-label ">Name</label>
                            <input type="text" className="form-control" id="name" name='name' value={data.name} onChange={onchangeHandler} />
                        </div>
                        <div class="mb-3">
                            <label for="email" className="form-label ">Email address</label>
                            <input type="email" className="form-control" id="email" name='email' value={data.email} onChange={onchangeHandler} />
                            <div id="emailHelp" className="form-text">We'll never share your email with anyone else.</div>
                        </div>
                        <div className="mb-3">
                            <label for="password" className="form-label">Password</label>
                            <input type="password" className="form-control" id="password" name='password' value={data.password} onChange={onchangeHandler} />
                        </div>
                        <div className="mb-3">
                            <label for="password2" className="form-label">Confirm Password</label>
                            <input type="password" className="form-control" id="password2" name='password2' value={data.password2} onChange={onchangeHandler} />
                        </div>
                        <button type="submit" className="btn btn-primary">Register</button>
                        <div className='mt-2'>
                            <p>Already Registered? <span><a href='/login' >SignIn</a></span></p>
                        </div>
                    </form>
                </div>

            </div>
        </div>
    )
}

export default Register