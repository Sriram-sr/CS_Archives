const ShowPost = () => {
    const taskList = []
    const Posts =  () => {
        // const response = await fetch('https://react-http-8b743-default-rtdb.firebaseio.com/Tasks.json');
        // const response = await fetch('http:192.168.191.76:8000/products/');
        // console.log(response.json());
        // fetch('http://localhost:8000/ser/', {mode: 'no-cors'}).then(res=>console.log(res.json()))
        // const data = await response.json();
        // console.log(data);
        // for(const key in data){
        //     taskList.push(data[key]);
        // }
        fetch('http:192.168.191.76:8000/products').then(res=>res.json()).then(result=>console.log(result))
    }

    const content = taskList.map(task => {
        return (<li>{task}</li>);
    })

    Posts();

    return (
        <h1>Good</h1>
    );
};

export default ShowPost;