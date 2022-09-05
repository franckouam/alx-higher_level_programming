#!/usr/bin/node

const n = process.argv.length;
if (n > 2) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
