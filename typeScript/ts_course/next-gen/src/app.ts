// const button = document.querySelector('button');

// if (button) {
//   button.addEventListener('click', (event) => console.log(event));
// }

// set defaults from the right
// const add = (a: number, b: number = 1) => a + b;

// console.log(add(6));

const hobbies = ['sports', 'cooking'];
const activeHobbies = ['hiking'];

activeHobbies.push(...hobbies);

console.log(activeHobbies);

const sum = (...numbers: number[]) => {
  return numbers.reduce((res, val) => {
    return res + val;
  }, 0);
};

console.log(sum(1, 2, 3, 4, 4.2));

const [hobby1, hobby2, ...otherHobbies] = activeHobbies;

console.log(hobby1, hobby2);
console.log(...otherHobbies);
