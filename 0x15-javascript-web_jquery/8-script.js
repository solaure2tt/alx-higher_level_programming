$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (movies) {
  $('UL#list_movies').append(...movies.results.map(movie => `<li>${movie.title}</li>`));
});
