const reverseArray = () => {
  list = [4, 5, 6, 7, 8, 9];
  reversed = [];
  let idx;

  for (idx = list.length - 1; idx >= 0; idx--) {
    reversed.push(list[idx]);
  }

  console.log(reversed);
};

const sumElements = () => {
    test_list = [12, 67, 98, 34];
    sumArray = [];
    for(let val of test_list){
        val = val.toString();
        let temp = 0;
        for(let char=0;char<val.length;char++){
            temp = temp + (+val[char]);
        }
        sumArray.push(temp);
    }
    console.log(sumArray);
}

sumElements();