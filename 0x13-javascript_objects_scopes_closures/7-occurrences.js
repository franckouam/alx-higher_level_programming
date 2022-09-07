#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let nbr = 0;
  list.forEach((item) => {
    if (item === searchElement) {
      nbr++;
    }
  });
  return nbr;
};
