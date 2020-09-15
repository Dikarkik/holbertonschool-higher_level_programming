#!/usr/bin/node

const argc = process.argv.length;

if (argc < 4) {
  console.log(0);
} else {
  const numbers = process.argv.slice(2).sort();
  console.log(numbers[numbers.length - 2]);
}
