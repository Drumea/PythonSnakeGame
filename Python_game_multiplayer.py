import time
import turtle
import random

score=0
high_score=0
delay=0.20

window= turtle.Screen() #Game Window
window.title("Drumea's Snake Game Attepmt - Multiplayer")
window.bgcolor("black")
window.setup(width=1000, height= 500)
window.tracer(0)

head= turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(-250,0)
head.direction="left"

food= turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(random.randint(-490,0),random.randint(-230,180))
food.direction="stop"

bodyparts=[]

score_display_p1=turtle.Turtle()
score_display_p1.speed(0)
score_display_p1.shape("circle")
score_display_p1.color("red")
score_display_p1.penup()
score_display_p1.hideturtle()
score_display_p1.goto(0,210)
score_display_p1.write("Score: 0 High Score: 0     ", align="right",font=("Courier",20,"bold"))

score_display_p2=turtle.Turtle()
score_display_p2.speed(0)
score_display_p2.shape("circle")
score_display_p2.color("green")
score_display_p2.penup()
score_display_p2.hideturtle()
score_display_p2.goto(0,210)
score_display_p2.write("     Score: 0 High Score: 0", align="left",font=("Courier",20,"bold"))

def move(): #Movement Directions
    y=head.ycor()
    x=head.xcor()
    if head.direction=="up":
        head.sety(y+20)

    if head.direction=="down":
        head.sety(y-20)

    if head.direction=="left":
        head.setx(x-20)

    if head.direction=="right":
        head.setx(x+20)
    
def go_up(): #Movement controls
    if head.direction !="down":
        head.direction="up"
def go_down():
    if head.direction !="up":
        head.direction="down"
def go_left():
    if head.direction !="right":
        head.direction="left"
def go_right():
    if head.direction !="left":
        head.direction="right"
def exit_game():
    turtle.bye()

window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down, "Down")
window.onkey(go_left, "Left")
window.onkey(go_right, "Right")
window.onkey(exit_game, "e")

#Game loop
while True:
    window.update()   
    if head.distance(food)<20:
        food.goto(random.randint(-490,0),random.randint(-230,180))
        new_bodypart=turtle.Turtle()
        new_bodypart.speed(0)
        new_bodypart.shape("square")
        new_bodypart.color("red")
        new_bodypart.penup()
        bodyparts.append(new_bodypart)

        score=score+5
        delay=delay-0.005
        if score>high_score:
            high_score=score
        score_display_p1.clear()
        score_display_p1.write("Score: {} High Score: {}     ".format(score,high_score), align="right",font=("Courier",20,"bold"))


    for i in range(len(bodyparts)-1,0,-1):
        bodyparts[i].goto(bodyparts[i-1].xcor(),bodyparts[i-1].ycor())       
    
    if len(bodyparts)>0:
        bodyparts[0].goto(head.xcor(),head.ycor())
    
    if head.xcor()>490 :
        head.goto(-490,head.ycor())
    if head.xcor()<-490 :
        head.goto(490,head.ycor())
    if head.ycor()>=200 :
        head.goto(head.xcor(),-240)
    if head.ycor()<-240 :
        head.goto(head.xcor(),200)
    
    move()

    for bodypart in bodyparts:
        if bodypart.distance(head)<20:
            head.goto(0,0)
            head.direction="up"
            for bodypart in bodyparts:
                bodypart.goto(5000,5000)
            bodyparts=[]
            score=0
            score_display_p1.clear()
            score_display_p1.write("Score: {} High Score: {}     ".format(score,high_score), align="right",font=("Courier",20,"bold"))
            delay=0.20
    time.sleep(delay)

turtle.mainloop()