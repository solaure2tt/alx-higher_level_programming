#!/usr/bin/node
const process = require('process');
const argv = process.argv;
if (!isNaN(argv[2])) {
  for (let i = 0; i < parseInt(argv[2]); i++) {
    let squ = '';
    for (let j = 0; j < parseInt(argv[2]); j++) {
      squ = squ + 'X';
    }
    console.log(squ);
  }
} else {
  console.log('Missing size');
}
