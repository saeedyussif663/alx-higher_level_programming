#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurence = 0;
  list.forEach((item) => {
    if (item === searchElement) {
      occurence++;
    }
  });
  return occurence;
};
