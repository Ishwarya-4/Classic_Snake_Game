# 🐍 Classic Snake Game

A fully functional recreation of the classic Snake game built with Python's `turtle` module, using Object-Oriented Programming principles. Guide the snake to eat food, grow longer, and beat your high score — all without hitting the walls or yourself!

---

## 🎮 Gameplay

- Use the **arrow keys** to steer the snake
- Each piece of food eaten grows the snake and increments your score by 1
- The game resets if the snake hits a wall or bites its own body
- Your **high score is saved** to disk and persists between sessions

---

## 🗂️ Project Structure

```
Classic_Snake_Game/
├── main.py          # Game loop — wires all components together
├── snake.py         # Snake class (movement, growth, collision reset)
├── food.py          # Food class (random placement)
├── scoreboard.py    # ScoreBoard class (live score + persistent high score)
├── borderbox.py     # BorderBox class (draws the game boundary)
└── score.txt        # Stores the all-time high score
```

---

## 🧱 Classes Overview

### `Snake` *(snake.py)*
Manages the snake's body as a list of turtle segments. Starts with 3 segments at the centre of the screen. Each frame, segments follow the one ahead of them, giving the illusion of smooth movement. Prevents illegal 180° reversals (e.g. you can't go right while moving left). When a collision occurs, all segments are cleared off-screen and the snake is rebuilt from scratch.

| Constant | Value | Description |
|---|---|---|
| `MOVE_DISTANCE` | 20px | Distance moved per frame |
| `STARTING_POSITIONS` | (0,0), (-20,0), (-40,0) | Initial 3-segment layout |

### `Food` *(food.py)*
A small yellow circle that teleports to a random location within the play area each time the snake eats it. Inherits from `Turtle`.

### `ScoreBoard` *(scoreboard.py)*
Displays the current score and all-time high score at the top of the screen. Reads the high score from `score.txt` on startup and writes a new one back whenever the current score beats it. Inherits from `Turtle`.

### `BorderBox` *(borderbox.py)*
Draws the white rectangular boundary that defines the playable area. The main game loop checks the snake's coordinates against these walls to detect collisions. Inherits from `Turtle`.

---

## 🚀 Getting Started

**Prerequisites:** Python 3.x (no third-party libraries required — uses the built-in `turtle` module)

```bash
git clone https://github.com/Ishwarya-4/Classic_Snake_Game.git
cd Classic_Snake_Game
python main.py
```

The game window will open immediately. Click on the window if it doesn't respond to key presses right away.

---

## 🕹️ Controls

| Key | Action |
|---|---|
| ↑ Up Arrow | Move up |
| ↓ Down Arrow | Move down |
| ← Left Arrow | Move left |
| → Right Arrow | Move right |

> The snake cannot reverse direction — pressing the opposite key is ignored.

---

## ✨ Features

- **Persistent high score** — saved to `score.txt` and loaded every time you play
- **Wall & self-collision detection** — game resets smoothly without closing
- **Boundary box** — a clean white border visually defines the play area
- **Infinitely replayable** — the snake resets after each collision, letting you immediately try again

---

## 🧠 OOP Concepts Demonstrated

- **Inheritance** — `Food`, `ScoreBoard`, and `BorderBox` all extend `Turtle`, reusing its drawing capabilities
- **Encapsulation** — each game component owns its own state and behaviour
- **Abstraction** — `main.py` orchestrates the game at a high level without knowing how each class works internally
- **Composition** — the `Snake` class is composed of multiple `Turtle` segment objects
