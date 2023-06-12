#!/usr/bin/node
const process = require('process');
const argv = process.argv;
function fact(a) {
  if ((a === 1) || (a === 0)) {
    return (1);
  }
  return (a * fact(a - 1));
}
if (isNaN(argv[2])) {
  console.log('1');
} else {
  console.log(fact(parseInt(argv[2])));
}
