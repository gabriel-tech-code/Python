# Snake Game (Python + Pygame)

A modular, object‑oriented Snake game built with **Python** and **Pygame**, featuring:

- Multiple map support    
- Map selection menu    
- Main menu    
- Game over screen (with win condition)    
- Clean OOP architecture    
- Pre‑rendered map optimization    
- Fully scalable tile‑based system    

This project is designed for clarity, extensibility, and performance.
## Features
### Main Menu

Simple start screen with clean UI.
### Map Selection Menu

Automatically loads all `.txt` maps from the `maps/` folder.
### Game Over Screen

Displays **YOU WIN** or **GAME OVER** depending on the outcome.
### Win Condition

You win when the snake fills all but **5 playable tiles**.
### Modular Architecture

Each system is isolated:

```
core/
    game.py
    snake.py
    food.py
    map_loader.py
    enums.py
    settings.py

graphics/
    renderer.py
    menu.py

maps/
    donut.txt
    hshape.txt
    ...
```

### Pre‑Rendered Map

Walls are drawn once to a surface for improved performance.
## How It Works

### Game Loop Flow

```
Main Menu
   ↓
Map Selection Menu
   ↓
Game
   ↓
Game Over Menu (Restart or Quit)
```

### 🗺 Map Format

Maps are simple `.txt` files using:

- `1` = wall
- `0` = empty space
- `2` = snake start position

Example:

```
1111111111
1000000001
1000200001
1000000001
1111111111
```
## Getting Started

### 1. Install dependencies

```
pip install pygame
```

### 2. Run the game

```
python main.py
```

### 3. Add your own maps

Place `.txt` files inside the `maps/` folder. They will automatically appear in the map selection menu.

## Project Structure

```
Snake/
│
├── main.py
├── core/
│   ├── game.py
│   ├── snake.py
│   ├── food.py
│   ├── map_loader.py
│   ├── enums.py
│   └── settings.py
│
├── graphics/
│   ├── renderer.py
│   └── menu.py
│
├── maps/
│   ├── donut.txt
│   └── ...
│
└── README.md
```

## Win Condition

The snake wins when:
```
len(snake.body) >= playable_tiles - 5
```

Where `playable_tiles` = number of `0` and `2` tiles in the map.

## Known Good Python Versions

- Python **3.10+**    
- Pygame **2.6+**
    

## License

This project is open‑source. Feel free to modify, extend, or use it in your own projects.
