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

head1= turtle.Turtle()
head1.speed(0)
head1.shape("square")
head1.color("red")
head1.penup()
head1.goto(-250,0)
head1.direction="left"

food1= turtle.Turtle()
food1.speed(0)
food1.shape("circle")
food1.color("yellow")
food1.penup()
food1.goto(random.randint(-490,0),random.randint(-230,180))
food1.direction="stop"

head2= turtle.Turtle()
head2.speed(0)
head2.shape("square")
head2.color("red")
head2.penup()
head2.goto(250,0)
head2.direction="right"

food2= turtle.Turtle()
food2.speed(0)
food2.shape("circle")
food2.color("yellow")
food2.penup()
food2.goto(random.randint(0,490),random.randint(-230,180))
food2.direction="stop"

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
    y1=head1.ycor()
    x1=head1.xcor()
    y2=head2.ycor()
    x2=head2.xcor()
    if head1.direction=="up":
        head1.sety(y1+20)

    if head1.direction=="down":
        head1.sety(y1-20)

    if head1.direction=="left":
        head1.setx(x1-20)

    if head1.direction=="right":
        head1.setx(x1+20)

    if head2.direction=="up":
        head2.sety(y2+20)

    if head2.direction=="down":
        head2.sety(y2-20)

    if head2.direction=="left":
        head2.setx(x2-20)

    if head2.direction=="right":
        head2.setx(x2+20)

def go_up1(): #Movement controls
    if head1.direction !="down":
        head1.direction="up"
def go_down1():
    if head1.direction !="up":
        head1.direction="down"
def go_left1():
    if head1.direction !="right":
        head1.direction="left"
def go_right1():
    if head1.direction !="left":
        head1.direction="right"

def go_up2(): #Movement controls
    if head2.direction !="down":
        head2.direction="up"
def go_down2():
    if head2.direction !="up":
        head2.direction="down"
def go_left2():
    if head2.direction !="right":
        head2.direction="left"
def go_right2():
    if head2.direction !="left":
        head2.direction="right"
def exit_game():
    window.bye()

window.listen()
window.onkey(go_up1, "w")
window.onkey(go_down1, "s")
window.onkey(go_left1, "a")
window.onkey(go_right1, "d")
window.onkey(go_up2, "Up")
window.onkey(go_down2, "Down")
window.onkey(go_left2, "Left")
window.onkey(go_right2, "Right")
window.onkey(exit_game, "F1")

#Game loop
while True:
    window.update()   
    if head1.distance(food1)<20:
        food1.goto(random.randint(-490,0),random.randint(-230,180))
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
        bodyparts[0].goto(head1.xcor(),head1.ycor())
    
    if head1.xcor()>490 :
        head1.goto(-490,head1.ycor())
    if head1.xcor()<-490 :
        head1.goto(490,head1.ycor())
    if head1.ycor()>=200 :
        head1.goto(head1.xcor(),-240)
    if head1.ycor()<-240 :
        head1.goto(head1.xcor(),200)
    if head2.xcor()>490 :
        head2.goto(-490,head2.ycor())
    if head2.xcor()<-490 :
        head2.goto(490,head2.ycor())
    if head2.ycor()>=200 :
        head2.goto(head2.xcor(),-240)
    if head2.ycor()<-240 :
        head2.goto(head2.xcor(),200)
    
    move()

    for bodypart in bodyparts:
        if bodypart.distance(head1)<20:
            head1.goto(0,0)
            head1.direction="up"
            for bodypart in bodyparts:
                bodypart.goto(5000,5000)
            bodyparts=[]
            score=0
            score_display_p1.clear()
            score_display_p1.write("Score: {} High Score: {}     ".format(score,high_score), align="right",font=("Courier",20,"bold"))
            delay=0.20
    time.sleep(delay)

turtle.mainloop()