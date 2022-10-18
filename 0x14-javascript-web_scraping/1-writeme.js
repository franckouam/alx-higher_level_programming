#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const str = process.argv[3];

try {
  fs.writeFile(file, str, (err) => {});
} catch (err) {
  console.log(`${err}`);
}
