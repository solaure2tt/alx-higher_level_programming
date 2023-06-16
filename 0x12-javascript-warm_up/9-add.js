#!/usr/bin/node
const process = require('process');
const argv = process.argv;
function add (a, b) {
  return (a + b);
}
const som = add(parseInt(argv[2]), parseInt(argv[3]));
console.log(som);
