#!/usr/bin/node
let fs = require('fs');
let file = process.argv[2];
let data = process.argv[3]
fs.writeFile (file, data, (err) => {
  if (err) {
    console.log(err);
    return;
  }
});
