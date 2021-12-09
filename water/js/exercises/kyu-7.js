'use strict';

// const getDivisorsCnt = n => {
//   let count = 0;
//   [...Array(n ** 0.5 + 1).keys()].slice(1).reduce(a => {
//     if (!(n % a) && a) count++;
//   }, 0);
//   return count;
// };

const getDivisorsCnt = n => [...Array((n / 2) ^ 0)].reduce((pre, _, idx) => (n % ++idx ? pre : ++pre), 1);

// const nbDig = (n, d) => {
//   let count = 0;
//   for (let i = 0; i < n + 1; i++) {
//     const sq = String(i * i);
//     if (new Set(sq).has(String(d))) {
//       [...sq].forEach(e => {
//         if (e == d) count++;
//       });
//     }
//   }
//   return count;
// };

const nbDig = (n, d) => {
  let count = 0;
  for (let i = 0; i <= n; i++) count += [...(i * i + '')].filter(e => +e === d).length;
  return count;
};

// console.log(nbDig(5750, 0));

// function declareWinner(fighter1, fighter2, firstAttacker) {
//   const attack = (attacker, defender) => {
//     defender.health -= attacker.damagePerAttack;
//   };

//   const fight = (fighter1, fighter2) => {
//     attack(fighter1, fighter2);
//     return fighter2.health <= 0 ? fighter1.name : fight(fighter2, fighter1);
//   };

//   const [first, second] = fighter1.name === firstAttacker ? [fighter1, fighter2] : [fighter2, fighter1];

//   return fight(first, second);
// }

function declareWinner(fighter1, fighter2, firstAttacker) {
  const fac1 = Math.ceil(fighter1.health / fighter2.damagePerAttack);
  const fac2 = Math.ceil(fighter2.health / fighter1.damagePerAttack);
  return fac1 === fac2 ? firstAttacker : fac1 > fac2 ? fighter1.name : fighter2.name;
}

function Fighter(name, health, damagePerAttack) {
  this.name = name;
  this.health = health;
  this.damagePerAttack = damagePerAttack;
  this.toString = function () {
    return this.name;
  };
}

// console.log(declareWinner(new Fighter('Lew', 10, 2), new Fighter('Harry', 5, 4), 'Lew'));

// console.log(declareWinner(new Fighter('Lew', 10, 2), new Fighter('Harry', 5, 4), 'Harry'));

// console.log(declareWinner(new Fighter('Harald', 20, 5), new Fighter('Harry', 5, 4), 'Harry'));

// function stray(numbers) {
//   for (let i = 1; i < numbers.length; i++) {
//     const e = numbers[i];
//     if (e != numbers[i - 1] && e != numbers[i + 1]) return e;
//   }
//   return numbers[0];
// }

const stray = numbers => numbers.reduce((a, b) => a ^ b);

// console.log(stray([1, 1, 2]));

// const reverseLetter = str =>
//   [...str]
//     .reverse()
//     .join('')
//     .replace(/[^a-z]/g, '');

const reverseLetter = str => str.match(/[a-z]/g).reverse().join('');

const isAnagram = (test, original) => {
  const clean = str => [...str.toLowerCase()].sort().join('');
  return clean(test) === clean(original);
};

const number = busStops => busStops.reduce((rem, [on, off]) => rem + on - off, 0);

// console.log(
//   number([
//     [10, 0],
//     [3, 5],
//     [5, 8],
//   ])
// );

// const nums = [1, 2, 3, 10, 5];

const solution1 = nums => (nums ? nums.slice().sort((a, b) => a - b) : []);

const gimme = arr => arr.indexOf(arr.slice().sort((a, b) => a - b)[1]);

// console.log(gimme([2, 3, 1]));

function highAndLow(numbers) {
  numbers = numbers.split(' ').map(Number);
  return `${Math.max(...numbers)} ${Math.min(...numbers)}`;
}

// console.log(highAndLow('4 5 29 54 4 0 -214 542 -64 1 -3 6 -6'));

const findSum = n => {
  let sum = 0;
  for (let i = 1; i < n + 1; i++) {
    if (i % 3 === 0 || i % 5 === 0) sum += i;
  }
  return sum;
};

// console.log(findSum(5));

const isSortedAndHow = arr => {
  const asc = arr =>
    arr
      .slice()
      .sort((a, b) => a - b)
      .join('');
  if (asc(arr) === [...arr].join('')) return 'yes, ascending';
  const desc = arr =>
    arr
      .slice()
      .sort((a, b) => b - a)
      .join('');
  if (desc(arr) === [...arr].join('')) return 'yes, descending';
  return 'no';
};

// console.log(isSortedAndHow([1, 2]));
// console.log(isSortedAndHow([15, 7, 3, -8]));

const findLongest = arr => arr.reduce((c, v) => (`${c}`.length < `${v}`.length ? v : c));

// console.log(findLongest([1, 10, 100]));

const solution = (str, ending) => str.endsWith(ending);

// console.log(solution('abcde', 'cde'));
// console.log(solution('abcde', 'abc'));
// console.log(solution('abcde', ''));

const capitals = str => [...str].map((e, i) => (e.toUpperCase() === e ? i : '')).filter(e => e !== '');

// console.log(capitals('CodEWaRs'));

const vertMirror = str => str.map(e => [...e].reverse().join(''));

const horMirror = str => str.reverse();

const oper = (fn, str) => fn(str.split('\n')).join('\n');

// console.log(oper(vertMirror, 'hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu'));

const accum = str => [...str].map((e, i) => `${e.toUpperCase()}${e.toLowerCase().repeat(i)}`).join('-');

// console.log(accum('ZpglnRxqenU'));

const reverseWords = str =>
  str
    .split(' ')
    .map(e => [...e].reverse().join(''))
    .join(' ');

console.log(reverseWords('The quick brown fox jumps over the lazy dog.'));
console.log(reverseWords('double  spaced  words'));
