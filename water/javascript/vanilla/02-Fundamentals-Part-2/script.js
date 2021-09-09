"use strict";

// Coding challenge 3
console.log(`Coding challenge 3 ↓`);

const mark = {
  firstName: "Mark",
  LastName: "Nut",
  mass: 74,
  height: 1.77,
  calcBMI: function () {
    this.bmi = Number((this.mass / this.height ** 2).toFixed(1));
    return this.bmi;
  },
};

const john = {
  firstName: "John",
  LastName: "Wayne",
  mass: 70,
  height: 1.8,
  calcBMI: function () {
    this.bmi = Number((this.mass / this.height ** 2).toFixed(1));
    return this.bmi;
  },
};

function higherBMI(person1, person2) {
  if (person1.calcBMI() > person2.calcBMI()) {
    return `${person1.firstName}'s BMI (${person1.bmi}) is higher than ${person2.firstName}'s (${person2.bmi})!`;
  } else {
    return `${person2.firstName}'s BMI (${person2.bmi}) is higher than ${person1.firstName}'s (${person1.bmi})!`;
  }
}

console.log(higherBMI(mark, john));

console.log("----------");

// Coding Challenge 4
console.log(`Coding Challenge 4 ↓`);

const bills = [22, 295, 176, 440, 37, 105, 10, 1100, 86, 52];
const tips = [];
const totals = [];

const calcTip = (bill) => (bill >= 50 && bill <= 300 ? bill * 0.15 : bill * 0.2);

const calcAverage = (arr) => (arr.reduce((p, c) => p + c, 0) / arr.length).toFixed(0);

for (let i = 0; i < bills.length; i++) {
  const bill = bills[i];
  const tip = Number(calcTip(bill).toFixed(0));
  const total = bill + tip;
  tips.push(tip);
  totals.push(total);
  console.log(`Bill: $${bill}\t Tip: $${tip} \t Total: $${total}.`);
}

console.log(`The average bill cost was ${calcAverage(bills)}, the average tip was ${calcAverage(tips)} and the average total cost was ${calcAverage(totals)}.`);

console.log("----------");

// -REFACTOR-
// -TESTING-
// -EXPLANATION-
// -TODO-
// -CONFUSED-
// -CRITICAL-
// -BROKEN-
