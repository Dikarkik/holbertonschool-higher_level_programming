#!/usr/bin/node

exports.callMeMoby = function (x, someFunction) {
  for (let i = 0; i < x; i++) {
    someFunction();
  }
};
