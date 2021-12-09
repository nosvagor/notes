console.log("Exporting module");

const shippingCost = 10;
export const cart = [];

export const addToCart = (product, quantity) => {
  cart.push({ product, quantity });
  console.log(`${quantity} ${product} added to card`);
};

const totalPrice = 237;
const totalQuantity = 23;

export { totalPrice, totalQuantity as tq };

export default (product, quantity) => {
  cart.push({ product, quantity });
  console.log(`${quantity} ${product} added to card`);
};
