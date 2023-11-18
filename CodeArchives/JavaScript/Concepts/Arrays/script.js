// -------------------------- Array.from -------------------------------

const someString = 'string';
const arrayFromString = Array.from(someString);
// console.log(arrayFromString);

const allListItems = document.querySelectorAll('li');
// console.log(allListItems);

const arrayFromNodeList = Array.from(allListItems);
// console.log(arrayFromNodeList);

// -------------------------- Array(shift, unshift) -------------------------------

const hobbies = ['Sports', 'Music'];
hobbies.unshift('Coding');
hobbies.shift(); // basically removes the first element
// console.log(hobbies);

// -------------------------- Array(splice) -------------------------------

const numbers = [1, 2, 3, 4, 5, 6, 7];
// numbers.splice(2, 0, 13,14); // To add from index 2
numbers.splice(-3, 3); // To remove two elements from index 0
// console.log(numbers);

// -------------------------- Array(slice) -------------------------------

const largeArray = [1, 2, 3, 4, 5, 6, 7];
const smallArray = largeArray.slice(-4, -1);
// console.log(smallArray);

// -------------------------- Array(find, findIndex) -------------------------------

const userData = [
  {
    id: 1,
    name: 'Sriram',
  },
  {
    id: 2,
    name: 'Mani',
  },
];

const userToLookFor = userData.find((user, idx, allUsers) => {
  return user.id === 2;
});
// console.log(userToLookFor);

const userIdxToLookFor = userData.findIndex((user, idx, allUsers) => {
  return user.id === 1;
});
// console.log(userIdxToLookFor);

// -------------------------- Array(forEach) -------------------------------

const expenses = [1200, 1000, 9800];
const someThing = expenses.forEach((expense, idx, expenses) => {
  return idx;
});
// console.log(someThing); // undefined as forEach won't return

// -------------------------- Array(map) -------------------------------

const prices = [1000, 5000, 8000];
const taxAmount = 2.44;

const taxAddedPrices = prices.map((price, idx, prices) => {
  return price * taxAmount;
});
// console.log(taxAddedPrices);

// -------------------------- Array(sort, reverse) -------------------------------

const unconventionalArray = [2, 99, 45, 789, 1, 1002];
const sortedArray = unconventionalArray.sort((a, b) => {
  // because sort takes each elements as string and compares
  if (a > b) {
    return 1;
  } else if (a === b) {
    return 0;
  } else {
    return -1;
  }
});
// console.log(sortedArray);
// console.log(sortedArray.reverse());

// -------------------------- Array(filter) -------------------------------

const ages = [12, 13, 25, 34, 39, 33, 18];
const filteredAges = ages.filter((age, idx, ages) => {
  return age > 18;
});
// console.log(filteredAges);

// -------------------------- Array(reduce) -------------------------------

const objectIds = [1, 4, 5, 2, 3, 6];
const reducedValue = objectIds.reduce((prevVal, currVal, idx, fullArray) => {
  return prevVal + currVal;
}, 0);
// console.log(reducedValue);

// -------------------------- Array(...spread) -------------------------------

const arrayOfObjects = [
  {
    id: 1,
    name: 'Sriram',
  },
  {
    id: 2,
    name: 'Mani',
  },
];

const copiedObjects = arrayOfObjects.map(data => ({
  id: data.id,
  name: data.name,
})); // To also copy the objects inside not the reference
arrayOfObjects[0].id = 100;
// console.log(copiedObjects);

// -------------------------- Array(destructuring) -------------------------------

const bunchOfData = [1, 'Sriram', 'somewhere on the earth'];
const [id, name] = bunchOfData;
// console.log(`Id is ${id} and name is ${name}`);

// -------------------------- Set in JS -------------------------------

const arrayArgument = [2,3,4,3,5,2,1];
const sampleSet = new Set(arrayArgument);
// console.log(sampleSet);

const firstKey = 'foreign';
const secondKey = 'primary';

const dynamicObject = {
  [firstKey]: 'Mysql',
  [secondKey]: 'Postgres'
}

console.log(dynamicObject['foreign']);
