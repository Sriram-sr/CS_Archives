let array = [2, 3, 10];

for(let idx=0;idx<array.length;idx++){
    let competitor = array[idx];
    console.log(competitor);
    let start = array.slice(0,idx);
    let end = array.slice(idx+1);
    let combined = start.concat(end);
    console.log('start', start);
    console.log('Combined', combined);
    console.log('end', end);
    let sum = combined.reduce((prev, curr)=> prev+=curr, 0);
    console.log(sum);
    
}


