import React, { useEffect, useState, useCallback } from 'react';
import AddMovie from './components/AddMovie';
import MoviesList from './components/MoviesList';

function App() {
  const [movies, setMovies] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setError] = useState();
  // const fetchHandler = () => {
  // fetch('https://swapi.dev/api/films').then(response => {
  //   return response.json();
  // }).then(data => {
  //   const tranformedMovies = data.results.map(movie => {
  //     return {
  //       id: movie.episode_id,
  //       title: movie.title,
  //       openingText: movie.opening_crawl,
  //       releaseDate: movie.release_date
  //     };
  //   });
  //   setMovies(tranformedMovies);
  // });
  // }

  const fetchHandler = useCallback(async () => {
    try {
      setIsLoading(true);
      // const response = await fetch('https://swapi.dev/api/films/');
      const response = await fetch('https://react-http-8b743-default-rtdb.firebaseio.com/movies.json')
      if(!response.ok){
        throw new Error('Something went wrong');
      }
      
      const data = await response.json();
      console.log(data);
      const loadedMovies = [];
      for(const key in data){
        loadedMovies.push({
          id: key,
          title: data[key].title,
          openingText: data[key].openingText,
          releaseDate: data[key].releaseDate,
        });
      }

      // const retrievedData = movies.map(movie => {
      //   return {
      //     id: movie.key,
      //     title: movie.title,
      //     releaseDate: movie.release_date,
      //     openingText: movie.opening_crawl
      //   }
      // });
      setMovies(loadedMovies);
    }catch (error){
        console.log(error.message);
        setError(error.message);
    }
    setIsLoading(false);
  }, []);

  useEffect( () => {
    fetchHandler();
  }, [fetchHandler]);

  const addMovieHandler = async(movie) => {
    const response = await fetch('https://react-http-8b743-default-rtdb.firebaseio.com/movies.json', {
      method: 'POST',
      body: JSON.stringify(movie),
      headers: {
        'Content-Type': 'application/json'
      }
    });
    const data = await response.json();
  };

  return (
    <React.Fragment>
      <section>
        <AddMovie onAddMovie={addMovieHandler}/>
      </section>
      <section>
        <button onClick={fetchHandler}>Fetch Movies</button>
      </section>
      <section>
        {isLoading && <p>Loading!!!</p>}
        {!isLoading && !errorMessage && movies.length === 0 && <p>No Movies Found</p>}
        {!isLoading && movies.length > 0 && <MoviesList movies={movies} />}
        {!isLoading && errorMessage && <p>{errorMessage}</p>}
      </section>
    </React.Fragment>
  );
}

export default App;
