const WORDS = [
  "java", "loop", "code", "byte", "node", "class", "array", "stack", "queue", "debug",
  "pixel", "cache", "logic", "input", "output", "syntax", "binary", "server", "python", "string",
  "object", "method", "import", "return", "public", "static", "boolean", "integer", "compile", "runtime",
  "planet", "rocket", "galaxy", "comet", "orbit", "nebula", "meteor", "lunar", "solar", "cosmos",
  "ghana", "accra", "kumasi", "jollof", "banku", "kenkey", "waakye", "kelewele", "plantain", "fufu",
  "river", "ocean", "forest", "desert", "island", "valley", "mountain", "thunder", "storm", "breeze",
  "tiger", "zebra", "falcon", "dolphin", "panther", "rabbit", "monkey", "parrot", "turtle", "lizard",
  "music", "guitar", "drums", "piano", "rhythm", "melody", "chorus", "violin", "trumpet", "speaker",
  "laptop", "keyboard", "monitor", "mouse", "router", "browser", "website", "network", "battery", "charger",
  "quick", "brave", "silent", "bright", "frozen", "golden", "hidden", "mighty", "gentle", "wild",
  "jump", "run", "type", "fast", "win", "lose", "rage", "focus", "speed", "faster",
  "algorithm", "function", "variable", "recursion", "database", "framework", "interface", "developer", "able", "about",
  "above", "accept", "across", "action", "active", "actor", "actual", "adapt", "admit", "adult",
  "advice", "afford", "after", "again", "agent", "agree", "ahead", "alarm", "album", "alive",
  "allow", "almost", "alone", "along", "already", "always", "amazing", "amount", "anchor", "angle",
  "animal", "answer", "anyone", "appear", "apple", "area", "argue", "arrive", "artist", "aspect",
  "assume", "attack", "attempt", "author", "autumn", "avoid", "award", "aware", "baby", "back",
  "badge", "baker", "balance", "ball", "banana", "band", "bank", "basic", "basket", "battle",
  "beach", "beauty", "become", "bedroom", "before", "begin", "behind", "belief", "belong", "below",
  "bench", "beside", "better", "beyond", "bicycle", "bird", "birthday", "black", "blade", "blanket",
  "blind", "block", "blood", "board", "boat", "body", "bonus", "book", "border", "bottle",
  "bottom", "bounce", "brain", "branch", "bread", "break", "breath", "bridge", "brief", "bring",
  "broken", "brother", "brown", "budget", "build", "bullet", "bundle", "burden", "butter", "button",
  "cabin", "cable", "cactus", "camera", "camp", "campus", "candle", "candy", "canvas", "capital",
  "captain", "carbon", "career", "carpet", "carry", "castle", "catch", "cattle", "cause", "ceiling",
  "center", "chain", "chair", "chalk", "chance", "change", "chapter", "charge", "chase", "cheap",
  "check", "cheese", "cherry", "chicken", "chief", "child", "choice", "choose", "circle", "citizen",
  "city", "claim", "clean", "clever", "client", "climb", "clock", "close", "cloud", "clown",
  "coach", "coast", "coffee", "coin", "collect", "college", "colour", "column", "combine", "comfort",
  "common", "company", "compare", "concert", "connect", "contest", "control", "cookie", "copper", "corner",
  "cotton", "couch", "count", "country", "couple", "course", "cousin", "cover", "crack", "craft",
  "crash", "crazy", "cream", "create", "credit", "crowd", "crown", "cruise", "crystal", "culture",
  "curtain", "custom", "cycle", "damage", "dance", "danger", "daring", "daughter", "decade", "decide",
  "deep", "degree", "delay", "deliver", "demand", "depend", "design", "detail", "device", "diamond",
  "dinner", "direct", "dirty", "doctor", "dollar", "domain", "double", "dragon", "drama", "dream",
  "dress", "drink", "drive", "driver", "early", "earth", "easily", "eagle", "effort", "eight",
  "elbow", "elder", "eleven", "empire", "empty", "energy", "engine", "enjoy", "enough", "entire",
  "equal", "escape", "event", "exact", "example", "excite", "exercise", "expert", "explain", "extra",
  "fabric", "factor", "family", "famous", "fancy", "farmer", "father", "feather", "feature", "fever",
  "field", "figure", "final", "finger", "finish", "flame", "flash", "flight", "float", "flower",
  "follow", "forget", "fortune", "forward", "fossil", "fountain", "fresh", "friend", "fruit", "future",
  "garden", "gather", "giant", "ginger", "giraffe", "glass", "global", "glory", "glove", "goal",
  "gold", "grace", "grade", "grain", "grand", "grape", "grass", "gravity", "great", "green",
  "grocery", "ground", "group", "growth", "guard", "guess", "guest", "guide", "habit", "hammer",
  "handle", "happen", "happy", "harbor", "harvest", "health", "heart", "heavy", "height", "hello",
  "helmet", "hero", "highway", "history", "hockey", "holiday", "honey", "honest", "hope", "horizon",
  "horse", "hospital", "hotel", "house", "human", "humble", "hunger", "hurry", "idea", "image",
  "impact", "income", "index", "injury", "insect", "inside", "invite", "iron", "jacket", "jelly",
  "jewel", "joke", "journey", "judge", "juice", "jungle", "junior", "kettle", "kidney", "kingdom",
  "kitchen", "kitten", "knife", "ladder", "large", "later", "laugh", "lawyer", "layer", "leader",
  "learn", "lemon", "lesson", "letter", "level", "library", "light", "limit", "liquid", "little",
  "local", "logo", "lucky", "lunch", "machine", "magic", "magnet", "major", "manage", "mango",
  "marble", "market", "master", "matter", "meadow", "medal", "member", "memory", "mercy", "middle",
  "midnight", "minute", "mirror", "mission", "mobile", "model", "modern", "moment", "money", "month",
  "morning", "mother", "motion", "motor", "movie", "muscle", "museum", "mystery", "narrow", "nation",
  "nature", "needle", "nephew", "nerve", "never", "noble", "noodle", "normal", "notice", "number",
  "nurse", "office", "often", "olive", "onion", "orange", "order", "oxygen", "paddle", "palace",
  "panel", "panic", "paper", "parent", "party", "pass", "patch", "path", "pencil", "people",
  "pepper", "perfect", "permit", "person", "phone", "photo", "picnic", "pillow", "pilot", "plastic",
  "player", "pocket", "poem", "point", "police", "pond", "popular", "portion", "potato", "power",
  "praise", "prayer", "present", "price", "pride", "print", "prison", "prize", "problem", "profit",
  "promise", "proud", "puzzle", "pyramid", "quality", "quarter", "queen", "question", "quiet", "radar",
  "radio", "rain", "rapid", "rare", "reason", "record", "region", "relax", "remote", "repair",
  "report", "rescue", "result", "reward", "ribbon", "rice", "rich", "riddle", "ripple", "ritual",
  "robot", "rough", "round", "royal", "rubber", "ruler", "sadness", "safety", "sail", "salad",
  "salt", "sample", "sand", "scale", "school", "science", "scissors", "season", "secret", "seed",
  "select", "sense", "series", "seven", "shadow", "shape", "share", "shark", "shelf", "shield",
  "shine", "shirt", "shock", "shoulder", "signal", "silver", "simple", "sister", "sketch", "skill",
  "sleep", "slice", "slow", "smile", "smoke", "snack", "snake", "soccer", "social", "socket",
  "soft", "soldier", "solid", "soup", "south", "space", "spare", "spirit", "sponge", "spoon",
  "sport", "spring", "square", "stable", "stadium", "stairs", "stamp", "star", "station", "steel",
  "stem", "stick", "stone", "street", "strong", "student", "studio", "style", "sugar", "summer",
  "sunset", "supper", "supply", "surface", "surprise", "swing", "symbol", "system", "table", "tablet",
  "talent", "target", "teacher", "temple", "tennis", "thank", "theory", "thirsty", "ticket", "timber",
  "toast", "today", "tomato", "tongue", "tonight", "tooth", "topic", "total", "tower", "town",
  "toy", "track", "traffic", "train", "travel", "treasure", "tribe", "trophy", "truck", "trust",
  "truth", "tunnel", "twelve", "twin", "umbrella", "uncle", "under", "unique", "update", "upload",
  "useful", "value", "velvet", "vessel", "victory", "village", "vintage", "visit", "vital", "voice",
  "volume", "voyage", "wagon", "waiter", "wallet", "warm", "water", "wealth", "weather", "wedding",
  "window", "winter", "wisdom", "wonder", "wooden", "world", "worry", "yellow", "yogurt", "young",
  "zero", "zigzag"
];

const DANGER_Y = 430;
const START_LIVES = 3;

const gameEl = document.getElementById("game");
const inputEl = document.getElementById("input");
const scoreEl = document.getElementById("score");
const levelEl = document.getElementById("level");
const livesEl = document.getElementById("lives");
const bestEl = document.getElementById("best");
const overlayEl = document.getElementById("overlay");
const overlayTitle = document.getElementById("overlay-title");
const overlayText = document.getElementById("overlay-text");
const startBtn = document.getElementById("start-btn");

let words, score, lives, level, typedCount, spawnTimer, running, lastTime;
let best = loadBest();
bestEl.textContent = best;
renderLives(START_LIVES);

function loadBest() {
  try { return Number(localStorage.getItem("typeOrDieBest")) || 0; }
  catch { return 0; }
}

function saveBest() {
  try { localStorage.setItem("typeOrDieBest", best); } catch {}
}
function startGame() {
  words?.forEach(w => w.el.remove());
  words = [];
  score = 0;
  lives = START_LIVES;
  level = 1;
  typedCount = 0;
  spawnTimer = 0;
  running = true;

  scoreEl.textContent = 0;
  levelEl.textContent = 1;
  renderLives(lives);
  overlayEl.classList.add("hidden");

  inputEl.disabled = false;
  inputEl.value = "";
  inputEl.focus();

  lastTime = performance.now();
  requestAnimationFrame(loop);
}

function gameOver() {
  running = false;
  inputEl.disabled = true;

  const newBest = score > best;
  if (newBest) {
    best = score;
    saveBest();
    bestEl.textContent = best;
  }

  overlayTitle.textContent = "Game over";
  overlayText.textContent = newBest
    ? `New best: ${score}! You typed ${typedCount} words.`
    : `Score: ${score} · You typed ${typedCount} words.`;
  startBtn.textContent = "Play again";
  overlayEl.classList.remove("hidden");
  startBtn.focus();
}

startBtn.addEventListener("click", startGame);

function fallSpeed() { return 0.35 + level * 0.12; }
function spawnDelay() { return Math.max(1800 - level * 150, 600); }


function spawnWord() {
  const onScreen = new Set(words.map(w => w.text));
  const options = WORDS.filter(w => !onScreen.has(w));
  const text = options[Math.floor(Math.random() * options.length)];

  const el = document.createElement("div");
  el.className = "word";
  el.textContent = text;
  gameEl.appendChild(el);

  const maxX = gameEl.clientWidth - el.offsetWidth - 10;
  const x = 10 + Math.random() * Math.max(maxX - 10, 0);
  el.style.left = `${x}px`;

  words.push({ text, y: 55, el });
}

function removeWord(word, popped) {
  words = words.filter(w => w !== word);
  if (popped) {
    word.el.classList.add("pop");
    setTimeout(() => word.el.remove(), 200);
  } else {
    word.el.remove();
  }
}
inputEl.addEventListener("input", () => {
  const typed = inputEl.value.trim().toLowerCase();
  const target = findTarget(typed);

  highlight(target, typed);

  if (typed && !target) {
    inputEl.classList.remove("wrong");
    void inputEl.offsetWidth;
    inputEl.classList.add("wrong");
  } else {
    inputEl.classList.remove("wrong");
  }

  if (target && typed === target.text) {
    score += target.text.length * 10;
    typedCount++;
    level = 1 + Math.floor(typedCount / 10);
    scoreEl.textContent = score;
    levelEl.textContent = level;
    removeWord(target, true);
    inputEl.value = "";
    highlight(null, "");
  }
});
function findTarget(typed) {
  if (!typed) return null;
  const exact = words.find(w => w.text === typed);
  if (exact) return exact;
  return words
    .filter(w => w.text.startsWith(typed))
    .sort((a, b) => b.y - a.y)[0] || null;
}

function highlight(target, typed) {
  words.forEach(w => {
    if (w === target) {
      w.el.classList.add("target");
      w.el.innerHTML = `<span class="typed">${typed}</span>${w.text.slice(typed.length)}`;
    } else if (w.el.classList.contains("target")) {
      w.el.classList.remove("target");
      w.el.textContent = w.text;
    }
  });
}

function renderLives(n) {
  livesEl.innerHTML = "";
  for (let i = 0; i < START_LIVES; i++) {
    const heart = document.createElement("span");
    heart.textContent = "♥";
    if (i >= n) heart.className = "lost";
    livesEl.appendChild(heart);
  }
}

function loseLife(word) {
  removeWord(word, false);
  lives--;
  renderLives(lives);

  gameEl.classList.remove("hit");
  void gameEl.offsetWidth;
  gameEl.classList.add("hit");
  if (!findTarget(inputEl.value.trim().toLowerCase())) inputEl.value = "";

  if (lives <= 0) gameOver();
}
function loop(time) {
  if (!running) return;

  const elapsed = time - lastTime;
  lastTime = time;
  const dt = Math.min(elapsed / (1000 / 60), 3);

  spawnTimer -= elapsed;
  if (spawnTimer <= 0) {
    spawnWord();
    spawnTimer = spawnDelay();
  }

  for (const w of [...words]) {
    w.y += fallSpeed() * dt;
    w.el.style.top = `${w.y}px`;
    w.el.classList.toggle("near", w.y > DANGER_Y - 80);

    if (w.y + w.el.offsetHeight >= DANGER_Y) {
      loseLife(w);
      if (!running) return;
    }
  }

  requestAnimationFrame(loop);
}