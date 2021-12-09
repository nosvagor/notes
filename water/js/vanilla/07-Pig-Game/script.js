'use strict';

// Selecting elements
const player0 = document.querySelector('.player--0');
const player1 = document.querySelector('.player--1');
const score0 = document.getElementById('score--0');
const current0 = document.getElementById('current--0');
const score1 = document.getElementById('score--1');
const current1 = document.getElementById('current--1');
const dice = document.querySelector('.dice');
const btnNew = document.querySelector('.btn--new');
const btnRoll = document.querySelector('.btn--roll');
const btnHold = document.querySelector('.btn--hold');

// Variables
const scores = [0, 0];
let currentScore = 0;
let activePlayer = 0;

// Functions
const switchPlayer = () => {
  document.getElementById(`current--${activePlayer}`).textContent = 0;
  currentScore = 0;
  activePlayer = activePlayer === 0 ? 1 : 0;
  player0.classList.toggle('player--active');
  player1.classList.toggle('player--active');
};

const newGame = () => {
  scores[0] = scores[1] = 0;
  currentScore = activePlayer = 0;
  score0.textContent = score1.textContent = 0;
  document.getElementById(`current--0`).textContent = 0;
  document.getElementById(`current--1`).textContent = 0;
  dice.classList.add('hidden');
  player0.classList.add('player--active');
  player1.classList.remove('player--active');
  player0.classList.remove('player--winner');
  player1.classList.remove('player--winner');
  btnRoll.classList.remove('hidden');
  btnHold.classList.remove('hidden');
};

newGame();

// Rolling dice functionality
btnRoll.addEventListener('click', () => {
  // 1. Generate random dice roll
  const diceRoll = Math.trunc(Math.random() * 6) + 1;

  // 2. Display dice
  dice.classList.remove('hidden');
  dice.src = `dice-${diceRoll}.png`;

  // 3. Respond to roll
  if (diceRoll !== 1) {
    // Add dice to current score
    currentScore += diceRoll;
    document.getElementById(`current--${activePlayer}`).textContent =
      currentScore;
  } else {
    switchPlayer();
  }
});

// Hold score functionality
btnHold.addEventListener('click', () => {
  scores[activePlayer] += currentScore;
  score0.textContent = scores[0];
  score1.textContent = scores[1];
  if (scores[activePlayer] >= 100) {
    document
      .querySelector(`.player--${activePlayer}`)
      .classList.add('player--winner');
    document
      .querySelector(`.player--${activePlayer}`)
      .classList.remove('player--active');
    dice.classList.add('hidden');
    document.getElementById(`name--${activePlayer}`).textContent = 'Winner!';
    btnRoll.classList.add('hidden');
    btnHold.classList.add('hidden');
  }
  switchPlayer();
});

// New game functionality
btnNew.addEventListener('click', newGame);
