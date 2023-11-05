const removeItem = (list, match) => {
  let removedArray = [];
  for (let value of list) {
    if (value != match) {
      removedArray.push(value);
    }
  }
  return removedArray;
};

const maxFinder = (list) => {
  let max_value = list[0];

  for (let value of list) {
    if (value > max_value) {
      max_value = value;
    }
  }

  return max_value;
};

let list1 = [10, 20, 4, 45, 99];
max_value = maxFinder(list1);
list1 = removeItem(list1, max_value);
let second_max = maxFinder(list1);
console.log(second_max);
