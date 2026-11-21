# Unlimited Wordle

A Wordle clone you can play as many times as you want. A new random word comes up every game.

To Play it: https://unlimited-wordle.netlify.app
## Features
- Guess a 5-letter word in 6 tries
- Green, yellow and grey tiles with a flip animation
- On-screen keyboard that changes colour as you play
- Works with your physical keyboard too
- Rejects words that don't exist ("Not in word list") and shakes the row
- 1,330 possible answers, from easy to hard (PSHAW, anyone?)
- 12,600+ valid guesses

## How it works
The trickiest part is colouring repeated letters correctly. If the answer is GUEST and you guess DRESS, only one S should turn green and the other should stay grey.

The game scores each guess in two passes:
1. **Greens first:** mark letters in the exact right spot, and count the letters left over in the answer.
2. **Then yellows:** mark a letter yellow only if that letter is still available in the leftover count.

The game also uses two word lists, the same way the real Wordle does:
- `plentywords.js`: the possible answers, so the answer is always a real, fair word
- `wordsvalidation.js`: every valid 5-letter word, used to check guesses

## Built with
HTML, CSS, JavaScript (no libraries)

## Run it locally
Download the folder and open `index.html` in your browser.
