#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // If w or h is not a positive integer, create an empty object.
      this.width = undefined;
      this.height = undefined;
    }
  }

  print () {
    // Check if width and height are defined and greater than 0.
    if (this.width !== undefined && this.height !== undefined) {
      // Loop through rows and columns to print the rectangle.
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += 'X';
        }
        console.log(row);
      }
    } else {
      console.log('Empty Rectangle');
    }
  }
};
