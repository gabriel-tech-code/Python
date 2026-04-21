# Python Projects Collection

This repository contains a collection of Python-based projects focused on **fractals, algorithms, and games**.

Each project explores different concepts such as recursion, visualization, and performance analysis.

---
## Project Structure


```

Projects/

│
├── Fractals/
│   ├── LSystems/
│   │   ├── *.txt              # L-system rule files
│   │   └── lsystems.py       # Pygame-based renderer
│   │
│   ├── shapes_fractal.py
│   ├── shapes_spirals.py
│   ├── shapes.py
│   ├── sierpinski.py
│   └── tree_fractal.py
│
├── Sorting/                 
│   ├── AlphabetSort.py
│   └── NumberSort.py
│
└── Game/                     # (Planned)

```

---

## Fractals

A collection of scripts that generate mathematical and procedural fractals using Python.

### L-Systems


* Uses **text-based rule files** to generate fractals
* Rendered using `pygame`
* Features:
	* Animated drawing
	* Recursive branching
	* Color gradients (red → neon cyan)
	* Stack-based transformations
#### Example:

```bash

python lsystems.py plant.txt 800 600 400 580 80 0.7

```

---
### Other Fractal Scripts
 

* `shapes_fractal.py` → geometric fractal patterns
* `shapes_spirals.py` → spiral-based designs
* `shapes.py` → base shape rendering
* `sierpinski.py` → Sierpinski triangle implementation
* `tree_fractal.py` → recursive tree generation

These scripts explore recursion, symmetry, and geometric construction.

---
## Sorting (Planned)
  
Interactive sorting applications focused on **algorithm comparison and performance analysis**.

### Alphabet Sort (`AlphabetSort.py`)

A GUI-based tool for sorting words or letters.

### Features:

* User input (space-separated words/letters)
* Sort options:
  * A → Z
  * Z → A
* Displays sorted output
* Benchmarks multiple algorithms:
  * Lambda (Python built-in / Timsort)
  * Bubble Sort
  * Cocktail Shaker Sort
  * Heap Sort
  * Merge Sort
  * Quick Sort
  * Bucket Sort
* Execution time displayed in:
  * Seconds
  * Milliseconds
  * Microseconds
  * Nanoseconds

### Number Sort (`NumberSort.py`)

An extended version designed for **numerical data and deeper algorithm comparison**.

#### Features:
* Accepts:
  * Manual input (space-separated numbers)
  * File input (`.txt`, supports multi-line data)
* Sort options:
  * 0 → 9 (ascending)
  * 9 → 0 (descending)
* Displays sorted output
* Benchmarks multiple algorithms:
  * Lambda (Timsort)
  * Bubble Sort (while loop)
  * Bubble Sort (recursive)
  * Heap Sort
  * Merge Sort
  * Quick Sort
  * Cycle Sort
  * Counting Sort
  * Shell Sort

#### Notes:
* Counting Sort uses **O(n + k)** and depends on value range
* Quick Sort may degrade to **O(n²)** depending on pivot choice
* Recursive Bubble Sort is included for educational purposes
---
## Game (Planned)

## Snake Game  

A classic Snake game implemented in Python.
### Planned Features:

* Real-time movement
* Score tracking
* Increasing difficulty
* Simple UI using `pygame`

---
## Requirements

* Python 3.x
* `pygame` (for graphics-based projects)

Install pygame:

```bash
pip install pygame
```

---
## Goals of This Repository

* Practice **algorithm design**
* Explore **recursion and fractals**
* Build **interactive visualizations**
* Compare **performance of algorithms**
* Develop small **game projects**

---
