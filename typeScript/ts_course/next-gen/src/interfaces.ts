console.log('------- INTERFACES ---------');

interface Greetable {
  name: string;
  // age: number;

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
