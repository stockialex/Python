from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake Game")

starting_position = [(0, 0), (-20, 0), (-40, 0)]

segments = []

screen.tracer(0)
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

    
game_alive = True

while game_alive:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.refresh()
        scoreboard.refresh()
    
        
        
    
screen.exitonclick()