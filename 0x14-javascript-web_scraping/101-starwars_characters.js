#!/usr/bin/node
// prints all characters of a Star wars movie
const req = require('request');
const args = process.argv;
const url = 'https://swapi-api.alx-tools.com/api/films/' + args[2] + '/';

(async () => {
  try {
    const body = await makeRequest(url);
    const movie = JSON.parse(body);
    const charUrl = movie.characters;
    await printCharacters(charUrl, 0);
  } catch (err) {
    console.log(err);
  }
})();

async function makeRequest (url) {
  return new Promise((resolve, reject) => {
    req(url, (err, reponse, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(body);
      }
    });
  });
}

async function printCharacters (characters, index) {
  try {
    const body = await makeRequest(characters[index]);
    console.log(JSON.parse(body).name);
    if (index + 1 < characters.length) {
      await printCharacters(characters, index + 1);
    }
  } catch (error) {
    console.log(error);
  }
}
