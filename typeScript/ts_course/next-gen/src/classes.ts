console.log(
  '\n',
  '┌─┐┬  ┌─┐┌─┐┌─┐┌─┐┌─┐\n',
  '│  │  ├─┤└─┐└─┐├┤ └─┐\n',
  '└─┘┴─┘┴ ┴└─┘└─┘└─┘└─┘\n',
  '---------------------\n',
  '\n'
);

class Department {
  static fiscalYear = 2022;
  protected employees: string[] = [];

  constructor(private readonly id: number, public name: string) {
    // console.log(Department.fiscalYear);
  }

  static createEmployee(name: string) {
    return { name: name };
  }

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

class ITDepartment extends Department {
  private lastReport: string;

  get mostRecentReport() {
    if (this.lastReport) {
      return this.lastReport;
    }
    throw new Error('No report found');
  }

  set mostRecentReport(id: string) {
    if (!id) {
      throw new Error('Plase pass in a valid id.');
    }
    this.addReport(id);
  }

  constructor(id: number, public admins: string[], private reports: string[]) {
    super(id, 'IT');
    this.lastReport = reports[0];
  }

  addReport(text: string) {
    this.reports.push(text);
    this.lastReport = text;
  }
}

// ----------------------------------------------------------------------------

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

const it = new ITDepartment(421, ['Michael'], []);
console.log(it);
// console.log(it.mostRecentReport);
// it.mostRecentReport = '';
// console.log(it.mostRecentReport);

console.log(Math.pow(5, 2));

const employee1 = Department.createEmployee('MAX!');

console.log(employee1, Department.fiscalYear);
