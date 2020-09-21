#!/usr/bin/node

exports.converter = function (base) {
  function numberConverter (number) {
    return number.toString(base);
  }
  return numberConverter;
};
