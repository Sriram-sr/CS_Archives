const button = document.querySelector('button');

const SELECTION_ROCK = 'ROCK';
const SELECTION_PAPER = 'PAPER';
const SELECTION_SCISSOR = 'SCISSOR';
const DEFAULT_SELECTION = SELECTION_ROCK;

const getPlayerSelection = () => {
    let userSelection = prompt('Enter your choice...', '').toUpperCase();
    if (userSelection !== SELECTION_ROCK && userSelection !== SELECTION_PAPER && userSelection !== SELECTION_SCISSOR) {
        console.log(`We selected ${DEFAULT_SELECTION} for you...`);
        userSelection = DEFAULT_SELECTION;
    }
    console.log(userSelection);
}

button.addEventListener('click', getPlayerSelection);


const defaultArgFunction = (...onlyArg) => {
    if (onlyArg) {
        console.log(typeof onlyArg);
    }
}

defaultArgFunction();