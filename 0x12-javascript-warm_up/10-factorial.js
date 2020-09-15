#!/usr/bin/node

const number = parseInt(process.argv[2]);

function fac (num) {
  if (num === 1) { return (num); }
  const next = fac(num - 1);
  return (num * next);
}

if (isNaN(number)) {
  console.log(1);
} else if (number <= 1) {
  console.log(1);
} else {
  console.log(fac(number));
}
