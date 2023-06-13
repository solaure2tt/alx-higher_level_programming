#!/usr/bin/node
exports.esrever = function (list) {
  let i = 0;
  let x;
  let j = list.length - 1;
  while (i <= j) {
    x = list[i];
    list[i] = list[j];
    list[j] = x;
    i = i + 1;
    j = j - 1;
  }
  return (list);
};
