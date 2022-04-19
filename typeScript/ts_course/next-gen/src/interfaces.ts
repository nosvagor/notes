console.log('------- INTERFACES ---------');

// type AddFn = (a: number, b: number) => number;

// interface AddFn {
//   (a: number, b: number): number;
// }
//
// let adds: AddFn;

// adds = (n1: number, n2: number) => {
//   return n1 + n2;
// };

interface Named {
  readonly name: string;
  outPutName?: string;
}

interface Greetable extends Named {
  greet(phrase: string): void;
}

class Person implements Greetable {
  name: string;

  constructor(n: string) {
    this.name = n;
  }

  greet(phrase: string) {
    console.log(phrase + ' ' + this.name);
  }
}

const user1 = new Person('cullyn');

console.log(user1);
user1.greet('Hello');
