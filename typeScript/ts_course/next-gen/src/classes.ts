console.log(
  '\n',
  '┌─┐┬  ┌─┐┌─┐┌─┐┌─┐┌─┐\n',
  '│  │  ├─┤└─┐└─┐├┤ └─┐\n',
  '└─┘┴─┘┴ ┴└─┘└─┘└─┘└─┘\n',
  '---------------------\n',
  '\n'
);

class Department {
  private employees: string[] = [];

  constructor(private readonly id: number, public name: string) {}

  describe(this: Department) {
    console.log(`Department [${this.id}]: ${this.name}`);
  }

  addEmployee(employee: string) {
    this.employees.push(employee);
  }

  printEmployeeInfo() {
    console.log(this.employees.length);
    console.log(this.employees);
  }
}

const accounting = new Department(420, 'Accounting');

console.log(accounting);
accounting.describe();
accounting.addEmployee('Kevin');
accounting.addEmployee('Angela');
// acounting.employees[2] = 'Anna'; // doesn't work with private
accounting.printEmployeeInfo();

// const accountingCopy = {
//   name: 'Copied account',
//   describe: accounting.describe,
// };
// accountingCopy.describe();
