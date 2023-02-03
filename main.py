import turtle
import random

screen = turtle.Screen()
screen.setup(width=500,height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions =[-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,len(colors)):
    
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_positions[turtle_index])

    all_turtles.append(new_turtle)

    
race_going = False
user_bet = screen.textinput(title = "Make your bet", prompt = "Who will win the race, pick any color of the rainbow.")

if user_bet:
    race_going = True

while race_going:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_going = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won!  {winning_color.title()} is the winner!")
            else:
                print(f"You've lost.  {winning_color.title()} was the winner!")
                
        
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        
        







screen.exitonclick()

