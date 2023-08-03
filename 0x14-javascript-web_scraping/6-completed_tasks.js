#!/usr/bin/node
let request = require('request');
let url = 'https://jsonplaceholder.typicode.com/todos';
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const results = JSON.parse(body)
  let completed = {};
  results.forEach((r) => {
    if (r.completed && completed[r.userId] === undefined) {
      completed[r.userId] = 1;
    } else if (r.completed) {
        completed[r.userId] += 1;
      }
    });
    console.log(completed);
});
