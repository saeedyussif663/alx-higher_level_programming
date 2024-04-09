#!/usr/bin/node

const Rectangle = class {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
      this.print = function () {
        const i = 0;
        let j = h;
        while (i < j) {
          console.log('X'.repeat(w));
          j--;
        }
      };
    }
  }
};

module.exports = Rectangle;
