#!/usr/bin/node

const list = require('./100-data').list;
const res = list.map((item, i) => item * i);
console.log(list);
console.log(res);
