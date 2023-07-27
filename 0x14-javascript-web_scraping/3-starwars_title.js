#!/usr/bin/node
var request = require('request');
let id = process.argv[2];
let url = 'https://swapi-api.alx-tools.com/api/films/' + id;
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log(JSON.parse(body).title);
  });
