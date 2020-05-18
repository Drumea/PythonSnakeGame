import time
import turtle
import random
import os

filepath=os.path.dirname((__file__))
txtpath= filepath+"\\SinglePlayerHighScores.txt"

def order_file():
    scores=[]
    names=[]
    with open(txtpath) as scoreboard:
        lines = scoreboard.readlines()
    for i in range(len(lines)):
        if i%2==0:
            scores.append(int(lines[i].strip("\n")))
        else:
            names.append(lines[i].strip("\n"))
    temp2=0
    temp=0 
    for i in range(0, len(scores)):
        for j in range(i+1, len(scores)):    
            if(scores[i] < scores[j]):
                temp2 =names[i]
                names[i]=names[j]
                names[j]=temp2
                temp = scores[i]
                scores[i] = scores[j]   
                scores[j] = temp     
    with open(txtpath,'w') as scoreboard:
        for i in range(0,len(scores)):
            scoreboard.write(str(scores[i])+"\n"+names[i]+"\n")

def game():
    delay=0.20
    score=0
    if os.path.exists(txtpath):
        order_file()
    else:
        scoreboard=open(txtpath,'w')

    scoreboard=open(txtpath,'r')
    high_score=scoreboard.readline()
    if not high_score:
        high_score=0
    else:
        high_score=int(high_score.strip('\n'))

    game_window= turtle.Screen()
    game_window.title("Drumea's Snake Game Attepmt - Singleplayer")
    game_window.tracer(0)
    game_window.bgcolor("black")
    game_window.setup(width=500, height= 500)

    head= turtle.Turtle()
    head.speed(0)
    head.shape("square")
    head.color("red")
    head.penup()
    head.direction="right"
    head.goto(0,0)

    food= turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("yellow")
    food.penup()
    food.direction="stop"
    food.goto(random.randint(-230,230),random.randint(-230,180))

    bodyparts=[]

    display=turtle.Turtle()
    display.speed(0)
    display.shape("circle")
    display.color("white")
    display.penup()
    display.hideturtle()
    display.goto(0,210)
    display.write("Score: 0 High Score: {}".format(high_score), align="center",font=("Courier",20,"bold"))
    
    def move():
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
            
    def go_up():
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
        game_window.bye()
    def new_game():
        game_window.clear()
        game()

    game_window.listen()
    game_window.onkey(go_up, "Up")
    game_window.onkey(go_down, "Down")
    game_window.onkey(go_left, "Left")
    game_window.onkey(go_right, "Right")
    game_window.onkey(exit_game, "F1")

    def game_over_screen():    
        game_window.clear()
        game_window.setup(width=700, height= 370)
        game_window.bgcolor("black")          
        display.goto(0,20)
        display.write(" Game Over \n Please enter your name into the console", align="center",font=("Courier",20,"bold"))
        name=input('Please enter your name: ')
        scoreboard = open(txtpath,"a")
        scoreboard.write(name+"\n")
        scoreboard.close()
        display.clear()
        display.write(" Thank you, {} \n If you wish to view the leaderbord \n press 'L' \n If you wish to play again press 'Space'".format(name), align="center",font=("Courier",20,"bold"))
        game_window.listen()
        game_window.onkey(new_game, "space")
        game_window.onkey(leaderboad,"l")
        game_window.onkey(exit_game, "F1")
    
    def leaderboad(): 
        game_window.clear()
        game_window.setup(width=600, height= 700)
        game_window.bgcolor("black")  
        game_window.listen()
        game_window.onkey(new_game, "space")
        game_window.onkey(exit_game, "F1")
        display.goto(0,320)
        display.write(" LeaderBoad", align="center",font=("Courier",20,"bold"))
        y=300
        j=1
        order_file()
        with open(txtpath) as scoreboard:
            lines = scoreboard.readlines()
        for i in range(0,len(lines),2):
            y=y-100
            display.goto(-100,y)
            display.write("{}.User: {} Score: {}".format(j,lines[i+1].strip('\n'),lines[i].strip('\n')), align="center",font=("Courier",20,"bold"))
            if j==5:
                break
            j=j+1
        
    while True:
        game_window.update()   
        if head.distance(food)<20:
            food.goto(random.randint(-230,230),random.randint(-230,180))
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
            display.clear()
            display.write("Score: {} High Score: {}".format(score,high_score), align="center",font=("Courier",20,"bold"))

        for i in range(len(bodyparts)-1,0,-1):
            bodyparts[i].goto(bodyparts[i-1].xcor(),bodyparts[i-1].ycor())       
        
        if len(bodyparts)>0:
            bodyparts[0].goto(head.xcor(),head.ycor())       
        if head.xcor()>240 :
            head.goto(-240,head.ycor())
        if head.xcor()<-240 :
            head.goto(240,head.ycor())
        if head.ycor()>=200 :
            head.goto(head.xcor(),-240)
        if head.ycor()<-240 :
            head.goto(head.xcor(),200)

        move()
        
        for bodypart in bodyparts:
            if bodypart.distance(head)<20:
                scoreboard = open(txtpath,"a")
                scoreboard.write(str(score)+"\n")
                scoreboard.close()
                bodyparts=[]
                game_over_screen()
                
        time.sleep(delay)
game()