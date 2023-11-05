let button = document.querySelector('button');
let numTotalCount = 0;

let buttonClickHandler = () => {
  console.log('Button clicked');
};

button.addEventListener('click', buttonClickHandler);

for (let n = 0; n < 100000; n++) {
  numTotalCount += n;
}

console.log(numTotalCount);


