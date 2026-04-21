# L-System Fractals (Python + Pygame)

A Python project that generates and animates L-System fractals using pygame.

Supports multiple fractal definitions via text files, animated drawing, recursive branch scaling, and a smooth red → neon cyan color gradient.

## Features

Supports multiple L-system types (tree, plant, dragon, sierpinski, triangle)

- Animated drawing (step-by-step rendering)
- Recursive branch scaling using ratio
- Color gradient from red → neon cyan
- Optional glow effect for neon-style visuals
- Easily configurable via .txt files

## Requirements
- Python 3.x
- pygame

Install pygame with: `pip install pygame`


## How to Run

```
python lsystems.py <file> <width> <height> <start_x> <start_y> <length> <ratio>
```

Example:
```
> python lsystems.py plant.txt 800 600 400 580 80 0.7
```

## L-System File Format

Each .txt file must follow this structure:
- Axiom
- Iterations
- Rule1
- Rule2 
- ...
- Angle

### Example: plant.txt
```
-X
7
X F+[[X]-X]-F[-FX]+X
F FF
15
```

### Example: triangle.txt

```
F+F+F
1
F F-F+F
120
```
### Example: dragon.txt

```
FX
2
X X+YF+
Y -FX-Y
90
```
### Example: sierpinski.txt

```
F-G-G
2
F F-G+F+G-F
G GG
120
```

## Controls & Behavior

Drawing is animated over time
Color transitions from:
- Red (start)
- Mid tones
- Cyan (end)
### Tips for Best Results

Use 4–6 iterations for complex fractals
Try these settings for plants:
- `python lsystems.py plant.txt 800 600 400 580 80 0.7`
- Lower ratio → sharper tapering (tree-like)
- Higher ratio → bushier structures
- Optional Enhancements
You can extend this project with:
- Glow / neon effects
- Keyboard controls (change fractals live)
- Restart animation
- Random angle variation (more natural look)
### How It Works

- Parse L-system rules from a text file
- Generate the instruction string via recursion
- Interpret symbols:
```
F, G → draw forward
+, - → rotate
[ ] → save/restore state (branching)
```
- Animate drawing using incremental steps
- Apply color gradient based on progress
### Example Output

Produces animated fractal plants and structures like:
- Organic plant growth
- Tree branching systems
- Dragon curves
- Geometric fractals