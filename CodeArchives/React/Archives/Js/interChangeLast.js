let array = [2,3,1,6,5,9];
let f_element = array[0];
let l_element = array[array.length - 1];

array[array.length-1] = f_element;
array[0] = l_element;

console.log(array);
