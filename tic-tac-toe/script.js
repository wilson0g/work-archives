const boardEl = document.getElementById("board");
const statusEl = document.getElementById("status");
const statsEl = document.getElementById("stats");
const restartBtn = document.getElementById("restart");

const HUMAN = "X";
const AI = "O";
const WIN_LINES = [
  [0, 1, 2], [3, 4, 5], [6, 7, 8], // rows
  [0, 3, 6], [1, 4, 7], [2, 5, 8], // columns
  [0, 4, 8], [2, 4, 6]             // diagonals
];

let board, gameOver, locked, aiTimer, positionsChecked;
const scores = { X: 0, O: 0, draw: 0 };

function init() {
  clearTimeout(aiTimer);
  board = Array(9).fill(null);
  gameOver = false;
  locked = false;
  boardEl.innerHTML = "";
  for (let i = 0; i < 9; i++) {
    const cell = document.createElement("div");
    cell.className = "cell";
    cell.addEventListener("click", () => humanMove(i));
    boardEl.appendChild(cell);
  }
  statusEl.textContent = "Your turn";
  statsEl.textContent = "";
}

function render(winLine = null) {
  boardEl.querySelectorAll(".cell").forEach((cell, i) => {
    cell.textContent = board[i] || "";
    cell.className = "cell";
    if (board[i]) cell.classList.add(board[i].toLowerCase());
    if (winLine && winLine.includes(i)) cell.classList.add("win");
  });
}

function getWinner(b) {
  for (const line of WIN_LINES) {
    const [a, c, d] = line;
    if (b[a] && b[a] === b[c] && b[a] === b[d]) return { player: b[a], line };
  }
  if (b.every(Boolean)) return { player: "draw", line: null };
  return null;
}

function humanMove(i) {
  if (gameOver || locked || board[i]) return;
  board[i] = HUMAN;
  render();
  if (checkEnd()) return;
  locked = true;
  statusEl.textContent = "AI is thinking...";
  aiTimer = setTimeout(aiMove, 300);
}

function aiMove() {
  positionsChecked = 0;
  let bestScore = -Infinity;
  let bestMove = null;

  for (let i = 0; i < 9; i++) {
    if (!board[i]) {
      board[i] = AI;
      const score = minimax(board, 0, false);
      board[i] = null;
      if (score > bestScore) {
        bestScore = score;
        bestMove = i;
      }
    }
  }

  board[bestMove] = AI;
  locked = false;
  statsEl.textContent = `AI checked ${positionsChecked.toLocaleString()} positions`;
  render();
  if (!checkEnd()) statusEl.textContent = "Your turn";
}

// Minimax: AI maximizes, human minimizes.
// Depth makes the AI prefer faster wins and slower losses.
function minimax(b, depth, isMaximizing) {
  positionsChecked++;
  const result = getWinner(b);
  if (result) {
    if (result.player === AI) return 10 - depth;
    if (result.player === HUMAN) return depth - 10;
    return 0;
  }

  let best = isMaximizing ? -Infinity : Infinity;
  for (let i = 0; i < 9; i++) {
    if (!b[i]) {
      b[i] = isMaximizing ? AI : HUMAN;
      const score = minimax(b, depth + 1, !isMaximizing);
      b[i] = null;
      best = isMaximizing ? Math.max(best, score) : Math.min(best, score);
    }
  }
  return best;
}

function checkEnd() {
  const result = getWinner(board);
  if (!result) return false;

  gameOver = true;
  render(result.line);

  if (result.player === "draw") {
    scores.draw++;
    statusEl.textContent = "Draw. Told you it's unbeatable.";
  } else if (result.player === HUMAN) {
    scores.X++;
    statusEl.textContent = "You won?! That shouldn't happen.";
  } else {
    scores.O++;
    statusEl.textContent = "AI wins.";
  }

  document.getElementById("score-x").textContent = scores.X;
  document.getElementById("score-o").textContent = scores.O;
  document.getElementById("score-d").textContent = scores.draw;
  return true;
}

restartBtn.addEventListener("click", init);
init();