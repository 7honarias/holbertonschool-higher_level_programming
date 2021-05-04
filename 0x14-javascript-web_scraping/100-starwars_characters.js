#!/usr/bin/node
const request = require('request');

const filmId = process.argv[2];
const mUrl = 'https://swapi-api.hbtn.io/api/films/' + filmId;
request.get(mUrl, function (err, response, body) {
  if (err) {
    console.log(err.message);
  }
  const filmCharacters = JSON.parse(body).characters;

  for (const characters in filmCharacters) {
    request.get(filmCharacters[characters], function (err, response, body) {
      if (err) {
        console.log(err.message);
      }
      const result = JSON.parse(body);
      console.log(result.name);
    });
  }
});
