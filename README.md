# Short Sticks Game 🥢

A simple and interactive command-line game written in Python that simulates the classic "draw the short straw" game. This project was developed to practice list manipulation, input validation, and modular logic in Python.

---

## Features

* **Dynamic Shuffling:** Uses Python's built-in `random` module to shuffle the stick lengths every time the game resets.
* **Input Validation:** Includes a robust `while` loop to guarantee the user only inputs valid choices between 1 and 4.
* **Index Mapping:** Handles data type transitions by converting the user's string choice into an integer, automatically adjusting it (`attempt - 1`) to match Python's zero-indexed list structure.
* **Clean Architecture:** Features a modular code structure, dividing the mix, input, and check-try logic into independent, clean functions.

---

## How to use

1. Clone this repository: 
   `git clone https://github.com/jerocubaque12/Sticks-game.git`
2. Run the script: 
   `sticks_game.py`
3. Follow the on-screen instructions to pick your number and test your luck.

---

## Requirements

* Python 3.6+
* `random` module (built-in)

---

## Author

* Jeronimo Cubaque - https://github.com/jerocubaque12
