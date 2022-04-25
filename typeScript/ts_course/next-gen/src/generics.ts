console.log('------ Generics ------');

// const names: Array<string | number> = [];
//
// console.log(names);

// const promise: Promise<string> = new Promise((resolve, reject) => {
//   setTimeout(() => {
//     resolve('This is done');
//   }, 2000);
// });

function merge<T, U>(objA: T, objB: U) {
  return Object.assign(objA, objB);
}

// console.log(merge({ name: 'max' }, { age: 30 }));
const mergedObj = merge({ name: 'max' }, { age: 30 });
console.log(mergedObj.name);

function extractAndConvert<T extends object, U extends keyof T>(
  obj: T,
  key: U
) {
  return 'Value ' + obj[key];
}

extractAndConvert({ name: 'max' }, 'name');

class DataStorage<T> {
  private data: T[] = [];

  addItem(item: T) {
    this.data.push(item);
  }

  removeItem(item: T) {
    this.data.splice(this.data.indexOf(item), 1);
  }

  getItems() {
    return [...this.data];
  }
}

const textStorage = new DataStorage<string>();
textStorage.addItem('max');
textStorage.addItem('manu');
textStorage.removeItem('max');
console.log(textStorage.getItems());
