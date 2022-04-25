console.log('------- ADVANCE TYPES ---------');

// intersection types {{{
type Admin = {
  name: string;
  privileges: string[];
};

type Employee = {
  name: string;
  startDate: Date;
  misc?: Universal;
};

// type ElevatedEmployee = Admin & Employee;
//or

interface ElevatedEmployee extends Employee, Admin {}

const e1: ElevatedEmployee = {
  name: 'Max',
  privileges: ['create-server'],
  startDate: new Date(),
  misc: 69,
};

type Combinable = string | number;
type Numeric = number | boolean;
type Universal = Combinable & Numeric;

console.log(e1);

// }}}

// type guards {{{

function guardedAdd(a: number, b: number): number;
function guardedAdd(a: string, b: string): string;
function guardedAdd(a: string, b: number): string;
function guardedAdd(a: number, b: string): string;

function guardedAdd(a: Combinable, b: Combinable) {
  if (typeof a === 'string' || typeof b === 'string') {
    return a.toString() + b.toString();
  }
  return a + b;
}

// function overload
const result = guardedAdd('Max', 'Schwarz');
result.split(' ');
console.log(guardedAdd('4', 4));

type UnknownEmployee = Employee | Admin;

function printEmployeeInfo(emp: UnknownEmployee) {
  console.log('Name: ', emp.name);

  if ('privileges' in emp) {
    console.log('Privileges: ', emp.privileges);
  }

  if ('startDate' in emp) {
    console.log('Start date: ' + emp.startDate);
  }
}

printEmployeeInfo(e1);
printEmployeeInfo({ name: 'Manu', startDate: new Date() });

class Car {
  drive() {
    console.log('Driving a car...');
  }
}

class Truck {
  drive() {
    console.log('Driving a truck...');
  }

  loadCargo(amount: number) {
    console.log('Loading cargo ... ' + amount);
  }
}

type Vehicle = Car | Truck;

const v1 = new Car();
const v2 = new Truck();

function useVehicle(vehicle: Vehicle) {
  vehicle.drive();
  if (vehicle instanceof Truck) {
    vehicle.loadCargo(1000);
  }
}

useVehicle(v1);
useVehicle(v2);

// discriminated unions

interface Bird {
  type: 'bird';
  flyingSpeed: number;
}

interface Horse {
  type: 'horse';
  runningSpeed: number;
}

type Animal = Bird | Horse;

function movieAnimal(animal: Animal) {
  let speed;
  switch (animal.type) {
    case 'bird':
      speed = animal.flyingSpeed;
      break;
    case 'horse':
      speed = animal.runningSpeed;
      break;
  }
  console.log('Moving at speed: ' + speed);
}

movieAnimal({ type: 'bird', flyingSpeed: 10 });
// }}}

// type casting {{{

const userInputElement = document.getElementById(
  'user-input'
) as HTMLInputElement;

userInputElement.value = 'Hi there!';

// index types
interface ErrorContainer {
  // id: string;
  [prop: string]: string;
}

const errorBag: ErrorContainer = {
  email: 'Not a valid email',
  usernmae: 'Must start with capital character',
};

console.log(errorBag);

// }}}

// optional chaining {{{

const fetchedUserData = {
  id: 'u1',
  name: 'max',
  job: { title: 'CEO', description: 'my own company' },
};

console.log(fetchedUserData?.job?.title);

// }}}

// nullish coalescing

const userInput = '';
const storedData = userInput ?? 'Default';
console.log(storedData);

const userInput2 = undefined;
const storedData2 = userInput2 ?? 'Default';
console.log(storedData2);
