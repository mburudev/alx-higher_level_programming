#!/usr/bin/node
module.exports = class Rectangle {
  constructor(w, h) {
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // If w or h is not a positive integer, create an empty object.
      this.width = undefined;
      this.height = undefined;
    }
  }
};
