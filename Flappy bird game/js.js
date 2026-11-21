const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");
const W = canvas.width;
const H = canvas.height;
const GRAVITY = 0.45;
const FLAP_POWER = -7.5;
const BIRD_X = 90;
const BIRD_R = 14;
const PIPE_W = 60;
const GAP = 150;          // space between top and bottom pipe
const PIPE_SPACING = 200; // horizontal distance between pipes
const GROUND_H = 60;

let state;  // "ready", "playing" or "over"
let bird, pipes, score, speed, groundX, overTime;
let best = loadBest();

const stars = Array.from({ length: 30 }, () => ({
  x: Math.random() * W,
  y: Math.random() * (H - GROUND_H - 100),
  r: Math.random() * 1.5 + 0.5
}));

function reset() {
  state = "ready";
  bird = { y: H / 2 - 40, vy: 0 };
  pipes = [];
  score = 0;
  speed = 2.5;
  groundX = 0;
}

function loadBest() {
  try { return Number(localStorage.getItem("flappyBest")) || 0; }
  catch { return 0; }
}

function saveBest() {
  try { localStorage.setItem("flappyBest", best); } catch {}
}

function flap() {
  if (state === "ready") {
    state = "playing";
    bird.vy = FLAP_POWER;
  } else if (state === "playing") {
    bird.vy = FLAP_POWER;
  } else if (state === "over" && performance.now() - overTime > 600) {
    reset(); // short delay so a panic-tap doesn't skip the game over screen
  }
}

document.addEventListener("keydown", e => {
  if (e.code === "Space" || e.code === "ArrowUp") {
    e.preventDefault();
    flap();
  }
});
canvas.addEventListener("mousedown", flap);
canvas.addEventListener("touchstart", e => {
  e.preventDefault();
  flap();
}, { passive: false });

function addPipe() {
  const minY = 80 + GAP / 2;
  const maxY = H - GROUND_H - 80 - GAP / 2;
  const gapY = minY + Math.random() * (maxY - minY); // centre of the gap
  pipes.push({ x: W, gapY, passed: false });
}

function update(dt, time) {
  if (state === "ready") {
    bird.y = H / 2 - 40 + Math.sin(time / 300) * 6; // gentle bobbing
    groundX = (groundX - speed * dt) % 24;
    return;
  }

  // Gravity pulls the bird down every frame
  bird.vy += GRAVITY * dt;
  bird.y += bird.vy * dt;

  if (state === "over") {
    // Let the bird fall to the ground after dying
    bird.y = Math.min(bird.y, H - GROUND_H - BIRD_R);
    return;
  }

  groundX = (groundX - speed * dt) % 24;

  // Move pipes and spawn new ones
  pipes.forEach(p => (p.x -= speed * dt));
  if (pipes.length === 0 || pipes[pipes.length - 1].x < W - PIPE_SPACING) addPipe();
  pipes = pipes.filter(p => p.x + PIPE_W > -10);

  pipes.forEach(p => {
    if (!p.passed && p.x + PIPE_W < BIRD_X) {
      p.passed = true;
      score++;
      speed = Math.min(2.5 + score * 0.05, 4.5);
    }
  });

  // Ceiling: stop at the top
  if (bird.y - BIRD_R < 0) {
    bird.y = BIRD_R;
    bird.vy = 0;
  }

  // Ground or pipe = game over
  if (bird.y + BIRD_R >= H - GROUND_H || pipes.some(hitsPipe)) gameOver();
}

function hitsPipe(p) {
  const topRect = { x: p.x, y: 0, w: PIPE_W, h: p.gapY - GAP / 2 };
  const bottomY = p.gapY + GAP / 2;
  const bottomRect = { x: p.x, y: bottomY, w: PIPE_W, h: H - GROUND_H - bottomY };
  return circleHitsRect(BIRD_X, bird.y, BIRD_R - 2, topRect) ||
         circleHitsRect(BIRD_X, bird.y, BIRD_R - 2, bottomRect);
}

// Find the closest point on the rectangle to the circle's centre
function circleHitsRect(cx, cy, r, rect) {
  const nearestX = Math.max(rect.x, Math.min(cx, rect.x + rect.w));
  const nearestY = Math.max(rect.y, Math.min(cy, rect.y + rect.h));
  const dx = cx - nearestX;
  const dy = cy - nearestY;
  return dx * dx + dy * dy < r * r;
}

function gameOver() {
  state = "over";
  overTime = performance.now();
  if (score > best) {
    best = score;
    saveBest();
  }
}

function draw() {
  ctx.fillStyle = "#1e293b";
  ctx.fillRect(0, 0, W, H);
  ctx.fillStyle = "#e2e8f0";
  stars.forEach(s => {
    ctx.beginPath();
    ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
    ctx.fill();
  });
  ctx.fillStyle = "#fde68a";
  ctx.beginPath();
  ctx.arc(290, 80, 22, 0, Math.PI * 2);
  ctx.fill();

  pipes.forEach(drawPipe);
  drawGround();
  drawBird();
  drawText();
}

function drawPipe(p) {
  const topH = p.gapY - GAP / 2;
  const bottomY = p.gapY + GAP / 2;

  ctx.fillStyle = "#22c55e";
  ctx.fillRect(p.x, 0, PIPE_W, topH);
  ctx.fillRect(p.x, bottomY, PIPE_W, H - GROUND_H - bottomY);

  // Pipe caps
  ctx.fillStyle = "#16a34a";
  ctx.fillRect(p.x - 6, topH - 20, PIPE_W + 12, 20);
  ctx.fillRect(p.x - 6, bottomY, PIPE_W + 12, 20);
}

function drawGround() {
  const y = H - GROUND_H;
  ctx.fillStyle = "#78350f";
  ctx.fillRect(0, y, W, GROUND_H);
  ctx.fillStyle = "#65a30d";
  ctx.fillRect(0, y, W, 10);

  // Moving stripes make the ground look like it's scrolling
  ctx.fillStyle = "#92400e";
  for (let x = groundX; x < W; x += 24) {
    ctx.fillRect(x, y + 18, 12, 6);
  }
}

function drawBird() {
  // Tilt up when rising, nose-dive when falling
  const angle = Math.max(-0.5, Math.min(bird.vy / 10, 1.2));

  ctx.save();
  ctx.translate(BIRD_X, bird.y);
  ctx.rotate(angle);

  ctx.fillStyle = "#fb923c"; // body
  ctx.beginPath();
  ctx.arc(0, 0, BIRD_R, 0, Math.PI * 2);
  ctx.fill();

  ctx.fillStyle = "#fdba74"; // wing
  ctx.beginPath();
  ctx.ellipse(-5, 4, 8, 5, 0, 0, Math.PI * 2);
  ctx.fill();

  ctx.fillStyle = "#fff"; // eye
  ctx.beginPath();
  ctx.arc(5, -5, 5, 0, Math.PI * 2);
  ctx.fill();
  ctx.fillStyle = "#0f172a";
  ctx.beginPath();
  ctx.arc(6.5, -5, 2.2, 0, Math.PI * 2);
  ctx.fill();

  ctx.fillStyle = "#facc15"; // beak
  ctx.beginPath();
  ctx.moveTo(12, -1);
  ctx.lineTo(22, 2);
  ctx.lineTo(12, 5);
  ctx.fill();

  ctx.restore();
}

function outlinedText(text, x, y, size) {
  ctx.font = `bold ${size}px system-ui, sans-serif`;
  ctx.textAlign = "center";
  ctx.lineWidth = 4;
  ctx.strokeStyle = "#0f172a";
  ctx.strokeText(text, x, y);
  ctx.fillStyle = "#fff";
  ctx.fillText(text, x, y);
}

function drawText() {
  if (state === "ready") {
    outlinedText("Get ready", W / 2, 160, 36);
    outlinedText("Tap or press Space", W / 2, 330, 18);
    return;
  }
  outlinedText(score, W / 2, 70, 48);

  if (state === "over") {
    ctx.fillStyle = "rgba(15, 23, 42, 0.75)";
    ctx.fillRect(50, 170, W - 100, 170);
    outlinedText("Game over", W / 2, 215, 34);
    outlinedText(`Score: ${score}   Best: ${best}`, W / 2, 260, 20);
    outlinedText(score > 0 && score === best ? "New best!" : "One more try?", W / 2, 295, 18);
    outlinedText("Click to restart", W / 2, 325, 14);
  }
}
let lastTime = performance.now();

function loop(time) {
  const dt = Math.min((time - lastTime) / (1000 / 60), 3);
  lastTime = time;

  update(dt, time);
  draw();
  requestAnimationFrame(loop);
}

reset();
requestAnimationFrame(loop);