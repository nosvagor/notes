// 'use strict';

// // Constructor functions
// console.log(`Constructor functions ↓`);

// const Person = function (firstName, birthYear) {
//   this.firstName = firstName;
//   this.birthYear = birthYear;
// };

// const cullyn = new Person('cullyn', 1996);
// console.log(cullyn);

// console.log('----------');

// // Prototypes
// console.log(`Prototypes ↓`);

// Person.prototype.calcAge = function () {
//   console.log(2038 - this.birthYear);
// };

// cullyn.calcAge();

// Person.prototype.species = 'Homo Sapiens';

// console.log('----------');

// // Prototypal Inheritance
// console.log(`Prototypal Inheritance  ↓`);

// console.log(cullyn.__proto__.__proto__);
// console.dir(Person.prototype.constructor);

// const arr = [6, 3, 3, 7, 6, 8, 8, 9, 62, 839];
// console.log(arr.__proto__ === Array.prototype);
// console.log(arr.__proto__.__proto__);

// Array.prototype.unique = function () {
//   [...new Set(this)];
// };

// const h1 = document.querySelector('h1');

// console.log('----------');

// // Coding Challenge #1
// console.log(`Coding Challenge #1 ↓`);

// const Car = function (make, speed) {
//   this.make = make;
//   this.speed = speed;
// };

// Car.prototype.accelerate = function () {
//   this.speed += 10;
//   console.log(`The ${this.make} is going ${this.speed} km/h`);
// };

// Car.prototype.brake = function () {
//   this.speed -= 5;
//   console.log(`The ${this.make} is going ${this.speed} km/h`);
// };

// const car1 = new Car('BMW', 120);
// const car2 = new Car('Tesla', 200);

// car1.brake();
// car2.accelerate();
// car2.brake();
// car2.brake();

// console.log('----------');

// ES6 Classes
// console.log(`ES6 Classes ↓`);

// class PersonCl {
//   constructor(fullName, birthYear) {
//     this.fullName = fullName;
//     this.birthYear = birthYear;
//   }

//   calcAge() {
//     console.log(2028 - this.birthYear);
//   }

//   get age() {
//     return 2028 - this.birthYear;
//   }

//   set fullName(name) {
//     name.includes(" ") ? (this._fullName = name) : console.log(`${name}is not a full name!`);
//   }

//   get fullName() {
//     return this._fullName;
//   }

//   static hey() {
//     console.log(`Hey there 👋`);
//   }
// }

// const jessica = new PersonCl("Jessica Vagor", 1996);
// jessica.calcAge();
// console.log(jessica.age);
// console.log(jessica.fullName);
// PersonCl.hey();

// // PersonCl.prototype.greet = function () {
// //   console.log(`Hey ${this.firstName}`);
// // };
// // jessica.greet();

// console.log("----------");

// // Getters and Setters
// console.log(`Getters and Setters ↓`);

// const account = {
//   owner: "Jonas",
//   movements: [200, 530, 120, 300],

//   get latest() {
//     return this.movements.slice(-1).pop();
//   },

//   set latest(mov) {
//     return this.movements.push(mov);
//   },
// };

// console.log("----------");

// console.log(account.latest);
// account.latest = 42;
// console.log(account.movements);

// Object.create
// console.log(`Object.create ↓`);

// const PersonProto = {
//   calcAge() {
//     console.log(3005 - this.birthYear);
//   },

//   init(firstName, birthYear) {
//     this.firstName = firstName;
//     this.birthYear = birthYear;
//   },
// };

// const steven = Object.create(PersonProto);

// steven.name = "Steven";
// steven.birthYear = "2011";
// steven.calcAge();

// console.log(steven.__proto__ == PersonProto);
// accelerate() {
//   this.speed += this.speed * .05 ;
//   console.log(`The ${this.make} is going ${this.speed} km/h`);
// }
// const sarah = Object.create(PersonProto);

// console.log("----------");
// sarah.init("sarah", 1979);
// sarah.calcAge();

// Coding challenge #2
// console.log(`Coding challenge #2 ↓`);

// class Car {
//   constructor(make, speed) {
//     this.make = make;
//     this.speed = speed;
//   }

//   accelerate(s) {
//     this.speed += this.speed * 0.05 * s;
//     console.log(`The ${this.make} is going ${this.speed} km/h`);
//   }

//   brake(s) {
//     this.speed -= this.speed * ((0.2 * s) / 1);
//     if (this.speed < 0) this.speed = 0;
//     console.log(`The ${this.make} is going ${this.speed} km/h`);
//   }

//   get speedUS() {
//     return this.speed / 1.6;
//   }

//   set speedUS(speed) {
//     this.speed = speed * 1.6;
//   }
// }

// const car = new Car("ford", 120);

// console.log(car.speed);
// console.log(car.speedUS);
// car.accelerate(10);
// console.log(`The speed in km/h is ${car.speed}; imperial ${car.speedUS} mph`);
// car.brake(2);
// console.log(`The speed in km/h is ${car.speed}; imperial ${car.speedUS} mph`);
// car.speedUS = 50;
// console.log(car.speed);

// console.log("----------");

// const Person = function (firstName, birthYear) {
//   this.firstName = firstName;
//   this.birthYear = birthYear;
// };

// Person.prototype.calcAge = function () {
//   console.log(2038 - this.birthYear);
// };

// const Student = function (firstName, birthYear, course) {
//   Person.call(this, firstName, birthYear);
//   this.course = course;
// };

// Student.prototype = Object.create(Person.prototype);
// Student.prototype.constructor = Student;

// Student.prototype.introduce = function () {
//   console.log(`My name is ${this.firstName} and I study ${this.course}`);
// };

// const mike = new Student("Mike", 2020, "Computer Science");
// console.log(mike);
// mike.introduce();
// // mike.calcAge();
// console.log(mike instanceof Student);
// console.log(mike instanceof Person);
// console.log(mike instanceof Object);

// Coding Challenge #3
// console.log(`Coding Challenge #3 ↓`);

// const Car = function (make, speed) {
//   this.make = make;
//   this.speed = speed;
// };

// Car.prototype.accelerate = function () {
//   this.speed += 10;
//   console.log(`The ${this.make} is going ${this.speed} km/h`);
// };

// Car.prototype.brake = function () {
//   this.speed -= 5;
//   console.log(`The ${this.make} is going ${this.speed} km/h`);
// };

// const EV = function (make, speed, charge) {
//   Car.call(this, make, speed);
//   this.charge = charge;
// };

// EV.prototype = Object.create(Car.prototype);
// EV.prototype.constructor = EV;

// EV.prototype.chargeBattery = function (chargeTo) {
//   this.charge = chargeTo;
// };

// EV.prototype.accelerate = function () {
//   this.speed += 20;
//   this.charge--;
//   console.log(`The ${this.make} is going ${this.speed} km/h, with a charge of ${this.charge}%`);
// };
// EV.prototype.brake = function () {
//   this.charge += 0.2;
//   this.speed -= 20;
//   console.log(`The ${this.make} is going ${this.speed} km/h, with a charge of ${this.charge}%`);
// };

// const ford = new Car("Ford", 120);
// const modelS = new EV("Tesla", 120, 69);
// console.log(modelS);
// console.log(ford);
// // console.log(modelS.make);
// // console.log(modelS.speed);
// // console.log(modelS.charge);
// ford.accelerate();
// modelS.accelerate();
// ford.brake();
// modelS.brake();
// modelS.brake();
// modelS.chargeBattery(90);
// modelS.accelerate();

// console.log("----------");

// class PersonCl {
//   constructor(fullName, birthYear) {
//     this.fullName = fullName;
//     this.birthYear = birthYear;
//   }

//   calcAge() {
//     console.log(2028 - this.birthYear);
//   }

//   get age() {
//     return 2028 - this.birthYear;
//   }

//   set fullName(name) {
//     name.includes(" ") ? (this._fullName = name) : console.log(`${name}is not a full name!`);
//   }

//   get fullName() {
//     return this._fullName;
//   }

//   static hey() {
//     console.log(`Hey there 👋`);
//   }
// }

// class StudentCl extends PersonCl {
//   constructor(fullName, birthYear, course) {
//     super(fullName, birthYear);
//     this.course = course;
//   }

//   introduce() {
//     console.log(`My name is ${this.fullName} and I study ${this.course}`);
//   }

//   calcAge() {
//     console.log(`I'm ${2028 - this.birthYear} years old`);
//   }
// }

// const martha = new StudentCl("Martha Jones", 2012, "Computer Science");
// martha.introduce();
// martha.calcAge();

// const PersonProto = {
//   calcAge() {
//     console.log(3005 - this.birthYear);
//   },

//   init(firstName, birthYear) {
//     this.firstName = firstName;
//     this.birthYear = birthYear;
//   },
// };

// const steven = Object.create(PersonProto);

// const StudentProto = Object.create(PersonProto);
// StudentProto.init = function (firstName, birthYear, course) {
//   PersonProto.init.call(this, firstName, birthYear);
//   this.course = course;
// };

// StudentProto.introduce = function () {
//   console.log(`My name is ${this.firstName} and I study ${this.course}`);
// };

// const jay = Object.create(StudentProto);
// jay.init("Jay", 2010, "Computer Science");
// // console.log(jay);
// jay.introduce();
// jay.calcAge();

// class Account {
//   locale = navigator.language;
//   #movements = [];

//   constructor(owner, currency, pin) {
//     this.owner = owner;
//     this.currency = currency;
//     this._pin = pin;
//     // this._movements = [];
//     // this.locale = navigator.language;

//     console.log(`Thanks for opening an account, ${owner}`);
//   }

//   getMovements() {
//     return this.#movements;
//   }

//   deposit(val) {
//     this.#movements.push(val);
//     return this;
//   }

//   withdraw(val) {
//     this.deposit(-val);
//     return this;
//   }

//   _approveLoan(val) {
//     console.log(`${val} requested`);
//     return true;
//   }

//   requestLoan(val) {
//     this._approveLoan(val) ? console.log(`Loan approved`) : console.log("sucks to suck");
//     return this;
//   }
// }

// const acc1 = new Account("Jonas", "EUR", 1111);

// acc1.deposit(250);
// acc1.withdraw(140);

// console.log(acc1);
// acc1.requestLoan(100);

// acc1.deposit(250).deposit(420);
// console.log(acc1.getMovements());

// Coding Challenge #4
console.log(`Coding Challenge #4 ↓`);

class Car {
  constructor(make, speed) {
    this.make = make;
    this.speed = speed;
  }

  accelerate = function () {
    this.speed += 10;
    console.log(`The ${this.make} accelrated to ${this.speed} km/h`);
    return this;
  };

  brake = function () {
    this.speed -= 5;
    console.log(`The ${this.make} slowed ${this.speed} km/h`);
    return this;
  };
}

class EV extends Car {
  #charge;

  constructor(make, speed, charge) {
    super(make, speed);
    this.#charge = charge;
  }

  chargeBattery = function (chargeTo) {
    this.#charge = chargeTo;
    console.log(`Your ${this.make} now has ${this.#charge}% battery`);
    return this;
  };

  accelerate = function () {
    this.speed += 20;
    this.#charge--;
    console.log(`The ${this.make} acclerated to ${this.speed} km/h, with a charge of ${this.#charge}%`);
    return this;
  };

  brake = function () {
    this.#charge += 0.2;
    this.speed -= 20;
    console.log(`The ${this.make} slowed ${this.speed} km/h, with a charge of ${this.#charge}%`);
    return this;
  };
}

const ford = new Car("Ford", 120);
const modelS = new EV("Tesla", 120, 69);
console.log(modelS);
console.log(ford);
ford.accelerate().brake().accelerate().brake();
modelS.accelerate().brake().brake().chargeBattery(90).accelerate();

console.log("----------");
