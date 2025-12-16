# Turn-Based Battle Game (Python)

A simple **turn-based battle game** developed in Python and played directly in the terminal. This project was created for learning purposes, focusing on **object-oriented programming**, **user input validation**, and **basic game logic**.

---

## 🎮 Game Overview

* You play as a **Warrior**
* You choose a **difficulty level** (Easy, Medium, Hard)
* Each difficulty spawns an enemy with different stats
* The game runs in **turns** until one character's life points reach zero

---

## ⚔️ Gameplay Mechanics

### Player Actions

On your turn, you can choose one of the following actions:

1. **Attack** – Deal damage to the enemy
2. **Defend** – Reduce incoming damage
3. **Special Ability** – Perform a stronger or unique attack

### Enemy Actions

* The enemy chooses actions automatically
* Enemy behavior is probabilistic:

  * **70% chance** to attack
  * **30% chance** to defend

---

## 🧱 Project Structure

```
polimorfic_adventure/
│
├── main.py # Game loop and user interaction
├── entity.py # Base Entity class (shared behavior)
├── character.py # Player character class (inherits from Entity)
├── enemy.py # Enemy class and AI behavior (inherits from Entity)
└── README.md # Project documentation
```

---

## 🧠 Concepts Practiced

* Object-Oriented Programming (OOP)
* Classes and inheritance
* Input validation with loops and exceptions
* Randomized behavior using `random.choices`
* Terminal screen control
* Turn-based game logic

---

## ▶️ How to Run

1. Make sure you have **Python 3.x** installed
2. Open a terminal in the project directory
3. Run the game:

```bash
python main.py
```

> ⚠️ The game is designed to run in a **terminal**, not in an IDE output panel.

---

## 📌 Future Improvements (Ideas)

* Add more character classes
* Implement items or inventory
* Improve enemy AI
* Add animations or delays for better immersion
* Refactor menus into reusable functions

---

## 📚 Purpose

This project is intended as a **learning exercise** to practice Python fundamentals and game logic in a clean and structured way.

---

## ✅ Author

Developed by **João Henrique** 🚀

Feel free to modify, extend, or refactor the project as you learn more!
