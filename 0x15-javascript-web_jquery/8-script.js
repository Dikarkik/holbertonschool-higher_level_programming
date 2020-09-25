// Script that fetches and lists the title for all movies
// by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
// All movie titles must be list in the HTML tag UL#list_movies

const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

$.get(url, function (data) {
  const movies = data.results;
  for (movie of movies)
    $('UL#list_movies').append('<li>' + movie.title + '</li>');
});
