#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line = line + 'X';
      }
      console.log(line);
    }
  }

  rotate() {
    const x = this.width;
    this.width = this.height;
    this.height = x;
  }

  double() {
   this.width = this.width * 2;
   this.height = this.height * 2;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint(c) {
    if (typeof c === 'undefined') {
      this.print();
    } else {
      for (let i = 0; i < this.size; i++) {
        let line = '';
        for (let j = 0; j < this.size; j++) {
          line = line + c;
        }
        console.log(line);
      }
    }
  }
}
module.exports = Square;
