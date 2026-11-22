# Charades

A party charades game for your phone. Hold it to your forehead, your friends act out the word, and you tilt to answer.

Play it: https://gamecharades.netlify.app

## How to play
1. Pick a category and a round length (30, 60 or 90 seconds)
2. Turn your phone sideways and press **Start**
3. During the 3-2-1 countdown, put the phone on your forehead, screen facing your friends
4. They act it out with no talking, and you guess
5. **Tilt down** if you got it, **tilt up** to skip
6. When time runs out, see every word you got and missed

On a laptop, use the buttons or the keyboard: **→** or **Space** for correct, **←** to skip.

## Features
- **Tilt controls** using the phone's motion sensor. On a phone, the buttons disappear once tilt is working
- **8 categories, 2,000+ words:** Animals, Movies, Ghana food, Actions, Jobs, Sports, Famous people, Objects
- **Custom category:** type your own words, like inside jokes or friends' names
- Green and red screen flashes, beeps and vibration on every answer
- A results screen listing every word you got and skipped
- Best score saved for each category

## How the tilt works
The browser reports the phone's angle many times a second (`deviceorientation`). The game turns that into one number for which way the screen is facing:

- `0` = upright on your forehead
- `-1` = screen facing the floor (tilted down = correct)
- `+1` = screen facing the ceiling (tilted up = skip)

It's calculated as `cos(beta) × cos(gamma)`, which works the same in portrait or landscape and doesn't jump around when the phone is upright. After a tilt counts, the phone has to come back upright before the next one counts, so one tilt can't score twice.

On iPhone, Safari asks for permission to use the motion sensor when you press Start. The tilt also only works over `https://`.

## Built with
HTML, CSS, JavaScript (no libraries). The sounds are made in code with the Web Audio API, so there are no audio files.

## Run it locally
Download the folder and open `index.html`. To test the tilt, deploy it (for example on Netlify) and open the link on your phone.
