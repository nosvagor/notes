"use strict";

const temps1 = [3, -2, -6, -1, "error", 9, 13, 17, 16, 9, 5];
const temps2 = [1, 9, 100, "error", "yes", true, false, 0, -10];

const temps = temps1.concat(temps2);

console.log(temps.length);

function errorCheck(arr) {
  arr.forEach((e, i) => {
    if (typeof e !== "number") {
      arr.splice(i, 1);
    }
  });
  return arr;
}

function range(arr) {
  const min = Math.min(...arr),
    max = Math.max(...arr);
  return max - min;
}

console.log(errorCheck(temps));

console.log(range(errorCheck(temps)));

// Coding Challenge 1
console.log(`Coding Challenge 1 ↓`);

const printForecast = function (temps) {
  const forecast = errorCheck(temps);
  forecast.forEach((e, i) => console.log(`${e}°C in ${i + 1} days\n`));
};

printForecast(temps);
