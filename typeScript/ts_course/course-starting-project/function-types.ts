function add(n1: number, n2: number) {
	return n1 + n2;
}

function subtract(n1: number, n2: number) {
	return n1 - n2;
}

function printRes(num: number): void {
	console.log('Result: ' + num);
}

let combineVal: (a: number, b: number) => number;

combineVal = add;
// combineVal = add;
combineVal = subtract;

printRes(5 + 50);
printRes(combineVal(8, 8));

console.log('-----------------------------------');

let userInput: unknown;
let userName: string;

userInput = 5;
userInput = 'Max';
userName = 'None';

if (typeof userInput === 'string') {
	userName = userInput;
}

console.log(userName);

console.log('-------------------------------------');

function generateError(message: string, code: number): never {
	throw { message: message, errorCode: code };
}

generateError('An error: ', 500);
