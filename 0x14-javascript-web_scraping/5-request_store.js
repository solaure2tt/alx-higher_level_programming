#!/usr/bin/node
const request = require('request');
var fs = require('fs');
let url = process.argv[2]
request(url).pipe(fs.createWriteStream(process.argv[3]));
