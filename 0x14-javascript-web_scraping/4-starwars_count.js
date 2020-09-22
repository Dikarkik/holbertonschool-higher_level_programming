#!/usr/bin/node
// Script that prints the number of movies
// where the character “Wedge Antilles” is present.
// Wedge Antilles is character ID 18
// ./4-starwars_count.js https://swapi-api.hbtn.io/api/films

const request = require('request');
const url = process.argv[2];

if (url) {
  request(url, function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const movies = JSON.parse(body).results;
      let count = 0;

      for (const movie of movies) {
        for (const character of movie.characters) {
          if (character.slice(-4) === '/18/') {
            count++;
          }
        }
      }
      console.log(count);
    }
  });
}
