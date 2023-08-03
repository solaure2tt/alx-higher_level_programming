#!/usr/bin/node
const request = require('request');
let fs = require('fs');
let url = process.argv[2]
request(url).pipe(fs.createWriteStream(process.argv[3]));
