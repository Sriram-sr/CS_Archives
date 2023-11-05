let array = [2,3,4,5];

const demo = array.reduce( (prev, curr, idx, arr) => {
	//console.log('prev ', prev);
	//console.log('curr ', curr);
	//console.log('idx ', idx);
	return prev-curr; 
}
,2);

//console.log(demo);

const getMax = (a, b) => {
	console.log(a);
        return Math.max(a, b);
}
// callback is invoked for each element in the array starting at index 0
const answer = [1, 100].reduce(getMax, 50); // 100

console.log(answer);
