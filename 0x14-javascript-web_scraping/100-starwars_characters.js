#!/usr/bin/node
// prints all characters of a Star wars movie
const req = require('request');
const args = process.argv;
const url = 'https://swapi-api.alx-tools.com/api/films/' + args[2] + '/';

req(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const movie = JSON.parse(body);
  const characterUrls = movie.characters;
  characterUrls.forEach((charUrl) => {
    req(charUrl, (err, resp, body) => {
      if (err) {
        console.log(err);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  });
});
