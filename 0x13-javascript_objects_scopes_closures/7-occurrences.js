#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let total = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) { total++; }
  }
  return total;
};
