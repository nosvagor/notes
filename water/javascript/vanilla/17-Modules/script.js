// import {
//   addToCart,
//   totalPrice as price,
//   tq,
// } from "./shoppingCart.js";

// console.log("importing module");
// addToCart("apples", 7);
// console.log(tq, price);

// import * as Shop from "./shoppingCart.js";
// Shop.addToCart("bread", 5);

import { cart, addToCart as add } from "./shoppingCart.js";
add("mink", 42);
add("bread", 3);
add("apple", 6);
console.log(cart);

// const ShoppingCart2 = (function () {
//   const cart = [];
//   const shippignCost = 10;
//   const totalPrice = 237;
//   const totalQuantity = 42;
//   const addToCart = (product, quantity) => {
//     cart.push({ product, quantity });
//     console.log(`${quantity} ${product} added to card`);
//   };
//   const orderStock = (product, quantity) => {
//     console.log(`${quantity} ${product} ordered from supplier`);
//   };

//   return {
//     addToCart,
//     cart,
//     totalPrice,
//     totalQuantity,
//   };
// })();

// ShoppingCart2.addToCart("apple", 4);
// ShoppingCart2.addToCart("apple", 2);
// console.log(...ShoppingCart2.cart)

import cloneDeep from "lodash-es";

const state = {
  cart: [
    { product: "bread", quantity: 5 },
    { product: "milk", quantity: 2 },
  ],
  user: { loggedIn: true },
};

const stateClone = Object.assign({}, state);
const stateDeepClone = cloneDeep(state);

state.user.loggedIn = false;
console.log(stateClone);
console.log(stateDeepClone);

if (module.hot) {
  module.hot.accept();
}
