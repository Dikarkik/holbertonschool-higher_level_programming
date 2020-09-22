#!/usr/bin/node
// Script that prints the number of movies
// where the character “Wedge Antilles” is present.
// Wedge Antilles is character ID 18
// ./4-starwars_count.js https://swapi-api.hbtn.io/api/films

const request = require('request');
const url = process.argv[2];
const characterId = 18;

request(url, function (error, response, body) {
  if (error) { return (console.log(error)); }

  const movies = JSON.parse(body).results;
  let count = 0;

  for (const movie of movies) {
    if (movie.characters.includes('https://swapi-api.hbtn.io/api/people/' + characterId + '/')) { count++; }
  }
  console.log(count);
});
