const array = [3,8,7,1,8,10];
let indexes = array.entries(); // entries is like enumerate (idx, value)
let bool = array.includes(1);
// console.log(bool);

// for(let value of array){
//     console.log(value);
// }

for(let idx of indexes){
    // console.log(idx);
}

let random_value = Math.random();
// console.log(Math.floor(random_value*100));

function ageCheck(){
    let value = document.getElementById('get').value;
    if (value<18){
        document.getElementById('age').innerHTML = 'Too Young';
    }
    else{
        document.getElementById('age').innerHTML = 'Good Enough';
    }
}

let swValue = 13;
switch (swValue){
    case 1:
        console.log('This is one');
        break;

    case 2:
        console.log('This is Two');
        break;

    case 3:
        console.log('This is Three');
        break;

    case 4:
        console.log('This is Four');
        break;

    case 5:
        console.log('This is Five');   
        break;

    default:
        console.log('Nothing is found');
        break;
}

const cars = ["BMW", "Volvo", "Mini"];

let text = "Goodbye";
for (let x of text) {
    console.log(x);
    text += x;
}
