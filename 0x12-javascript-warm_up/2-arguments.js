#!/usr/bin/node

const n = process.argv.length;
if (n > 2) {
  if (n === 3) {
    console.log('Argument found');
  } else {
    console.log('Arguments found');
  }
} else {
  console.log('No argument');
}
