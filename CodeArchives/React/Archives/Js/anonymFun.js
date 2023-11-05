let alias = function(){
    console.log('Im called anonymously....');
}

let credentials = {
    username: 'sriram',
    password: 'sr'
};

let bunch_data = [
    {
        username: 'sriram',
        message: 'Trust the process is your message'
    },
    {
        username: 'sr',
        message: 'Dont look back is the message'
    }
]


let show_data = function(username){
    console.log(`username is ${username}`);
    console.log('Trust the process');
}

// let username = prompt('Enter your Username');
let username = 'sriram';

for(obj in bunch_data){
    console.log(bunch_data[obj].username);
    if(bunch_data[obj].username == 'sriram'){
        console.log('success');
    }
    else{
        console.log('Something went wrong');
    }
}
// let password = prompt('Enter your password');

// if (username === credentials.username && password === credentials.password){
//     show_data(username);
// }
// else{
//     console.log('Enter valid credentials');
// }
