#!/usr/bin/node

const Square = require('./5-square');

module.exports = class Square2 extends Square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) { c = 'X'; }

    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
