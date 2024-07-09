const moviesLi = document.getElementById('list_movies');

//make fetch to api
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
      const movies = data.results;
      movies.forEach(movie => { 
        const li = document.createElement('li');
        li.textContent = movie.title;
        moviesLi.appendChild(li);
      });
    })
    .catch(err => {
      console.error("Err fetch movies", err);
  });
