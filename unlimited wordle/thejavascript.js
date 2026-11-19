const MAX_GUESSES = 6;
const WORD_LENGTH = 5;
const KEY_ROWS = [
  ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
  ["a", "s", "d", "f", "g", "h", "j", "k", "l"],
  ["enter", "z", "x", "c", "v", "b", "n", "m", "back"]
];

const boardEl = document.getElementById("board");
const keyboardEl = document.getElementById("keyboard");
const messageEl = document.getElementById("message");
const restartBtn = document.getElementById("restart");

let answer, currentRow, currentCol, guesses, gameOver, revealing;

function init() {
  answer = WORDS[Math.floor(Math.random() * WORDS.length)];
  currentRow = 0;
  currentCol = 0;
  guesses = Array(MAX_GUESSES).fill("");
  gameOver = false;
  revealing = false;
  messageEl.textContent = "";
  restartBtn.classList.add("hidden");
  buildBoard();
  buildKeyboard();
}

function buildBoard() {
  boardEl.innerHTML = "";
  for (let r = 0; r < MAX_GUESSES; r++) {
    const row = document.createElement("div");
    row.className = "row";
    for (let c = 0; c < WORD_LENGTH; c++) {
      const tile = document.createElement("div");
      tile.className = "tile";
      row.appendChild(tile);
    }
    boardEl.appendChild(row);
  }
}

function buildKeyboard() {
  keyboardEl.innerHTML = "";
  KEY_ROWS.forEach(keys => {
    const row = document.createElement("div");
    row.className = "key-row";
    keys.forEach(k => {
      const btn = document.createElement("button");
      btn.className = "key" + (k.length > 1 ? " wide" : "");
      btn.textContent = k === "back" ? "⌫" : k;
      btn.dataset.key = k;
      btn.addEventListener("click", () => {
        btn.blur();
        handleKey(k);
      });
      row.appendChild(btn);
    });
    keyboardEl.appendChild(row);
  });
}

function getTile(r, c) {
  return boardEl.children[r].children[c];
}

function handleKey(key) {
  if (gameOver || revealing) return;
  if (key === "enter") submitGuess();
  else if (key === "back") deleteLetter();
  else if (/^[a-z]$/.test(key)) addLetter(key);
}

function addLetter(letter) {
  if (currentCol >= WORD_LENGTH) return;
  const tile = getTile(currentRow, currentCol);
  tile.textContent = letter;
  tile.classList.add("filled");
  guesses[currentRow] += letter;
  currentCol++;
}

function deleteLetter() {
  if (currentCol === 0) return;
  currentCol--;
  const tile = getTile(currentRow, currentCol);
  tile.textContent = "";
  tile.classList.remove("filled");
  guesses[currentRow] = guesses[currentRow].slice(0, -1);
}

function showMessage(text, duration = 1500) {
  messageEl.textContent = text;
  if (duration) {
    setTimeout(() => {
      if (messageEl.textContent === text) messageEl.textContent = "";
    }, duration);
  }
}

function submitGuess() {
  const guess = guesses[currentRow];

  if (guess.length < WORD_LENGTH) {
    showMessage("Not enough letters");
    shakeRow();
    return;
  }

  if (!VALID_GUESSES.has(guess)) {
    showMessage("Not in word list");
    shakeRow();
    return;
  }

  revealRow(guess, scoreGuess(guess, answer));
}

function shakeRow() {
  const row = boardEl.children[currentRow];
  row.classList.remove("shake");
  void row.offsetWidth; // restarts the animation
  row.classList.add("shake");
}

function scoreGuess(guess, answer) {
  const result = Array(WORD_LENGTH).fill("grey");
  const remaining = {};

  // Pass 1: greens, and count the answer letters left over
  for (let i = 0; i < WORD_LENGTH; i++) {
    if (guess[i] === answer[i]) result[i] = "green";
    else remaining[answer[i]] = (remaining[answer[i]] || 0) + 1;
  }

  // Pass 2: yellows, only if that letter is still available
  for (let i = 0; i < WORD_LENGTH; i++) {
    if (result[i] !== "green" && remaining[guess[i]] > 0) {
      result[i] = "yellow";
      remaining[guess[i]]--;
    }
  }
  return result;
}

function revealRow(guess, colors) {
  revealing = true;
  const row = currentRow;

  colors.forEach((color, i) => {
    setTimeout(() => {
      const tile = getTile(row, i);
      tile.classList.add("flip");
      setTimeout(() => tile.classList.add(color), 250); // colour appears mid-flip
    }, i * 300);
  });

  setTimeout(() => {
    colors.forEach((color, i) => updateKey(guess[i], color));
    revealing = false;
    checkResult(guess);
  }, WORD_LENGTH * 300 + 300);
}

const RANK = { grey: 1, yellow: 2, green: 3 };
function updateKey(letter, color) {
  const key = keyboardEl.querySelector(`[data-key="${letter}"]`);
  const current = ["green", "yellow", "grey"].find(c => key.classList.contains(c));
  if (current && RANK[current] >= RANK[color]) return;
  key.classList.remove("green", "yellow", "grey");
  key.classList.add(color);
}

function checkResult(guess) {
  if (guess === answer) {
    gameOver = true;
    const praise = ["Genius!", "Magnificent!", "Impressive!", "Splendid!", "Great!", "Phew!"];
    showMessage(praise[currentRow], 0);
    restartBtn.classList.remove("hidden");
    return;
  }
  currentRow++;
  currentCol = 0;
  if (currentRow === MAX_GUESSES) {
    gameOver = true;
    showMessage(`The word was ${answer.toUpperCase()}`, 0);
    restartBtn.classList.remove("hidden");
  }
}

document.addEventListener("keydown", e => {
  if (e.metaKey || e.ctrlKey) return; // let Cmd+R etc. work
  if (e.key === "Enter") {
    e.preventDefault();
    handleKey("enter");
  } else if (e.key === "Backspace") {
    handleKey("back");
  } else {
    handleKey(e.key.toLowerCase());
  }
});

restartBtn.addEventListener("click", init);
init();