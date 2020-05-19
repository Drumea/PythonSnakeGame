import time
import turtle
import random
import os
import shutil

gamepath=os.path.dirname((__file__))

window= turtle.Screen() 
window.title("Drumea's Snake Game Attepmt - Two Players")

display=turtle.Turtle()
display.speed(0)
display.shape("circle")
display.color("white")
display.penup()
display.hideturtle()
generated=False

def exit_game():
    window.bye()

def generate_extra(num,dir):
    for i in range(0,num):
        f=open (dir+"/ExtraFile"+str(i)+".txt","w+")
    
def generate1():
    global player1dir, player2dir, generated
    generated=True
    player1dir=gamepath+"/Player1Folder"
    os.mkdir(player1dir)
    player2dir=gamepath+"//Player2Folder"
    os.mkdir(player2dir)
    for i in range(0,20):
        f1=open (player1dir+"/RandomName"+str(i)+".txt","w+")
        f1.close()
        f2=open (player2dir+"/RandomName"+str(i)+".txt","w+")
        f2.close()
    game()

def intro():    
    window.clear()
    window.setup(width=700, height= 350)
    window.bgcolor("black")          
    display.goto(0,20)
    display.write(" Welcome to my Snake Game \n Would you like to use existing folders? \n (y/n)", align="center",font=("Courier",20,"bold"))
    
    def give_paths():
        global player1dir, player2dir
        display.clear()
        display.write("Please enter the paths of the two \n folders in the console", align="center",font=("Courier",20,"bold"))
        player1dir=input("Player 1 (red) folder path: " )
        lista1 = os.listdir(player1dir)
        if(len(lista1)<20):
            generate_extra(20-len(lista1),player1dir)
        player2dir=input("Player 2 (green) folder path: " )
        lista2 = os.listdir(player1dir)
        if(len(lista2)<20):
            generate_extra(20-len(lista2),player1dir)
        game()
    window.listen()
    window.onkey(give_paths,"y")
    window.onkey(generate1,"n")
    window.onkey(exit_game,"F1")     
    window.mainloop()

def game():
    display.clear()
    score1=0
    score2=0
    hp1=20
    hp2=20
    delay=0.15
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
    food1.color("orange")
    food1.penup()
    food1.goto(random.randint(-490,0),random.randint(-230,180))
    food1.direction="stop"

    head2= turtle.Turtle()
    head2.speed(0)
    head2.shape("square")
    head2.color("green")
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

    bodyparts2=[]
    bodyparts1=[]

    super_food= turtle.Turtle()
    super_food.speed(0)
    super_food.shape("circle")
    super_food.color("blue")
    super_food.penup()
    super_food.goto(random.randint(-490,490),random.randint(-230,180))
    super_food.direction="stop"

    score_display_p1=turtle.Turtle()
    score_display_p1.speed(0)
    score_display_p1.shape("circle")
    score_display_p1.color("red")
    score_display_p1.penup()
    score_display_p1.hideturtle()
    score_display_p1.goto(0,210)
    score_display_p1.write("Score: 0 Health points: 20    ", align="right",font=("Courier",20,"bold"))

    score_display_p2=turtle.Turtle()
    score_display_p2.speed(0)
    score_display_p2.shape("circle")
    score_display_p2.color("green")
    score_display_p2.penup()
    score_display_p2.hideturtle()
    score_display_p2.goto(0,210)
    score_display_p2.write("    Score: 0 Health points: 20", align="left",font=("Courier",20,"bold"))

    def move(): 
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

    def go_up1():
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

    def go_up2():
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

    def add_bodyparts1():
        new_bodypart=turtle.Turtle()
        new_bodypart.speed(0)
        new_bodypart.shape("square")
        new_bodypart.color("red")
        new_bodypart.penup()
        new_bodypart.goto(5000,5000)
        bodyparts1.append(new_bodypart)

    def add_bodyparts2():
        new_bodypart=turtle.Turtle()
        new_bodypart.speed(0)
        new_bodypart.shape("square")
        new_bodypart.color("green")
        new_bodypart.penup()
        new_bodypart.goto(5000,5000)
        bodyparts2.append(new_bodypart)

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

    while True:
        window.update()   
        if head1.distance(food1)<20:
            food1.goto(random.randint(-490,0),random.randint(-230,180))
            add_bodyparts1()
            score1=score1+5
            score_display_p1.clear()
            score_display_p1.write("Score: {} Health Points: {}   ".format(score1,hp1), align="right",font=("Courier",20,"bold"))
        
        if head2.distance(food2)<20:
            food2.goto(random.randint(0,490),random.randint(-230,180))
            add_bodyparts2()
            score2=score2+5
            score_display_p2.clear()
            score_display_p2.write("   Score: {} Health Points: {}     ".format(score2,hp2), align="left",font=("Courier",20,"bold"))

        if head1.distance(super_food)<20:
            super_food.goto(random.randint(-490,490),random.randint(-230,180))
            x=2
            while x!=0:
                add_bodyparts1()
                x=x-1
            score1=score1+10
            score_display_p1.clear()
            score_display_p1.write("Score: {} Health Points: {}   ".format(score1,hp1), align="right",font=("Courier",20,"bold"))
        
        if head2.distance(super_food)<20:
            super_food.goto(random.randint(-490,490),random.randint(-230,180))
            x=2
            while x!=0:
                add_bodyparts2()
                x=x-1
            score2=score2+10
            score_display_p2.clear()
            score_display_p2.write("   Score: {} Health Points: {}     ".format(score2,hp2), align="left",font=("Courier",20,"bold"))

        for i in range(len(bodyparts1)-1,0,-1):
            bodyparts1[i].goto(bodyparts1[i-1].xcor(),bodyparts1[i-1].ycor())       
        
        if len(bodyparts1)>0:
            bodyparts1[0].goto(head1.xcor(),head1.ycor())
        
        for i in range(len(bodyparts2)-1,0,-1):
            bodyparts2[i].goto(bodyparts2[i-1].xcor(),bodyparts2[i-1].ycor())       
        
        if len(bodyparts2)>0:
            bodyparts2[0].goto(head2.xcor(),head2.ycor())

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

        def game_over_1():
            if generated==True:
                shutil.rmtree(player1dir, ignore_errors=True)
                shutil.rmtree(player2dir, ignore_errors=True)
            window.clear()
            window.setup(width=700, height= 350)
            window.bgcolor("black")          
            display.goto(0,20)
            display.write(" Player 1 has lost \n press space to restart the game", align="center",font=("Courier",20,"bold"))
            window.listen()
            window.onkey(exit_game,"F1") 
            window.onkey(intro,"space")
        
        def game_over_2():
            if generated==True:
                shutil.rmtree(player1dir, ignore_errors=True)
                shutil.rmtree(player2dir, ignore_errors=True)
            window.clear()
            window.setup(width=700, height= 350)
            window.bgcolor("black")          
            display.goto(0,20)
            display.write(" Player 2 has lost \n Press space to restart the game", align="center",font=("Courier",20,"bold"))
            window.listen()
            window.onkey(exit_game,"F1") 
            window.onkey(intro,"space") 

        def snake1_death():
            lista = os.listdir(player1dir)
            x=random.choice(lista)
            os.remove(player1dir+"/"+x)
            head1.goto(-250,0)
            head1.direction="left"
            score1=0
            score_display_p1.clear()
            score_display_p1.write("Score: {} Health Points: {}   ".format(score1,hp1), align="right",font=("Courier",20,"bold"))
        
        def snake2_death():
            lista = os.listdir(player2dir)
            x=random.choice(lista)
            os.remove(player1dir+"/"+x)
            head2.goto(250,0)
            head2.direction="right"
            score2=0
            score_display_p2.clear()
            score_display_p2.write("   Score: {} Health Points: {}     ".format(score2,hp2), align="left",font=("Courier",20,"bold"))

        for bodypart in bodyparts1:
            if bodypart.distance(head1)<20:
                hp1=hp1-1
                snake1_death()
                if hp1==0:
                    game_over_1()
                for bodypart in bodyparts1:
                    bodypart.goto(5000,5000)
                bodyparts1=[]
    
        for bodypart in bodyparts2:
            if bodypart.distance(head2)<20:
                hp2=hp2-1
                snake1_death()
                if hp2==0:
                    game_over_2()
                snake2_death()
                for bodypart in bodyparts2:
                    bodypart.goto(5000,5000)
                bodyparts2=[]

        for bodypart in bodyparts1:
            if bodypart.distance(head2)<20 or head1.distance(head2)<20:
                if len(bodyparts1)>len(bodyparts2):
                    hp2=hp2-1
                    snake2_death()
                    if hp2==0:
                        game_over_2()                   
                    for bodypart in bodyparts2:
                        bodypart.goto(5000,5000)
                    bodyparts2=[]
                else:
                    hp1=hp1-1
                    snake1_death()
                    if hp1==0:
                        game_over_1() 
                    for bodypart in bodyparts1:
                        bodypart.goto(5000,5000)
                    bodyparts1=[]
        
        for bodypart in bodyparts2:
            if bodypart.distance(head1)<20 or head2.distance(head1)<20:
                if len(bodyparts1)>len(bodyparts2):
                    hp2=hp2-1
                    snake2_death()
                    if hp2==0:
                        game_over_2() 
                    for bodypart in bodyparts2:
                        bodypart.goto(5000,5000)
                    bodyparts2=[]
                else:
                    hp1=hp1-1
                    snake1_death()
                    if hp1==0:
                        game_over_2() 
                    for bodypart in bodyparts1:
                        bodypart.goto(5000,5000)
                    bodyparts1=[]  
        
        time.sleep(delay)
    window.mainloop()
intro()