function swap_first_last() {
  let numbers = [2, 3, 4, 7, 1, 33, 98];
  length = numbers.length;
  first = numbers[0];
  last = numbers[length - 1];

  numbers[0] = last;
  numbers[length - 1] = first;

  console.log(typeof numbers);
}

let swap_any = () => {
    let List = [23, 65, 19, 90], pos1 = 1, pos2 = 3;
    temp = List[pos1];
    List[pos1] = List[pos2];
    List[pos2] = temp;
    console.log(List);
}

let replaceChars = () => {
    let stringList = ['Gfg', 'is', 'best', 'for', 'Geeks'];
    stringList.forEach((sub, idx)=>{
        sub = sub.replace(/G/g, '-');
        sub = sub.replace(/e/g, 'G');
        sub = sub.replace(/-/g, 'e');
        stringList[idx] = sub;
    });
    console.log(stringList);
}

replaceChars();
