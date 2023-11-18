const numbers = [4, 5, 6, 3, 2, 1, 3, 9];

const findSmallestNumber = array => {
    let smallNumber = array[0];
    for(const num of array) {
        if (num < smallNumber) {
            smallNumber = num;
        }
    }

    return smallNumber;
}

console.log(findSmallestNumber(numbers));

