const promise = new Promise( (resolve, reject) => {
    if(false){
        resolve('Stuff Worked');
    }else{
        reject('Not Worked');
    }
})

promise.then( result => console.log(result));

let users = fetch('https://jsonplaceholder.typicode.com/users').then(response=>{
    console.log(response.json());
})