#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const results = JSON.parse(body);
  const chars = results.characters;
  for (const c of chars) {
    request.get(c, function (err, res, bod) {
      if (err) {
        console.log(err);
      }
      const resus = JSON.parse(bod);
      console.log(resus.name);
    });
  }
});
