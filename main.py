from turtle import Screen,Turtle
from snake import Snake
from food import Food

import time
score = 0
tim = Turtle()
tim.color('white')
tim.penup()
tim.goto(0,270)
tim.write(f"Score: {score}", align='center')
tim.hideturtle()


screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height= 600)
screen.tracer(0)

# Creating the snake
snake = Snake()

# Creating Food
food = Food()

# Key events
screen.listen()
screen.onkey(snake.Up, key='Up')
screen.onkey(snake.Down, key='Down')
screen.onkey(snake.Left, key='Left')
screen.onkey(snake.Right, key='Right')

# Moving the snake
is_game_on = True
while is_game_on:
    screen.update() # updating the screen after all the moved forward.
    time.sleep(0.1) # using sleep function to control the speed of snake by stopping the screen.  
    snake.move()  
    
    #checking collision with walls
    if snake.head.xcor() >= 295 or snake.head.xcor() <= -295 or snake.head.ycor() >= 295 or snake.head.ycor() <= -295:
        break

    # Detecting the collisions with food and increasing the score
    if snake.head.distance(food)<15:
        score += 1
        tim.clear()
        tim.write(f"Score: {score}", align='center')
        snake.extend()
        food.generate_food() 

    for segment in snake.body[1:]:
            if snake.head.distance(segment) < 10:
                is_game_on = False

screen.exitonclick()