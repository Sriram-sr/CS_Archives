import React from 'react';
// import BackwardCounter from './components/BackwardCounter';
// import ForwardCounter from './components/ForwardCounter';
import PostForm from './components/PostForm';
import ShowPost from './components/ShowPost';

function App() {
  const sendHttp = async (task) => {
    // 'https://react-http-8b743-default-rtdb.firebaseio.com/'
    await fetch('https://react-http-8b743-default-rtdb.firebaseio.com/Tasks.json', {
      method: 'POST',
      body: JSON.stringify(task),
      headers: {
        'Content-Type': 'application/json'
      }
    });
    console.log('check firebase');
  }

  return (
    // <React.Fragment>
    //   <ForwardCounter />
    //   <BackwardCounter />
    // </React.Fragment>
    <div>
      <PostForm sendHttp={sendHttp}/>
      <ShowPost />
    </div>
  );
}

export default App;
