#!/usr/bin/node
// displays the status code of a GET request

const args = process.argv;
const req = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + args[2];
req(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(JSON.parse(body).title);
});
