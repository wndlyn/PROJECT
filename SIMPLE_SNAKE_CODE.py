import tkinter as tk
import random

# Game settings
WINDOW_SIZE = 500
SEGMENT_SIZE = 20
SPEED = 100

class SnakeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Snake Game")
        self.canvas = tk.Canvas(self.window, width=WINDOW_SIZE, height=WINDOW_SIZE, bg="black")
        self.canvas.pack()

        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self.place_food()
        self.direction = "Right"
        self.running = True

        self.draw_snake()
        self.draw_food()

        self.window.bind("<Up>", lambda e: self.change_direction("Up"))
        self.window.bind("<Down>", lambda e: self.change_direction("Down"))
        self.window.bind("<Left>", lambda e: self.change_direction("Left"))
        self.window.bind("<Right>", lambda e: self.change_direction("Right"))

        self.run_game()
        self.window.mainloop()

    def draw_snake(self):
        self.canvas.delete("snake")
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(x, y, x + SEGMENT_SIZE, y + SEGMENT_SIZE, fill="green", tag="snake")

    def draw_food(self):
        self.canvas.delete("food")
        x, y = self.food
        self.canvas.create_oval(x, y, x + SEGMENT_SIZE, y + SEGMENT_SIZE, fill="red", tag="food")

    def place_food(self):
        x = random.randint(0, (WINDOW_SIZE // SEGMENT_SIZE) - 1) * SEGMENT_SIZE
        y = random.randint(0, (WINDOW_SIZE // SEGMENT_SIZE) - 1) * SEGMENT_SIZE
        return (x, y)

    def change_direction(self, new_direction):
        opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if new_direction != opposites.get(self.direction, ""):
            self.direction = new_direction

    def move_snake(self):
        x, y = self.snake[0]
        if self.direction == "Up":
            y -= SEGMENT_SIZE
        elif self.direction == "Down":
            y += SEGMENT_SIZE
        elif self.direction == "Left":
            x -= SEGMENT_SIZE
        elif self.direction == "Right":
            x += SEGMENT_SIZE

        new_head = (x, y)
        self.snake = [new_head] + self.snake[:-1]

    def grow_snake(self):
        self.snake.append(self.snake[-1])

    def check_collisions(self):
        x, y = self.snake[0]

        # Check for wall collisions
        if x < 0 or y < 0 or x >= WINDOW_SIZE or y >= WINDOW_SIZE:
            return True

        # Check for self collisions
        if (x, y) in self.snake[1:]:
            return True

        return False

    def run_game(self):
        if not self.running:
            return

        self.move_snake()

        # Check for collisions
        if self.check_collisions():
            self.running = False
            self.canvas.create_text(WINDOW_SIZE // 2, WINDOW_SIZE // 2, fill="white", font="Arial 20 bold", text="Game Over!")
            return

        # Check for food collision
        if self.snake[0] == self.food:
            self.food = self.place_food()
            self.grow_snake()
            self.draw_food()

        self.draw_snake()
        self.window.after(SPEED, self.run_game)

# Run the game
if __name__ == "__main__":
    SnakeGame()
