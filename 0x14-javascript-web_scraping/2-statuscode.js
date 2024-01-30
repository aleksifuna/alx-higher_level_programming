#!/usr/bin/node
// displays the status code of a GET request

const args = process.argv;
const req = require('request');

req(args[2], (err, response) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log('code:', response.statusCode);
});
