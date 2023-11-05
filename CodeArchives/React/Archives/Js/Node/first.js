let number = 57821;
let rem, temp, result = 0;

while(number>1){
    rem = number%10;
    result = (result*10) + rem;
    number = Math.floor(number/10);
}

// console.log(result);

let keyword = this;
console.log(keyword);

function myFunc(){
    return this;
}

function add(num1, num2){
    return num1 + num2;
}

// console.log(add(1,2));
console.log(myFunc());