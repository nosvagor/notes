'use strict';

// console.log(document.querySelector('.message').textContent);

// document.querySelector('.message').textContent = '🥳 Correct Number!';

// document.querySelector('.number').textContent = 13;

// document.querySelector('.guess').value = 13;
// console.log(document.querySelector('.guess').value);

let sn = Math.trunc(Math.random() * 20) + 1;
let score = 20;
let highscore = 0;

document.querySelector('.guess').value = '';

document.querySelector('.check').addEventListener('click', function () {
  const guess = Number(document.querySelector('.guess').value);

  if (!guess || guess > 20) {
    document.querySelector('.message').textContent = 'Input a number between 1 and 20!';
    return;
  } else if (guess === sn) {
    document.querySelector('.message').textContent = '✅ Correct!';

    if (score > highscore) {
      highscore = score;
    }

    document.querySelector('body').style.backgroundColor = '#60b347';

    document.querySelector('.number').textContent = sn;

    document.querySelector('.number').style.width = '30rem';
    document.querySelector('.highscore').textContent = highscore;
    return;
  }

  if (score < 1) {
    document.querySelector('.message').textContent = 'game over!';
  } else {
    score--;
    document.querySelector('.score').textContent = score;

    if (guess > sn) {
      document.querySelector('.message').textContent = '📈 Too high!';
    } else if (guess < sn) {
      document.querySelector('.message').textContent = '📉 Too low!';
    }
  }
});

document.querySelector('.again').addEventListener('click', function () {
  document.querySelector('body').style.backgroundColor = '#222';
  sn = Math.trunc(Math.random() * 20) + 1;
  document.querySelector('.message').textContent = 'Start guessing...';
  document.querySelector('.guess').value = '';
  score = 20;
  document.querySelector('.score').textContent = score;
  document.querySelector('.number').textContent = '?';
});
