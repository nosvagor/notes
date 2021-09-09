'use strict';

// const bookings = [];

// const createBooking = (flight, people = 1, price = 199 * people) => {
//   const booking = {
//     flight,
//     people,
//     price,
//   };
//   console.log(booking);
//   bookings.push(booking);
// };

// createBooking('LH123', undefined, 499);

// const flight = 'LH234';
// const cullyn = {
//   name: 'cullyn newman',
//   passport: 24739423423,
// };

// const checkIn = (flight, person) => {
//   person.name = 'Mr. ' + person.name;

//   if (person.passport === 24739423423) {
//     console.log('Checked in');
//   } else {
//     console.log('Wrong passport!');
//   }
// };

// checkIn(flight, cullyn);

// const newPassport = person => (person.passport = Math.trunc(Math.random() * 10000000000));

// newPassport(cullyn);
// console.log('---');
// checkIn(flight, cullyn);

// const oneWord = str => str.replace(/ /g, '').toLowerCase();

// const upperFirstWord = str => {
//   const [first, ...others] = str.split(' ');
//   return [first.toUpperCase(), ...others].join(' ');
// };

// const transformer = (str, fn) => {
//   console.log(`Original: ${str}`);
//   console.log(`Transformed string: ${fn(str)}`);
//   console.log(`Transformed by: ${fn.name}`);
// };

// transformer('JavaScript is the best!', upperFirstWord);
// transformer('JavaScript is the best!', oneWord);

// const greet = greeting => name => console.log(`${greeting} ${name}`);

// const greeter = greet('Hey');
// console.log(greeter);

// greet('Hello')('Cullyn');
// greeter('Cullyn');

// const alaska = {
//   airline: 'Alaskan Airlines',
//   iataCode: 'AL',
//   bookings: [],
//   book(flight, name) {
//     console.log(`${name} booked a seat on ${this.airline} flight ${this.iataCode}${flight}`);
//     this.bookings.push({ flight: `${this.iataCode}${flight}`, name });
//   },
// };

// alaska.book(239, 'Cullyn');
// alaska.book(635, 'Jonas');
// console.log(alaska.bookings);

// const book = alaska.book;

// const hawaiian = {
//   airline: 'Hawaiian',
//   iataCode: 'EW',
//   bookings: [],
// };

// book.call(hawaiian, 23, 'Sarah');
// console.log(hawaiian);

// book.call(alaska, 239, 'Mary');
// console.log(alaska);

// const flightData = [583, 'George'];
// book.call(hawaiian, ...flightData);

// // Bind method
// console.log(`Bind method ↓`);
// const bookHW = book.bind(hawaiian);
// bookHW(23, 'Steven');

// const addTax = rate => value => console.log(value + (value * rate) / 100);

// const tax23 = addTax(23);

// tax23(100);

// console.log('----------');

// // Coding Challenge 1
// console.log(`Coding Challenge 1 ↓`);

// const poll = {
//   question: 'What is your favourite programming language?',
//   options: ['0: JavaScript', '1: Python', '2: Rust', '3: C++'],
//   answers: new Array(4).fill(0),
//   registerNewAnswer: function () {
//     const choices = [];

//     for (const e of this.options) {
//       choices.push(`${e}\n`);
//     }

//     const answer = Number(prompt(`${this.question}\n\n${[...choices].join('')}\n`));

//     answer <= 3 && answer >= 0 ? this.answers[answer]++ : console.log('Not a valid answer!');
//   },
//   displayResults: function (type) {
//     type === 'array' ? console.log(this.answers) : console.log(`Poll results are ${[...this.answers].join(' ')}`);
//   },
// };

// const pollPrompt = poll.registerNewAnswer.bind(poll);

// document.querySelector('.poll').addEventListener('click', pollPrompt);

// // poll.registerNewAnswer();
// // console.log(poll.answers);

// console.log('----------');

// IIFE
// (() => {
//   console.log('This will never run again');
// })();

// const secureBooking = () => {
//   let passengerCount = 0;

//   return () => {
//     passengerCount++;
//     console.log(`${passengerCount} passengers`);
//   };
// };

// const booker = secureBooking();

// booker();
// booker();

// let f;

// const g = () => {
//   const a = 23;
//   f = () => console.log(a * 2);
// };

// g();
// f();

// const h = () => {
//   const b = 777;
//   f = () => console.log(b * 2);
// };

// h();
// f();
// g();
// f();

// console.dir(f);

// // Timer Example
// console.log(`Timer Example ↓`);

// const boarding = (n, wait) => {
//   const perGroup = n / 3;

//   setTimeout(() => {
//     console.log(`We are now boarding all ${n} passengers`);
//     console.log(`There are 3 groups, each with ${perGroup} passengers`);
//   }, wait * 1000);

//   console.log(`Will start boarding in ${wait} seconds`);
// };

// boarding(180, 2);

// console.log('----------');

// Coding challenge #2
console.log(`Coding challenge #2 ↓`);

(function () {
  const header = document.querySelector('h1');
  header.style.color = 'red';
  document.querySelector('body').addEventListener('mousedown', () => {
    header.style.color = 'blue';
  });
  document.querySelector('body').addEventListener('mouseup', () => {
    header.style.color = 'red';
  });
})();

console.log('----------');
