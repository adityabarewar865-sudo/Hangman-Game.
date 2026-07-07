# 🎯 Hangman Game
🎯 A beginner-friendly Python implementation of the classic Hangman game where players guess letters to uncover a hidden word before running out of lives.

```text
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/
```
---

## ✨ Features

- Randomly selects a word from a predefined word list.
- Allows the player to guess one letter at a time.
- Tracks correct and incorrect guesses.
- Displays the current progress after each guess.
- Uses ASCII art to show the remaining lives.
- Ends the game when the player wins or runs out of lives.
- Uses separate modules for game logic, ASCII art, and the word list.
- Beginner-friendly project demonstrating Python lists, loops, functions, modules, and conditional statements.

---

## 📂 Project Structure

```text
Hangman-Game/
├── main.py
├── hangman_words.py
├── hangman_art.py
└── README.md
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🎨 Hangman Stages

```text
+---+
|   |
O   |
/|\  |
/ \  |
    |
=========
```

```text
+---+
|   |
O   |
/|\  |
/    |
    |
=========
```

```text
+---+
|   |
O   |
/|\  |
    |
    |
=========
```

```text
+---+
|   |
O   |
/|   |
    |
    |
=========
```

```text
+---+
|   |
O   |
|   |
    |
    |
=========
```

```text
+---+
|   |
O   |
    |
    |
    |
=========
```

```text
+---+
|   |
    |
    |
    |
    |
=========
```

---

## 🖥️ Example Gameplay

```text
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/

Welcome to Hangman!

Word to guess:
_ _ _ _ _

Guess a letter:
a

Correct!

Word:
_ a _ _ _

Lives Remaining:

+---+
|   |
O   |
/|\  |
/ \  |
    |
=========

Guess another letter:
e

Wrong!

Lives Remaining:

+---+
|   |
O   |
/|\  |
/    |
    |
=========

...
```

---

## 🛠️ Technologies Used

- Python 3
- Random Module
- Lists
- Loops
- Functions
- Conditional Statements
- Modules
- ASCII Art
