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
  printCharacters(characterUrls, 0);
});

function printCharacters (characters, index) {
  req(characters[index], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    console.log(JSON.parse(body).name);
  });
  if (index + 1 < characters.length) {
    printCharacters(characters, index + 1);
  }
}
