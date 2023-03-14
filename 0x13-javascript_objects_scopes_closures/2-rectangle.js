#!/usr/bin/node
module.exports = Class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.weight = w;
      this.height = h;
    }
  };
