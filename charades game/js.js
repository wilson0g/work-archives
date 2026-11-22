// ---------- Elements ----------
const $ = id => document.getElementById(id);

const screens = { menu: $("menu-screen"), game: $("game-screen"), results: $("results-screen") };
const categoriesEl = $("categories");
const customBox = $("custom-box");
const customWords = $("custom-words");
const durationEl = $("duration");
const tiltToggle = $("tilt-toggle");
const menuError = $("menu-error");
const wordEl = $("word");
const timerEl = $("timer");
const progressBar = $("progress-bar");
const scoreEl = $("game-score");
const gameCategoryEl = $("game-category");

const TILT_ON = 0.6;
const TILT_OFF = 0.3;

let selected = null;
let deck = [], results = [], score = 0;
let timeLeft = 0, duration = 60, timerId = null;
let playing = false, tiltReady = true, tiltEnabled = false;
let audioCtx = null;
function buildMenu() {
  const all = { ...CATEGORIES, "Custom": { color: "#334155", words: null } };
  Object.entries(all).forEach(([name, cat]) => {
    const btn = document.createElement("button");
    btn.className = "cat";
    btn.style.background = cat.color;
    btn.textContent = name;
    btn.addEventListener("click", () => selectCategory(name, btn));
    categoriesEl.appendChild(btn);
  });
}

function selectCategory(name, btn) {
  selected = name;
  document.querySelectorAll(".cat").forEach(b => b.classList.remove("selected"));
  btn.classList.add("selected");
  customBox.classList.toggle("hidden", name !== "Custom");
  menuError.textContent = "";
}

function getWords() {
  if (selected === "Custom") {
    return customWords.value.split(/[,\n]/).map(w => w.trim()).filter(Boolean);
  }
  return CATEGORIES[selected].words;
}

function showScreen(name) {
  Object.values(screens).forEach(s => s.classList.add("hidden"));
  screens[name].classList.remove("hidden");
}
$("start-btn").addEventListener("click", async () => {
  if (!selected) {
    menuError.textContent = "Pick a category first";
    return;
  }
  const words = getWords();
  if (words.length < 5) {
    menuError.textContent = "Add at least 5 words to your custom list";
    return;
  }
  unlockAudio();
  tiltEnabled = tiltToggle.checked && await enableTilt();
  if (!tiltEnabled) screens.game.classList.remove("tilt-mode");
  startRound();
});

$("again-btn").addEventListener("click", startRound);
$("menu-btn").addEventListener("click", () => showScreen("menu"));

function startRound() {
  deck = shuffle([...getWords()]);
  results = [];
  score = 0;
  duration = Number(durationEl.value);
  timeLeft = duration;

  scoreEl.textContent = 0;
  gameCategoryEl.textContent = selected;
  timerEl.textContent = duration;
  progressBar.style.width = "100%";
  screens.game.style.background = selected === "Custom" ? "#334155" : CATEGORIES[selected].color;
  showScreen("game");

  let count = 3;
  playing = false;
  wordEl.textContent = count;
  const countdown = setInterval(() => {
    count--;
    if (count > 0) {
      wordEl.textContent = count;
      beep(500, 0.1);
    } else {
      clearInterval(countdown);
      beep(900, 0.2);
      playing = true;
      tiltReady = false;
      nextWord();
      timerId = setInterval(tick, 1000);
    }
  }, 1000);
}

function tick() {
  timeLeft--;
  timerEl.textContent = timeLeft;
  progressBar.style.width = `${(timeLeft / duration) * 100}%`;
  if (timeLeft <= 5 && timeLeft > 0) beep(700, 0.08);
  if (timeLeft <= 0) endRound();
}
function shuffle(arr) {
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

function nextWord() {
  if (deck.length === 0) deck = shuffle([...getWords()]);
  wordEl.textContent = deck.pop();
}

function answer(correct) {
  if (!playing) return;
  results.push({ word: wordEl.textContent, correct });
  if (correct) {
    score++;
    scoreEl.textContent = score;
  }

  const flash = correct ? "flash-correct" : "flash-skip";
  screens.game.classList.add(flash);
  setTimeout(() => screens.game.classList.remove(flash), 300);
  beep(correct ? 880 : 220, 0.15);
  if (navigator.vibrate) navigator.vibrate(correct ? 60 : [40, 40, 40]);

  nextWord();
}

$("correct-btn").addEventListener("click", () => answer(true));
$("skip-btn").addEventListener("click", () => answer(false));
document.addEventListener("keydown", e => {
  if (!playing) return;
  if (e.key === "ArrowRight" || e.code === "Space") { e.preventDefault(); answer(true); }
  if (e.key === "ArrowLeft") { e.preventDefault(); answer(false); }
});
function endRound() {
  playing = false;
  clearInterval(timerId);
  beep(300, 0.4);

  $("final-score").textContent = score;

  const key = `charadesBest_${selected}`;
  let best = 0;
  try { best = Number(localStorage.getItem(key)) || 0; } catch {}
  if (score > best) {
    best = score;
    try { localStorage.setItem(key, best); } catch {}
    $("best-line").textContent = `New best for ${selected}!`;
  } else {
    $("best-line").textContent = `correct · best ${best}`;
  }

  const list = $("results-list");
  list.innerHTML = "";
  results.forEach(r => {
    const li = document.createElement("li");
    li.className = r.correct ? "got" : "missed";
    li.textContent = `${r.correct ? "✓" : "✗"} ${r.word}`;
    list.appendChild(li);
  });

  showScreen("results");
}
async function enableTilt() {
  if (!("DeviceOrientationEvent" in window)) return false;
  if (typeof DeviceOrientationEvent.requestPermission === "function") {
    try {
      const result = await DeviceOrientationEvent.requestPermission();
      if (result !== "granted") return false;
    } catch {
      return false;
    }
  }
  window.removeEventListener("deviceorientation", onTilt);
  window.addEventListener("deviceorientation", onTilt);
  return true;
}

function onTilt(e) {
  if (!tiltEnabled || e.beta === null) return;

  if (!screens.game.classList.contains("tilt-mode")) {
    screens.game.classList.add("tilt-mode");
  }
  if (!playing) return;

  const rad = Math.PI / 180;
  const facing = Math.cos(e.beta * rad) * Math.cos(e.gamma * rad);

  if (Math.abs(facing) < TILT_OFF) {
    tiltReady = true;
  } else if (tiltReady && facing < -TILT_ON) {
    tiltReady = false;
    answer(true);
  } else if (tiltReady && facing > TILT_ON) {
    tiltReady = false;
    answer(false);
  }
}
function unlockAudio() {
  try {
    audioCtx = audioCtx || new (window.AudioContext || window.webkitAudioContext)();
    if (audioCtx.state === "suspended") audioCtx.resume();
  } catch {}
}

function beep(freq, seconds) {
  if (!audioCtx) return;
  const osc = audioCtx.createOscillator();
  const gain = audioCtx.createGain();
  osc.frequency.value = freq;
  gain.gain.setValueAtTime(0.2, audioCtx.currentTime);
  gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + seconds);
  osc.connect(gain).connect(audioCtx.destination);
  osc.start();
  osc.stop(audioCtx.currentTime + seconds);
}

buildMenu();