#!/usr/bin/node

exports.esrever = function (list) {
  const reversed = [];
  for (let index = list.length - 1; index >= 0; index--) {
    reversed.push(list[index]);
  }
  return reversed;
};
