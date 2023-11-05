value = 21;
value = value + 'dot';
console.log(value);
console.log(typeof value);

let someRandomObject = {
  name: 'Sriram',
  getName: function () {
    console.log(this.name);
  },
};

// someRandomObject.getName();

setTimeout(someRandomObject.getName, 1000);

let someTempFunction = someRandomObject.getName;

setTimeout(someTempFunction, 100);

// let person = {
//     name: 'John Doe',
//     getName: function() {
//         console.log(this.name);
//     }
// };

// setTimeout(person.getName, 1000);

let someString = 'Bijili';

function Person(first, last, age, eye) {
  this.firstName = first;
  this.lastName = last;
  this.age = age;
  this.eyeColor = eye;
}

/*
  class Person:
	  def __init__(self, fn, ln, age, ec):
		  self.fn = fn
		  self.ln = ln
		  self.age = age
		  self.ec = ec
  
  instance = Person("John", "Doe", 50, "blue")
  */

Person.prototype.newProperty = 'somevalue';

const myFather = new Person('John', 'Doe', 50, 'blue');
// console.log(myFather.newProperty);

const typicalObject = {
  name: 'Sriram',
  age: 23,
  place: 'TM',
  getName: function () {
    return this.name;
  },
  setName: function (newName) {
    this.name = newName;
  },
};

// typicalObject.setName('Varsha');
// console.log(typicalObject.getName());

const uniqueElements = array => {
  const uniqueArray = [];
  for (let element of array) {
    if (!uniqueArray.includes(element)) {
      uniqueArray.push(element);
    } else {
      return false;
    }
  }
  return true;
};

const array = [2, 4, 5, 5, 7, 9];
console.log(uniqueElements(array));
