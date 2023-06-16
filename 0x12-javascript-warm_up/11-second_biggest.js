#!/usr/bin/node
const process = require('process');
const argv = process.argv;
if (argv.length < 3) {
  console.log('0');
} else if (argv.length === 3) {
  console.log('0');
} else {
  let max = parseInt(argv[2]);
  let i = 2;
  let sec;
  argv.forEach((val, index) => {
    if (index > 2) {
      if (max < parseInt(val)) {
        max = parseInt(val);
      }
    }
  })
  while ((i < argv.length) && (max < parseInt(argv[i]))) {
    i = i + 1;
  }
  if (i < argv.length) {
    sec = parseInt(argv[i]);
    argv.forEach((val, index) => {
      if (index > 1) {
        if ((sec <  parseInt(val)) && (parseInt(val) < max)) {
          sec = parseInt(val);
        }
      }
    })
  } else {
    sec = 0;
    }
    console.log(sec);
}
