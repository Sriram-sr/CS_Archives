import './App.css';
import { Route, Routes } from "react-router-dom"
import Login from './screens/login';
import Register from './screens/register';
import Test from './screens/test';
import Drawer from './screens/drawer';
import Profile from './screens/profile';
import Attendance from './screens/attendance';
import Home from './screens/home';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path='/login' element={<Login />} />
        <Route path='/register' element={<Register />} />
        <Route path='/test' element={<Test />} />
        <Route path='/dashboard' element={<Drawer />}>
          <Route path='home' element={<Home />} />
          <Route path='attendance' element={<Attendance />} />
          <Route path='profile' element={<Profile />} />
        </Route>
      </Routes>
    </div>
  );
}

export default App;
