#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const mUrl = process.argv[2];
const filePage = process.argv[3];
request.get(mUrl, function (err, response, body) {
  if (err) { console.log('Error: ', err); }
  fs.writeFile(filePage, body, 'utf8', function (err) {
    if (err) {
      console.log(err.message);
    }
  });
});
