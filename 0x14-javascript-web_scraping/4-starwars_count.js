#!/usr/bin/node
let request = require('request');
let url = 'https://swapi-api.alx-tools.com/api/films/';
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const results = JSON.parse(body).results;
  console.log(results.reduce((count, movie) => {
    return movie.characters.find((character) => character.endsWith('/18/'))
      ? count + 1
      : count;
    }, 0));
  });
