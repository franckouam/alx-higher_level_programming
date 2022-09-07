#!/usr/bin/node

exports.converter = function (base) {
  return (nbr) => {
    return nbr.toString(base);
  };
};
