#!/usr/bin/node
// Print the response status code if a response was received
const request = require('request');

const mUrl = process.argv[2];
request(mUrl, function (error, response) {
  if (error) { console.log('code: ', error); }
  console.log('code:', response.statusCode);
});
