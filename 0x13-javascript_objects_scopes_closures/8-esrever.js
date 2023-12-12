#!/usr/bin/node
exports.esrever = function (list) {
  let idx = list.length - 1;
  const newArray = [];
  while (idx >= 0) {
    newArray.push(list[idx]);
    idx--;
  }
  return newArray;
};
