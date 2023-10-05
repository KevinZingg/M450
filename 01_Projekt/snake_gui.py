import turtle
import time
from snake_game import SnakeGame

# Initialize game instance
game = SnakeGame()

# Setup the screen
wn = turtle.Screen()
wn.title('Snake Game')
wn.bgcolor('white')
wn.setup(width=1000, height=700)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Score display
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('black')
pen.penup()
pen.hideturtle()
pen.goto(0, 310)
pen.write('Score: 0  High Score: 0', align='center', font=('Courier', 24, 'normal'))

# Key bindings
wn.listen()
wn.onkeypress(lambda: setattr(game, 'direction', 'up'), 'w')
wn.onkeypress(lambda: setattr(game, 'direction', 'down'), 's')
wn.onkeypress(lambda: setattr(game, 'direction', 'left'), 'a')
wn.onkeypress(lambda: setattr(game, 'direction', 'right'), 'd')

# Main game loop
while True:
    game.move()

    # Check for wall collision
    if game.check_wall_collision():
        game.reset_game()

    # Check for self collision
    if game.check_self_collision():
        game.reset_game()

    # Check for food collision
    if game.check_food_collision():
        game.update_food_position()
        game.update_score()
        food.goto(game.food_position[0], game.food_position[1])
        # Add a segment (this can be refined to actually display on screen)
        game.segments.append(game.head_position.copy())

    # Move the snake head
    head.goto(game.head_position[0], game.head_position[1])

    # Update the score display
    pen.clear()
    pen.write('Score: {} High Score: {}'.format(game.score, game.high_score), align='center',
              font=('Courier', 24, 'normal'))

    # Control the game speed
    time.sleep(game.delay)
    wn.update()

# Keep the window open
wn.mainloop()
