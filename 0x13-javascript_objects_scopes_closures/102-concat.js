#!/usr/bin/node
const arrArg = process.argv.slice(2);

const ff = require('fs');
const fs = require('fs');

fs.readFile(arrArg[0], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  }
  ff.readFile(arrArg[1], 'utf8', function (err2, data2) {
    if (err2) {
      console.log(err2);
    }
    console.log(data + data2);
  });
});
