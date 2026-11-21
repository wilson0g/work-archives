Flappy bird 

A Flappy Bird–style game built from scratch on an HTML canvas. Looks easy. It isn't.

Play it: https://flappybirdart.netlify.app

How to play
Press Space, ↑, or click (or tap on your phone) to flap
Fly through the gaps between the pipes
Each pipe you pass is +1 point
Hit a pipe or the ground and it's game over
The game speeds up the further you get
Features
Smooth 60fps game loop using requestAnimationFrame
Gravity and flap physics
Circle-to-rectangle collision detection
Speed increases as your score goes up
Best score saved in your browser with localStorage
Works with mouse, keyboard and touch
How it works

Game loop: about 60 times a second, the game updates everything (bird, pipes, score), then redraws the whole canvas.

Physics: every frame, gravity is added to the bird's falling speed. A flap sets that speed to a negative number, so the bird jumps up and then falls again.

Collisions: the bird is a circle and each pipe is a rectangle. The game finds the point on the rectangle closest to the bird's centre. If that point is closer than the bird's radius, it's a hit.

Same speed on every screen: movement is scaled by the time between frames, so the game runs at the same speed on a 60Hz or a 120Hz display.

Built with

HTML, CSS, JavaScript (no libraries)

Run it locally

Download the folder and open index.html in your browser.
