'use strict';

/////////////////////////////////////////////////
/////////////////////////////////////////////////
// BANKIST APP

// Data
const account1 = {
  owner: 'Jonas Schmedtmann',
  movements: [200, 450, -400, 3000, -650, -130, 70, 1300],
  interestRate: 1.2, // %
  pin: 1111,
};

const account2 = {
  owner: 'Jessica Davis',
  movements: [5000, 3400, -150, -790, -3210, -1000, 8500, -30],
  interestRate: 1.5,
  pin: 2222,
};

const account3 = {
  owner: 'Steven Thomas Williams',
  movements: [200, -200, 340, -300, -20, 50, 400, -460],
  interestRate: 0.7,
  pin: 3333,
};

const account4 = {
  owner: 'Sarah Smith',
  movements: [430, 1000, 700, 50, 90],
  interestRate: 1,
  pin: 4444,
};

const accounts = [account1, account2, account3, account4];

// Elements
const labelWelcome = document.querySelector('.welcome');
const labelDate = document.querySelector('.date');
const labelBalance = document.querySelector('.balance__value');
const labelSumIn = document.querySelector('.summary__value--in');
const labelSumOut = document.querySelector('.summary__value--out');
const labelSumInterest = document.querySelector('.summary__value--interest');
const labelTimer = document.querySelector('.timer');

const containerApp = document.querySelector('.app');
const containerMovements = document.querySelector('.movements');

const btnLogin = document.querySelector('.login__btn');
const btnTransfer = document.querySelector('.form__btn--transfer');
const btnLoan = document.querySelector('.form__btn--loan');
const btnClose = document.querySelector('.form__btn--close');
const btnSort = document.querySelector('.btn--sort');

const inputLoginUsername = document.querySelector('.login__input--user');
const inputLoginPin = document.querySelector('.login__input--pin');
const inputTransferTo = document.querySelector('.form__input--to');
const inputTransferAmount = document.querySelector('.form__input--amount');
const inputLoanAmount = document.querySelector('.form__input--loan-amount');
const inputCloseUsername = document.querySelector('.form__input--user');
const inputClosePin = document.querySelector('.form__input--pin');

const createUsernames = acc => {
  acc.forEach(acc => {
    acc.username = acc.owner
      .toLowerCase()
      .split(' ')
      .map(name => name[0])
      .join('');
  });
};

createUsernames(accounts);

const displayMovements = (acc, sort = false) => {
  containerMovements.innerHTML = '';

  const movs = sort ? acc.movements.slice().sort((a, b) => a - b) : acc.movements;

  movs.forEach((mov, i) => {
    const type = mov > 0 ? 'deposit' : 'withdrawal';

    const html = `
    <div class="movements__row">
      <div class="movements__type movements__type--${type}">${i + 1} ${type}</div>
      <div class="movements__value">${mov}</div>
    </div>
    `;

    containerMovements.insertAdjacentHTML('afterbegin', html);
  });
};

const calcDisplayBalance = acc => {
  acc.balance = acc.movements.reduce((bal, mov) => (bal += mov), 0);
  labelBalance.textContent = `${acc.balance} EUR`;
};

const calcDisplaySummary = acc => {
  const incomes = acc.movements.filter(mov => mov > 0).reduce((s, mov) => s + mov, 0);
  labelSumIn.textContent = `${incomes}€`;

  const out = acc.movements.filter(mov => mov < 0).reduce((s, mov) => s - mov, 0);
  labelSumOut.textContent = `${out}€`;

  const interest = acc.movements
    .filter(mov => mov > 0)
    .map(deposit => (deposit * acc.interestRate) / 100)
    .filter(r => r >= 1)
    .reduce((s, r) => s + r, 0);

  labelSumInterest.textContent = `${interest.toFixed(2)}€`;
};

// Event handler
let currentAccount;

btnLogin.addEventListener('click', e => {
  e.preventDefault();

  currentAccount = accounts.find(acc => acc.username === inputLoginUsername.value);

  if (currentAccount?.pin === Number(inputLoginPin.value)) {
    // Display UI and welcome message
    containerApp.style.opacity = 100;
    labelWelcome.textContent = `Welcome back, ${currentAccount.owner.split(' ')[0]}`;

    // Clear input fields
    inputLoginUsername.value = inputLoginPin.value = '';
    inputLoginPin.blur();

    // Dispaly balance, summary, movements
    updateUI(currentAccount);
  }
});

const updateUI = acc => {
  displayMovements(acc);
  calcDisplayBalance(acc);
  calcDisplaySummary(acc);
};

btnTransfer.addEventListener('click', e => {
  e.preventDefault();

  const amount = Number(inputTransferAmount.value);
  const receiverAcc = accounts.find(acc => acc.username === inputTransferTo.value);

  inputTransferAmount.value = inputTransferTo.value = '';

  if (amount > 0 && amount <= currentAccount.balance && receiverAcc && receiverAcc.username !== currentAccount.username) {
    currentAccount.movements.push(-amount);
    receiverAcc.movements.push(amount);
    updateUI(currentAccount);
  }
});

btnLoan.addEventListener('click', e => {
  e.preventDefault();

  const amount = Number(inputLoanAmount.value);

  if (amount > 0 && currentAccount.movements.some(mov => mov >= amount * 0.1)) {
    currentAccount.movements.push(amount);
    updateUI(currentAccount);
  }

  inputLoanAmount.value = '';
});

btnClose.addEventListener('click', e => {
  e.preventDefault();

  if (inputCloseUsername.value === currentAccount.username && Number(inputClosePin.value) === currentAccount.pin) {
    if (prompt('Delete account? (yes/no)') === 'yes') {
      accounts.splice(
        accounts.findIndex(acc => acc.username === currentAccount.username),
        1
      );
    }
    inputCloseUsername.value = inputClosePin.value = '';
    containerApp.style.opacity = 0;
  }

  inputCloseUsername.value = inputClosePin.value = '';
});

let sorted = false;
btnSort.addEventListener('click', e => {
  e.preventDefault();
  displayMovements(currentAccount, !sorted);
  sorted = !sorted;
});

/////////////////////////////////////////////////
/////////////////////////////////////////////////
// LECTURES
/////////////////////////////////////////////////

// let arr = [...'abcde'];

// // Slice
// console.log(`Slice ↓`);

// console.log(arr.slice(2));
// console.log(arr);

// console.log('----------');

// // Splice
// console.log(`Splice ↓`);

// console.log(arr.splice(-1));
// console.log(arr);
// console.log(arr.splice(1, 2));
// console.log(arr);

// console.log('----------');

// // Reverse
// console.log(`Reverse ↓`);

// const arr2 = [...'jihgf'];
// console.log(arr2.reverse());
// console.log(arr2);

// console.log('----------');

// // Concat
// console.log(`Concat ↓`);

// arr = [...'abcde'];
// const letters = arr.concat(arr2);
// console.log(letters);
// console.log([...arr, ...arr2]);

// console.log('----------');

// // Join
// console.log(`Join ↓`);

// console.log(letters.join(' 👏 '));

// console.log('----------');

// const currencies = new Map([
//   ['USD', 'United States dollar'],
//   ['EUR', 'Euro'],
//   ['GBP', 'Pound sterling'],
// ]);

const movements = [200, 450, -400, 3000, -650, -130, 70, 1300];

// movements.forEach((move, i) => {
//

// currencies.forEach((val, key, map) => {
//   console.log(`${key}: ${val}`);
//   console.log(map);
// });

// const eurToUsd = 1.19;

// const movementsUSD = movements.map(mov => mov * eurToUsd);

// console.log(movements);
// console.log(movementsUSD);

// const moveDescription = movements.map((move, i) => {
//   const str = `Movement ${i + 1}: you`;
//   return move > 0 ? `${str} deposited ${move}` : `${str} withdrew ${Math.abs(move)}`;
// });

// console.log(moveDescription);

// Filter
// console.log(`Filter ↓`);

// const deposits = movements.filter(mov => mov > 0);
// const withdrawals = movements.filter(mov => mov < 0);
// console.log(deposits);
// console.log(withdrawals);

// console.log('----------');

// Reduce
// console.log(`Reduce ↓`);

// let iBal = 60;
// const balance = movements.reduce((sum, val) => (sum += val), iBal);

// console.log(balance);

// const max = movements.reduce((max, mov) => (mov > max ? (max = mov) : max));

// console.log(max);

// console.log('----------');

// Chainiing
// console.log(`Chainiing ↓`);

// const rate = 1.19;
// const usd = movements
//   .filter(mov => mov > 0)
//   .map(mov => mov * rate)
//   .reduce((bal, mov) => bal + mov, 0);

// console.log(usd);

// console.log('----------');

// Find
// console.log(`Find ↓`);

// console.log(movements.find(mov => mov < 0));

// console.log(accounts);

// const account = accounts.find(acc => acc.owner === 'Jessica Davis');
// console.log(account);

// console.log('----------');

// Includes
// console.log(`Includes ↓`);

// console.log(movements.includes(-130));

// const any = movements.some(mov => mov > 1500);
// console.log(any);

// console.log('----------');

// Flat
// console.log(`Flat ↓`);

// const arr = [[1, 2, 3], [4, 5, 6], 7, 8];
// console.log(arr.flat());

// const arrDeep = [[[1, 2], 3], [[4, 5, 6], 7], 7, 8];
// console.log(arrDeep.flat(2));

// console.log(accounts.flatMap(acc => acc.movements).reduce((s, e) => s + e));

// console.log('----------');

// Arrays
console.log(`Arrays ↓`);

let x = Array.from({ length: 7 }, () => 1);
console.log(x);

x = Array.from({ length: 7 }, (_, i) => i + 1);
console.log(x);

labelBalance.addEventListener('click', e => {
  const movementsUI = Array.from(document.querySelectorAll('.movements__value'), el => Number(el.textContent));
  console.log(movementsUI);
});

console.log('----------');
