function secondLargest(array){
	array.sort()
	return array[array.length-2];
}

let array = [2,3,8,1,4];
console.log(secondLargest(array))
