#!/usr/bin/node
var request = require('request');
request(process.argv[2], function (error, response, body) {
  console.log('code: ' + response.statusCode);
  });
