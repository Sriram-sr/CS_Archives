// This is to demo the let, var and const in JS. Hoisting, Scoping.

let letVar = 34;
var varVar = 90;
const constVar = 21;

if (true){
  letVar = 50;
  varVar = 50;
  // constVar = 12;   This should not be done though it is a const variable
}

console.log(letVar);  // will print 50
console.log(varVar);  // will print 50

// But if you do like this,

if (true){
  let letVar = 99;
  var varVar = 99;
}

console.log(letVar); // will print 50 since it is a re-eclared as a block scope variable
console.log(varVar); // will print 99 since it is function scope

console.log(goingToDeclareVar);  // will print undefined

var goingToDeclareVar = 'Declared and initialised'; // This js will do like below

/* 
var goingToDeclareVar;

goingToDeclareVar = 'your text';

// It also does this for let declarations. But you let cannot return undefined intead Reference error
*/

// console.log(goingToDeclareLet);

// let goingToDeclareLet = 12; This will through reference error 

let stringArray = ['Gfg', 'is', 'best', 'for', 'Geeks'];

for(let idx=0;idx<stringArray.length;idx++){
  stringArray[idx] = stringArray[idx].replace('e', 'G').replace('G', 'e');
}

console.log(stringArray);


