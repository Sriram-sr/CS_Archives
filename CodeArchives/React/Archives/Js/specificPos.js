let array = [23, 65, 19, 90];
let pos1 = 1;
let pos2 = 3;

let val1 = array[pos1-1];
let val2 = array[pos2-1];

array[pos2-1] = val1;
array[pos1-1] = val2;

console.log(array);
