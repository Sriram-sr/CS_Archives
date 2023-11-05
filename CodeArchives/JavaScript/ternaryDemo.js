let userInput = 10;

userInput < 0
  ? console.log('user entered is negative')
  : userInput == 0
  ? console.log('user entered is zero')
  : userInput > 0
  ? console.log('user entered is positive')
  : console.log('user entered is unknown');

// if (userInput < 0) {
//   console.log("user entered is negative");
// } else if (userInput == 0) {
//   console.log("user entered is zero");
// } else if (userInput > 0) {
//   console.log("user entered is positive");
// } else {
//   console.log("user entered is unknown");
// }

const someThing = {
  x: 42,
  getX: function() {
    return this.x;
  }
};

const unboundGetX = someThing.getX;
console.log(unboundGetX());

console.log(unboundGetX.bind(someThing)());
// console.log(boundGetX());
