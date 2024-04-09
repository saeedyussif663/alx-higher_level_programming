#!/usr/bin/node

const Rectangle = class {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
      this.print = function () {
        for (let index = 0; index < h; index++) {
          console.log('X'.repeat(w));
        }
      };
    }
  }
};

module.exports = Rectangle;
