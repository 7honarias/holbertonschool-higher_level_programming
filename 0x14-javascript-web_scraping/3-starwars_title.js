#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const mUrl = 'https://swapi-api.hbtn.io/api/films/' + movieId;
request.get(mUrl, function (err, response, body) {
  if (err) { console.log('Error: ', err); }
  const filejson = JSON.parse(body);
  console.log(filejson.title);
});
