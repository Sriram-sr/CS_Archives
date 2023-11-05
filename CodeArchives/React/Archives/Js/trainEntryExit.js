let entry = [7,0,5,1,3];
let exit = [1,2,1,3,4];
let passCount = 0;
let pass_list = [];

entry.forEach( (val,idx) => {
	passCount+=entry[idx];
	passCount-=exit[idx];
	pass_list.push(passCount);
});

console.log(pass_list);
let max_val = pass_list.reduce( (prev, curr) => {
	console.log('prev ', prev , ' curr', curr);
	return Math.max(prev, curr);
},9);

console.log(max_val);

let max = pass_list[0];
for(let val of pass_list){
	if(val>max){
		max = val;
	}
}

console.log(max);
