#!/usr/bin/node
const arrArg = process.argv.slice(2);
let str = '';
fs = require('fs');

fs.readFile(arrArg[0], 'utf8', function(err, data){
  return data;
});

console.log(str);
