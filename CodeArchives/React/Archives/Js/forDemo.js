// let numbers = [1,2,3,4,5,6];

// numbers.forEach(function(i,j,k){
//     console.log(i,j,k);
// });

// function  demoFun(){
//     console.log('Called function');
// }

// demoFun();

cart_items = [
    {id: 'm1', name: undefined, amount: 1, price: 22.99},
    {id: 'm2', name: undefined, amount: 1, price: 22.99},
    {id: 'm3', name: undefined, amount: 1, price: 22.99},
    {id: 'm4', name: undefined, amount: 1, price: 22.99},
]

const redValue = cart_items.reduce(
    (currNumber, item, idx, arr) => {
        console.log('currNum', currNumber);
        console.log('item', item);
        return currNumber+item.amount;
    }, 0);

console.log(redValue);

let arry = [1,2,3,5,6,7];

const unlimited = () => {
    console.log('try');
}

// setInterval(unlimited, 1000);