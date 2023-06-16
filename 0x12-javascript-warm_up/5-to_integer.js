#!/usr/bin/node
const process = require('process');
const argv = process.argv;
if (!isNaN(argv[2])) {
  console.log('My number: ' + parseInt(argv[2]));
} else {
  console.log('Not a number');
}
