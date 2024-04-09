#!/usr/bin/node

const Square5 = require('./5-square');

const Square = class extends Square5 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      for (let index = 0; index < this.height; index++) {
        console.log('X'.repeat(this.width));
      }
    } else {
      for (let index = 0; index < this.height; index++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};

module.exports = Square;
