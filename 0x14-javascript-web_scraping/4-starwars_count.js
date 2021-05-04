#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const characterId = 'https://swapi-api.hbtn.io/api/people/18/';
let numMoviesByCharter = 0;
request.get(url, function (err, response, body) {
  if (err) { console.log('Error: ' + err.message); }
  const films = JSON.parse(body);
  for (const film in films.results) {
    const listCharters = films.results[film].characters;
    if (listCharters.indexOf(characterId) !== -1) {
      numMoviesByCharter += 1;
    }
  }
  console.log(numMoviesByCharter);
});
