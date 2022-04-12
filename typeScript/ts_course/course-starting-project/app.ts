type Combinable = number | string;
type ConversionOpt = 'string' | 'number';

function combine(
  input1: Combinable,
  input2: Combinable,
  resultOpt: ConversionOpt
) {
  let result: Combinable;
  if (
    (typeof input1 === 'number' && typeof input2 === 'number') ||
    resultOpt === 'number'
  ) {
    result = +input1 + +input2;
  } else {
    result = input1.toString() + input2.toString();
  }
  return result;
}

console.log(combine('Hello ', 'World', 'string'));
console.log(combine(30, 26, 'number'));
console.log(combine(30, 26, 'string'));
console.log(combine(30, '26', 'number'));
console.log(combine(30, '26', 'string'));
