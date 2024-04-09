#!/usr/bin/node

const Rectangle = require('./4-rectangle');

const Square = class extends Rectangle {
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
