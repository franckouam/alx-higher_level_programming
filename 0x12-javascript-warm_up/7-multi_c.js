#!/usr/bin/node

if (process.argv.length > 2) {
  const n = parseInt(process.argv[2]);
  if (!isNaN(n)) {
    for (let i = 0; i < n; i++) {
      console.log('C is fun');
    }
  }
} else {
  console.log('Missing number of occurrences');
}
