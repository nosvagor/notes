"use strict";

const currentYear = 2048;

const cullyn = {
  firstName: "Cullyn",
  birthYear: "1996",
  age: function () {
    const isZoomer = () => {
      console.log(this.birthYear >= 1996 && this.birthYear <= 2020);
    };
    isZoomer();
    return currentYear - this.birthYear;
  },
  greet: function () {
    console.log(`Hey ${this.firstName}`);
  },
};

cullyn.greet();

// function calcAge(birthYear) {
//   const age = currentYear - birthYear;
//   console.log(this);
//   return age;
// }

// const calcAgeArrow = birthYear => {
//   const age = currentYear - birthYear;
//   console.log(this);
//   return age;
// };

// calcAge(1996);
// calcAgeArrow(1996);

console.log(cullyn.age());

const jonas = {
  birthYear: 2017,
};

jonas.age = cullyn.age;
console.log(jonas.age());
