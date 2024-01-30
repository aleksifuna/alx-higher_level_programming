#!/usr/bin/node
// streams the response of a website to a file

const args = process.argv;
const req = require('request');
const fs = require('fs');

req(args[2]).pipe(fs.createWriteStream(args[3]));
