#!/usr/bin/node

const dict = require('./101-data').dict;

const occurrences = {};
for (const [key, value] of Object.entries(dict)) {
  if (occurrences[value] === undefined) {
    occurrences[value] = [key];
  } else {
    occurrences[value].push(key);
  }
}

console.log(occurrences);
