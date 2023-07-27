#!/usr/bin/node
var fs = require('fs');
var file = process.argv[2];
var data = process.argv[3]
fs.writeFile(file, data, (err) => {
  if (err) {
    console.log(err);
    return;
  }
});
