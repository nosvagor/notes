console.log('------- Decorators -------');

function Logger(logString: string) {
  console.log('Logger factory');

  return function (constructor: Function) {
    console.log(logString);
    console.log(constructor);
  };
}

function WithTemplate(template: string, hookId: string) {
  console.log('Template factory');

  return function (constructor: any) {
    console.log('Rendering template');

    const hookEl = document.getElementById(hookId);
    const p = new constructor();
    if (hookEl) {
      hookEl.innerHTML = template;
      hookEl.querySelector('h1')!.textContent = p.name;
    }
  };
}

@Logger('Logging -> Person')
@WithTemplate('<h1>My Person Object</h1>', 'app')
class Person2 {
  name = 'Max';

  constructor() {
    console.log('Creating person object...');
  }
}

const pers = new Person2();

console.log(pers);

// ----------

function Log(target: any, propertyName: string | symbol) {
  console.log('Property decorator!');
  console.log(target, propertyName);
}

function Log2(target: any, name: string, descriptor: PropertyDescriptor) {
  console.log('Accessor decorator! ->');
  console.log(target);
  console.log(name);
  console.log(descriptor);
}

function Log3(
  target: any,
  name: string | symbol,
  descriptor: PropertyDescriptor
) {
  console.log('Method decorator! ->');
  console.log(target);
  console.log(name);
  console.log(descriptor);
}

function Log4(target: any, name: string | symbol, position: number) {
  console.log('parameter decorator! ->');
  console.log(target);
  console.log(name);
  console.log(position);
}

class Product {
  @Log
  @Log2
  set price(val: number) {
    if (val > 0) {
      this._price = val;
    } else {
      throw new Error('Invalid price, should be positive!');
    }
  }

  constructor(public title: string, private _price: number) {}

  @Log3
  getPriceWithTax(@Log4 tax: number) {
    return this.price * (1 + tax);
  }

  print() {
    console.log(this._price);
    console.log(this.title);
  }
}

const prod = new Product('Cheese', 420);

prod.print();

prod.price = -69;
