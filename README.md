# Snake Game

This is a simple Snake Game built using Python and Tkinter.

# How to Play
- Control the snake using the arrow keys:
  - **Up**: Move Up
  - **Down**: Move Down
  - **Left**: Move Left
  - **Right**: Move Right
- The goal is to eat the red food, which makes the snake grow longer.
- Avoid colliding with the walls or the snake's own body.
- The game ends when a collision occurs.

# Features
- Dynamic snake movement.
- Randomly placed food items.
- Collision detection for walls and the snake's body.
- Game Over screen displayed when the game ends.

# Requirements
- Python 3.x
- Tkinter (built-in with Python on most systems)

# How to Run
1. Save the code in a file named `snake_game.py`.
2. Run the game using the command:
   ```bash
   python snake_game.py
   ```
3. Enjoy playing the game!

# Code Overview

### Key Components
1. **Game Settings**:
   - `WINDOW_SIZE`: Size of the game window (default: 500x500).
   - `SEGMENT_SIZE`: Size of each segment of the snake (default: 20).
   - `SPEED`: Game speed in milliseconds (default: 100).

2. **Classes and Methods**:
   - `SnakeGame`: The main class that handles game logic.
     - `__init__`: Initializes the game window, snake, and food.
     - `draw_snake`: Draws the snake on the canvas.
     - `draw_food`: Draws the food on the canvas.
     - `place_food`: Randomly places food on the canvas.
     - `change_direction`: Changes the snake's direction based on user input.
     - `move_snake`: Moves the snake in the current direction.
     - `grow_snake`: Adds a segment to the snake when food is eaten.
     - `check_collisions`: Checks for collisions with walls or the snake's own body.
     - `run_game`: Main game loop that updates the game state.

# Collision Logic
- **Wall Collision**: Ends the game if the snake's head moves outside the window boundaries.
- **Self Collision**: Ends the game if the snake's head collides with any part of its body.

# Food Logic
- When the snake's head overlaps the food's position, the snake grows longer and new food is randomly placed.

## Future Improvements
- Add score tracking.
- Implement levels with increasing difficulty.
- Add a pause and resume feature.
- Include sound effects and enhanced graphics.

Enjoy coding and playing! 🎮
