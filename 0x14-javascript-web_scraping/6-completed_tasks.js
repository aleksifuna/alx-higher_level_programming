#!/usr/bin/node
// computes the number of tasks completed by a user.id

const req = require('request');
const args = process.argv;

req(args[2], (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const todoLists = JSON.parse(body);
  const completed = {};
  todoLists.forEach((todo) => {
    if (todo.completed && completed[todo.userId] === undefined) {
      completed[todo.userId] = 1;
    } else if (todo.completed) {
      completed[todo.userId] += 1;
    }
  });
  console.log(completed);
});
