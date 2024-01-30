#!/usr/bin/node
// counts the number of times wedges Antilles is present in a movie

const args = process.argv;
const req = require('request');

req(args[2], (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const jsonResponse = JSON.parse(body);

  const movies = jsonResponse.results;

  const count = movies.reduce((totalCount, movie) => {
    const present = movie.characters.some((character) => character.endsWith('/18/'));
    return present ? totalCount + 1 : totalCount;
  }, 0);
  console.log(count);
});
