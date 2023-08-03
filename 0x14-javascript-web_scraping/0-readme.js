#!/usr/bin/node
let fs = require('fs');
let file = process.argv[2];
fs.readFile (file, 'utf-8', (error, text) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log(text);
});
