#!/usr/bin/node

const fs = require('fs');

function concatFiles (fileDestiny, file) {
  fs.readFile(file, 'utf-8', function (err, data) {
    if (err) {
      return console.log(err);
    }
    fs.appendFile(fileDestiny, data, function (err, result) {
      if (err) console.log('error', err);
    });
  });
}

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileDestiny = process.argv[4];

concatFiles(fileDestiny, fileA);
concatFiles(fileDestiny, fileB);
