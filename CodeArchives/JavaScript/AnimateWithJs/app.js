let moveForward = true;
let lastPosition = null;

let executeAnimation = () => {
  let innerBox = document.querySelector('.inner-box');
  let intervalMonitor;

  intervalMonitor = setInterval(moveElement, 5);
  let position = 0;
  function moveElement() {
    if (moveForward) {
      if (position == 350) {
        clearInterval(intervalMonitor);
        moveForward = false;
        lastPosition = position;
      } else {
        position++;
        innerBox.style.top = position + 'px';
        innerBox.style.left = position + 'px';
      }
    } else {
      if (lastPosition == 0) {
        clearInterval(intervalMonitor);
        moveForward = true;
      } else {
        lastPosition--;
        innerBox.style.top = lastPosition + 'px';
        innerBox.style.left = lastPosition + 'px';
      }
    }
  }
};

let animateButton = document.querySelector('button');
animateButton.addEventListener('click', executeAnimation);
