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

├── Sorting/                  # (Planned)

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
  
A number sorting program with performance comparison.
### Features (planned):
* Accepts:
	* User input
	* File input (space-separated numbers)
* Outputs:
	* Sorted numbers (ascending or descending)
* Includes multiple algorithms:
	* Bubble Sort
	* Selection Sort
	* Insertion Sort
	* (More to be added)
* Displays execution time in **nanoseconds**

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
## ⚙️ Requirements

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
## Future Improvements

* Add GUI controls for fractal parameters
* Expand sorting algorithms (merge, quicksort, etc.)
* Add benchmarking visualizations
* Enhance game mechanics and UI
