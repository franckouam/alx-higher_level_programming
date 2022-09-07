#!/usr/bin/node

let nbr = 0;
exports.logMe = function (item) {
  console.log(`${nbr}: ${item}`);
  nbr++;
};
