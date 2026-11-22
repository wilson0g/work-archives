# Type or Die

A falling-words typing game. Type each word before it hits the red line, or lose a life.

Play it: https://typeracegame.netlify.app


## How to play
- Click **Start** and words begin falling from the top
- Type a word and it disappears the moment you finish it (no Enter needed)
- If a word crosses the red line, you lose a heart
- Lose all 3 hearts and it's game over
- Every 10 words you level up: words fall faster and appear more often

## Features
- 800+ words, including coding terms and Ghanaian words (jollof, waakye, kelewele...)
- The word you're typing gets highlighted, letter by letter
- Words turn red when they're about to cross the line
- The input box shakes if what you type doesn't match any word on screen
- Levels that get harder as you go
- Best score saved in your browser with `localStorage`

## How it works
**Game loop:** about 60 times a second, every word moves down a little. Movement is scaled by the time between frames, so the game runs at the same speed on any screen.

**Targeting:** as you type, the game looks for the word that starts with your letters and is closest to the red line, since that's the most urgent one. An exact match always wins, so typing "fast" still works when "faster" is also on screen.

**Difficulty:** fall speed goes up and the time between new words goes down with each level, with a limit so it stays playable.

## Built with
HTML, CSS, JavaScript (no libraries)

## Run it locally
Download the folder and open `index.html` in your browser.
