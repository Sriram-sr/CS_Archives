const addMovieBtn = document.getElementById('add-movie-btn');
const searchBtn = document.getElementById('search-btn');
const movieList = document.getElementById('movie-list');

const movies = [];

const renderMovies = (filterString = '') => {
  console.log(movies, filterString);
  if (movies.length === 0) {
    movieList.classList.remove('visible');
  } else {
    movieList.classList.add('visible');
  }
  movieList.innerHTML = '';
  const filteredMovies = !filterString
    ? movies
    : movies.filter(movie =>
        movie.info.title.toLowerCase().includes(filterString.toLowerCase())
      );
  filteredMovies.forEach(movie => {
    const movieElement = document.createElement('li');
    movieElement.textContent = movie.info.title;
    movieList.appendChild(movieElement);
  });
};

const addMovieHandler = () => {
  const title = document.getElementById('title').value;
  const extraName = document.getElementById('extra-name').value;
  const extraValue = document.getElementById('extra-value').value;

  const movie = {
    info: {
      title,
      [extraName]: extraValue,
    },
    id: Math.random().toString(),
  };
  movies.push(movie);
  renderMovies();
};

const searchMovieHandler = () => {
  const searchString = document.getElementById('filter-title').value;
  renderMovies((filterString = searchString));
};

addMovieBtn.addEventListener('click', addMovieHandler);
searchBtn.addEventListener('click', searchMovieHandler);

// -------------------------- Object Destructuring -------------------------------

let person = {
  firstName: 'John',
  lastName: 'Doe',
};

const { firstName: fname, lastName: lname } = person; // This is like desctructure and rename in a name I give.
// console.log(fname, lname);

// -------------------------- Checking 'in' -------------------------------

const personData = {
  id: 1,
  info: {
    name: 'Sriram',
    age: 23,
  },
  bgnd: 'Python',
  describeBehaviour() {
    console.log(this);
    return `Background is ${this.bgnd}`;
  },
};
// console.log(('info' in personData));

// -------------------------- 'this' -------------------------------

// console.log(personData.describeBehaviour());

let { describeBehaviour } = personData;
describeBehaviour = describeBehaviour.bind(personData); // Meaning is eventhough the fn is pulled off object, bind the fn.
// console.log(describeBehaviour());
// console.log(describeBehaviour.call(personData));  // Can also use call instead for bind

const teamData = {
  get title() {
    return this._title;
  },

  set title(value) {
    this._title = value;
  },
  teamName: 'CSK',
  members: ['Raina', 'Dhoni', 'Bravo'],
  getTeamAndMembers() {
    this.members.forEach(function(member) {
      console.log(this);
      console.log(this.teamName + ' - '+ member);
    });
  }
}

teamData.title = 'return';
console.log(teamData.title);
