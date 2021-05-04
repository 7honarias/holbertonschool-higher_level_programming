#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
let numMoviesByCharter = 0;
request.get(url, function (err, response, body) {
  if (err) { console.log('Error: ' + err.message); }
  const films = JSON.parse(body).results;
  for (const film in films) {
    const listCharters = films[film].characters;
    for (const charters in listCharters) {
      if (listCharters[charters].includes('18')) {
        numMoviesByCharter++;
      }
    }
  }
  console.log(numMoviesByCharter);
});
