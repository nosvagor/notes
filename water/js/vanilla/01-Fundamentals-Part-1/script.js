// Values and variables
console.log("Values and variables ↓");
const country = "United States";
const continent = "North America";
let population = 328 * 10 ** 6;
console.log(country, continent, population);
console.log("----------");

// Data types
console.log("Data types ↓");
const isIsland = false;
let language;

console.log(typeof isIsland, isIsland);
console.log(typeof population, population);
console.log(typeof country, country);
console.log(typeof language, language);
console.log("----------");

// let, const, and var
language = "english";
// country = "Italy"; <- TypeError assignment to const

// Basic operators
console.log("Basic operators ↓");
console.log((population / 2).toExponential());
console.log(population + 1);
let finlandPop = 6 * 10 ** 6;
console.log(finlandPop >= population);
let averagePop = 33 * 10 ** 6;
console.log(averagePop >= population);
const description = `${country} is in ${continent}, and its ${population.toExponential()} people speak ${language}`;
console.log(description);
console.log("----------");

// Coding challenge 1
console.log("Coding challenge 1 ↓");

function BMI(m, h) {
  return (m / h ** 2).toFixed(2);
}

let [markHeight, markMass] = [1.77, 74];
let [johnHeight, johnMass] = [1.8, 70];

console.log(BMI(markMass, markHeight));
console.log(BMI(johnMass, johnHeight));

let [markBMI, johnBMI] = [BMI(markMass, markHeight), BMI(johnMass, johnHeight)];

[markHeight, markMass] = [1.69, 78];
[johnHeight, johnMass] = [1.95, 92];

let markHigherBMI = markBMI > johnBMI;
console.log(markHigherBMI);

[markHeight, markMass] = [1.88, 95];
[johnHeight, johnMass] = [1.75, 85];

[markBMI, johnBMI] = [BMI(markMass, markHeight), BMI(johnMass, johnHeight)];

markHigherBMI = markBMI > johnBMI;
console.log(markHigherBMI);

console.log("----------");

// if / else statements
console.log(`if / else statements ↓`);
if (population < averagePop) {
  console.log(`${country}'s population is ${averagePop - population} below average.`);
} else {
  console.log(`${country}'s population is ${(population - averagePop).toExponential(2)} above average.`);
}
console.log("----------");

// Coding challenge 2
console.log(`Coding challenge 2 ↓`);

[markHeight, markMass] = [1.8, 74];
[johnHeight, johnMass] = [1.77, 70];
[markBMI, johnBMI] = [BMI(markMass, markHeight), BMI(johnMass, johnHeight)];

if (markBMI > johnBMI) {
  console.log(`Mark's BMI (${markBMI}) is higher than John's BMI (${johnBMI})`);
} else {
  console.log(`Mark's BMI (${markBMI}) is lower than John's BMI (${johnBMI})`);
}
console.log("----------");

// Type conversion and coercion
console.log(`Type conversion and coercion ↓`);

const inputYear = "1996";
const Year = 2021;
console.log(Number(inputYear), inputYear);
console.log(Number(inputYear) + 21);

// only + converts to string (coercion)
console.log("I am " + (Year - Number(inputYear)) + " years olds");
console.log("23" + 10 - 4 + "6" / 2);
console.log("23" > "18");

console.log("----------");

// Boolean
console.log(`Boolean ↓`);

console.log(Boolean(0));
console.log(Boolean(undefined));
console.log(Boolean(""));
console.log(Boolean(NaN));
console.log(Boolean(null));

console.log("----------");

// Equality operators
// console.log(`Equality operators ↓`);

// const numNeighbors = prompt(`How many countries border your country?`);
// console.log(numNeighbors);
// console.log(typeof numNeighbors);

// if (Number(numNeighbors) === 1) {
//   console.log(`Only one border!`);
// } else if (numNeighbors > 1) {
//   console.log(`More than one neighbor!`);
// } else {
//   console.log(`No neighbors 😥`);
// }

// console.log("----------");

// Coding challenge 3
console.log(`Coding challenge 3 ↓`);

const [dolphins, koalas] = ["Dolphins", "Koalas"];
let dolphinsScore = [96, 108, 89];
let koalasScore = [88, 91, 110];

const average = (arr) => (arr.reduce((p, c) => p + c, 0) / arr.length).toFixed(0);

function winner(team1, team2, scores1, scores2) {
  const [a, b] = [average(scores1), average(scores2)];
  if (a > b) {
    console.log(`${team1} win with an average score of ${a} to ${b}`);
  } else if (a <= 100 && b <= 100) {
    console.log(`Neither team wins, stalemate!`);
  } else if (a === b) {
    console.log(`It's a tie!`);
  } else {
    console.log(`${team2} win with an average score of ${b} to ${a}`);
  }
}

winner(dolphins, koalas, dolphinsScore, koalasScore);

dolphinsScore = [97, 112, 101];
koalasScore = [109, 95, 123];

winner(dolphins, koalas, dolphinsScore, koalasScore);

dolphinsScore = [97, 112, 101];
koalasScore = [109, 95, 106];

winner(dolphins, koalas, dolphinsScore, koalasScore);

dolphinsScore = [97, 80, 99];
koalasScore = [92, 95, 100];

winner(dolphins, koalas, dolphinsScore, koalasScore);

console.log("----------");

// Coding challenge 4
console.log(`Coding challenge 4 ↓`);

const check = (bill) => (bill >= 50 && bill <= 300 ? bill * 0.15 : bill * 0.2);

const pay = (bill) => {
  const tip = check(bill).toFixed(0);
  const total = Number(bill) + Number(tip);
  return `The bill was $${bill}, the tip was $${tip}, so the total is $${total}.`;
};

let bill = 10;
console.log(pay(bill));
bill = 100;
console.log(pay(bill));
bill = 1000;
console.log(pay(bill));

console.log("----------");
