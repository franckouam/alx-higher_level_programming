#!/usr/bin/node

const dict = require('./101-data').dict;
const res = {};
for (const item in dict) {
  if (!(dict[item] in res)) {
    res[dict[item]] = [item];
  } else {
    res[dict[item]].push(item);
  }
}
console.log(res);
