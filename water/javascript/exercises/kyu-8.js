'use strict';

function findNeedle(haystack) {
  return 'found the needle at position ' + haystack.indexOf('needle');
}

// Apparently eval is not recommended, using switch instead.
function basicOp(operation, value1, value2) {
  switch (operation) {
    case '+':
      return value1 + value2;
    case '-':
      return value1 - value2;
    case '*':
      return value1 * value2;
    case '/':
      return value1 / value2;
    default:
      return 0;
  }
}

function noSpace(x) {
  return x.replace(/\s+/g, '');
}

function stringReverse(str) {
  [...str].reverse().join('');
}

const removeChar = str => str.slice(1, -1);

// getCount Returns number of voewls in a given string (assumes lowercase, a-z only.)
const getCount = str => (str.match(/[aeiou]/g) || []).length;

// longest returns a sorted string that consists of the longest
// sequence of distinct characters coming from both strings.
const longest = (s1, s2) => [...new Set(s1 + s2)].sort().join('');

const oddOrEven = arr => (arr.reduce((a, b) => a + b, 0) % 1 ? 'even' : 'odd');
