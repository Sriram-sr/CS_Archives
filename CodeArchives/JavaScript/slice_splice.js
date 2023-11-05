/**  Splice method

array.splice(index, howmany, item1, ....., itemX)

howmany stands for how many elements to remove, if you give more than 2 params, then values will be addes from
idx of your first idx specified **/

let someArray = [8,3,1,6,0];
// someArray.splice(2,1);  // from 2nd index 1 value will be removed
someArray.splice(1,0,99,88); // from 1nd idx doesn't remove anything just add two values 99 and 88
// console.log(someArray);

/** Slice method 
  slice method is for slicing the array to specific elements
 * */

let newArray = [2,4,6,1,5,9];
slicedArray = newArray.slice(1,4);
newSliced = newArray.slice(-3,-1);
// console.log(slicedArray);
console.log(newSliced);
