'use strict';

const weekdays = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'];

const openingHours = {
  [weekdays[3]]: {
    open: 12,
    close: 22,
  },
  [weekdays[4]]: {
    open: 11,
    close: 23,
  },
  [weekdays[5]]: {
    open: 0, // Open 24 hours
    close: 24,
  },
};

// Data needed for first part of the section
const restaurant = {
  name: 'Classico Italiano',
  location: 'Via Angelo Tavanti 23, Firenze, Italy',
  categories: ['Italian', 'Pizzeria', 'Vegetarian', 'Organic'],
  starterMenu: ['Focaccia', 'Bruschetta', 'Garlic Bread', 'Caprese Salad'],
  mainMenu: ['Pizza', 'Pasta', 'Risotto'],

  openingHours,

  order(startI, mainI) {
    return [this.starterMenu[startI], this.mainMenu[mainI]];
  },

  orderDelivery({ startI = 0, mainI = 0, time = '20:00', address }) {
    console.log(`Order received! ${this.starterMenu[startI]} with ${this.mainMenu[mainI]} will be delivered to ${address} at ${time}`);
  },
};

// const menu = [...restaurant.starterMenu, ...restaurant.mainMenu];
// for (const [i, e] of menu.entries()) {
//   console.log(`${i + 1}: ${e}`);
// }

// restaurant.orderDelivery({
//   time: '22:30',
//   address: 'Via del Sole, 21',
//   mainI: 2,
//   startI: 2,
// });

// restaurant.orderDelivery({
//   address: 'Via del Sole, 21',
// });

// let [first, , second] = restaurant.categories;
// console.log(first, second);

// [second, first] = [first, second];

// console.log(first, second);

// let [starter, main] = restaurant.order(2, 0);
// console.log(starter, "-", main);

// const nested = [2, 4, [5, 6]];
// const [i, , [j, k]] = nested;
// console.log(i, j, k);

// const [p = 1, q = 1, r = 1] = [2, 2];
// console.log(p, q, r);

// const {
//   name: restaurantName,
//   openingHours: hours,
//   categories: tags,
// } = restaurant;
// console.log(restaurantName, hours, tags);

// const { menu = [], starterMenu: starters = [] } = restaurant;
// console.log(menu, starters);

// let a = 111;
// let b = 999;
// const obj = { a: 3, b: 7, c: 14 };
// ({ a, b } = obj);
// console.log(a, b);

// const {
//   fri: { open: fo, close: co },
// } = hours;
// console.log(fo, co);

// restaurant.numGuests = 0;
// const guestCorrect = restaurant.numGuests ?? 10;
// console.log(guestCorrect);

const game = {
  team1: 'Bayern Munich',
  team2: 'Borrussia Dortmund',
  players: [
    ['Neuer', 'Pavard', 'Martinez', 'Alaba', 'Davies', 'Kimmich', 'Goretzka', 'Coman', 'Muller', 'Gnarby', 'Lewandowski'],
    ['Burki', 'Schulz', 'Hummels', 'Akanji', 'Hakimi', 'Weigl', 'Witsel', 'Hazard', 'Brandt', 'Sancho', 'Gotze'],
  ],
  score: '4:0',
  scored: ['Lewandowski', 'Gnarby', 'Lewandowski', 'Hummels'],
  date: 'Nov 9th, 2037',
  odds: {
    team1: 1.33,
    x: 3.25,
    team2: 6.5,
  },
};

// // Coding Challenge 1
// console.log(`Coding Challenge 1 ↓`);
// // 1.
// const [players1, players2] = game.players;
// console.log(players1, players2);

// // 2.
// const [gk, ...fieldPlayers] = players1;
// console.log(gk, fieldPlayers);

// // 3.
// const allPlayers = [...players1, ...players2];
// console.log(allPlayers);

// // 4.
// const players1Final = [...players1, 'Thiago', 'Coutinho', 'Perisic'];
// console.log(players1Final);

// // 5.
// const {
//   odds: { team1, x: draw, team2 },
// } = game;
// console.log(team1, draw, team2);

// // 6.
// const printGoals = (...names) => {
//   const arr = [...names];
//   for (let i = 0; i < arr.length; i++) {
//     const e = arr[i];
//     console.log(e, '- Goal number:', i + 1);
//   }
// };
// printGoals(...game.scored);
// console.log('---');
// printGoals('Davies', 'Muller', 'Lewandowski', 'Kimmich');

// // 7.
// console.log((team1 < team2 && game.team1) || (team1 > team2 && game.team2));

// console.log('----------');

// console.log(restaurant.openingHours?.mon?.open);

// for (const day of weekdays) {
//   const open = restaurant.openingHours[day]?.open ?? 'closed';
//   console.log(`On ${day}, we open at ${open}`);
// }

// console.log(restaurant.order?.(0, 1) ?? 'Method does not exist');

// const users = [{ name: 'Cullyn', email: 'hello@cullyn.io' }];

// console.log(users[0]?.name ?? 'User array empty');

// const prop = Object.keys(openingHours);

// let openStr = `We are open on ${prop.length} days: `;

// for (const day of prop) {
//   openStr += `${day}, `;
// }
// console.log(openStr);

// const values = Object.values(openingHours);
// console.log(values);

// const entries = Object.entries(openingHours);
// // console.log(entries);

// for (const [key, { open, close }] of entries) {
//   console.log(`On ${key} we open at ${open} and close at ${close}.`);
// }

// Coding Challenge 2
// console.log(`Coding Challenge 2 ↓`);

// // 1.
// const entries = Object.entries(game.scored);

// for (const [goal, player] of entries) {
//   console.log(`Goal ${goal}: ${player}!`);
// }

// // 2.
// const average = arr =>
//   (arr.reduce((p, c) => p + c, 0) / arr.length).toFixed(2);

// let odds = [];

// for (const v of Object.values(game.odds)) {
//   odds.push(v);
// }

// console.log(`Average odds: ${average(odds)}`);

// // 3.
// for (const [team, odds] of Object.entries(game.odds)) {
//   console.log(`Odds for ${game[team] || 'a draw'}: ${odds}`);
// }

// // 4.
// const scorers = Object.values(game.scored).reduce(
//   (people, goals) => ({
//     ...people,
//     [goals]: (people[goals] || 0) + 1,
//   }),
//   {}
// );
// console.log(scorers);

// console.log('----------');

// const ordersSet = new Set([
//   'Pasta',
//   'Pizza',
//   'Pizza',
//   'Risotto',
//   'Pasta',
//   'Pizza',
// ]);

// console.log(ordersSet);
// console.log(new Set('Cullyn'));
// console.log(ordersSet.size);
// console.log(ordersSet.has('Bread'));
// ordersSet.add('Garlic Bread');
// ordersSet.add('Garlic Bread');
// ordersSet.delete('Risotto');
// console.log(ordersSet);

// for (const order of ordersSet) {
//   console.log(order);
// }

// const staff = ['Waiter', 'Chef', 'Waiter', 'Manager', 'Chef', 'Waiter'];

// const staffUnique = [...new Set(staff)];
// console.log(staffUnique);

// const rest = new Map();

// rest.set('name', 'Classico Italiano').set(1, 'Firenze, Italy').set(2, 'Lisbon, Portugal').set('open', 11).set('close', 23).set(true, 'We are open!').set(false, 'We are closed!');

// // console.log(rest.get('name'));
// // console.log(rest.get(true));

// const time = 24;
// console.log(rest.get(time > rest.get('open') && time < rest.get('open')));

// const arr = [1, 2];

// rest.set(arr, 'Test');
// console.log(rest.get(arr));

// rest.set(document.querySelector('h1'), 'Heading');
// console.log(rest);

// const question = new Map([
//   ['question', 'What is the best programming language?'],
//   [1, 'C++'],
//   [2, 'Python'],
//   [3, 'JavaScript'],
//   [4, 'Go'],
//   ['correct', 4],
//   [true, 'Correct!'],
//   [false, 'Try again.'],
// ]);

// console.log(question.get(4));

// const hoursMap = new Map(Object.entries(openingHours));
// console.log(hoursMap);

// console.log(question.get('question'));
// for (const [key, value] of question) {
//   if (typeof key === 'number') console.log(`Answer ${key}: ${value}`);
// }

// const answer = Number(prompt('Your answer'));
// console.log(answer);

// console.log(question.get(answer === question.get('correct')));

// console.log([...question]);
// console.log([...question.keys()]);
// console.log([...question.values()]);

// const gameEvents = new Map([
//   [17, '⚽ GOAL'],
//   [36, '🔁 Substitution'],
//   [47, '⚽ GOAL'],
//   [61, '🔁 Substitution'],
//   [64, '🔶 Yellow card'],
//   [69, '🔴 Red card'],
//   [70, '🔁 Substitution'],
//   [72, '🔁 Substitution'],
//   [76, '⚽ GOAL'],
//   [80, '⚽ GOAL'],
//   [92, '🔶 Yellow card'],
// ]);

// // Coding Challege 3
// console.log(`Coding Challege 3 ↓`);

// // 1.
// const events = [...new Set(gameEvents.values())];
// console.log(events);

// // 2.
// gameEvents.delete(64);
// console.log(gameEvents);

// // 3.
// const times = [...new Set(gameEvents.keys())];

// const delta = arr => {
//   const delta = [arr[0]];
//   for (let i = 1; i < arr.length; i++) {
//     delta.push(arr[i] - arr[i - 1]);
//   }
//   return delta;
// };
// const average = arr => (arr.reduce((p, c) => p + c, 0) / arr.length).toFixed(1);

// let dAve = average(delta(times));

// console.log(`An event happend, on average, every ${dAve} minutes`);

// // 4.

// for (const e of gameEvents) {
//   let period = e[0] <= 45 ? 'FIRST' : 'SECOND';
//   console.log(`[${period} HALF] ${e[0]}: ${e[1]}`);
// }

// console.log('----------');

const flights = '_Delayed_Departure;fao93766109;txl2133758440;11:25+_Arrival;bru0943384722;fao93766109;11:45+_Delayed_Arrival;hel7439299980;fao93766109;12:05+_Departure;fao93766109;lis2323639855;12:30';

const airline = 'TAP Air Portugal';
const plane = 'A320';

console.log(airline.lastIndexOf('Air'));

console.log(airline.slice(4));

console.log(airline.slice(0, airline.indexOf(' ')));
console.log(airline.slice(airline.lastIndexOf(' ') + 1));

console.log(airline.slice(-2));
console.log(airline.slice(1, -9));

const checkSeat = seat => {
  const s = seat.slice(-1);
  if (s === 'B' || s === 'E') console.log(`${seat} is a middle seat.`);
  else {
    console.log(`${seat} is not a middle seat`);
  }
};

checkSeat('3E');
checkSeat('23C');
checkSeat('11B');
