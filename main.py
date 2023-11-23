import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
is_race_on = False
screen.setup(width=500, height=400)
colors = ["red", "blue", "green", "orange", "purple", "violet"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-220, y=y_positions[i])
    turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"{winning_color} is the winner, you won the bet!")
            else:
                print(f"{winning_color} is the winner, you lost the bet!")
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)
screen.exitonclick()
