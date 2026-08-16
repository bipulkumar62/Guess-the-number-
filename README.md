# 🎯 Number Guessing Game (Python)

A lightweight, interactive command-line application where players attempt to guess a randomly generated target number between 1 and 100. Built entirely using standard Python modules.

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen.svg)

---

## 📌 Features

* **Real-Time Feedback:** Instantly guides the player with `"Lower"` or `"Higher"` prompts after each turn.
* **Attempt Tracking:** Keeps track of total guesses taken to complete the game.
* **Zero External Dependencies:** Uses only Python's built-in `random` module.

---

## 🕹️ How It Works

1. The game selects a hidden integer strictly between **1 and 100**.
2. The player inputs a numeric guess.
3. If the guess is:
   * **Too high:** The program requests a lower number.
   * **Too low:** The program requests a higher number.
4. Once guessed correctly, the total attempt count is displayed, and the program exits.

---

## 🚀 Getting Started

### Prerequisites

* [Python 3.x](https://www.python.org/downloads/) installed on your system.

### Installation & Execution

1. Clone this repository or copy the `guess_the_number.py` file to your target directory.
2. Open your terminal or command prompt in that directory.
3. Run the script:

```bash
python guess_the_number.py
