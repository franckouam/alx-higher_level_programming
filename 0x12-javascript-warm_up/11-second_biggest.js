#!/usr/bin/node

const n = process.argv.length;
if (n < 4) {
  console.log(0);
} else {
  let max = parseInt(process.argv[2]);
  let max2 = parseInt(process.argv[n - 1]);
  for (let i = 3; i < n; i++) {
    const a = parseInt(process.argv[i]);
    if (a > max) {
      max2 = max;
      max = a;
    } else if (a > max2) {
      max2 = a;
    }
  }
  console.log(max2);
}
