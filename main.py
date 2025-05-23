import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("lightblue1")

t = turtle.Turtle()
t.speed(0)


t.penup()
t.goto(-5000,-100)
t.pendown()
t.fillcolor("green")
t.pencolor("green")
t.begin_fill()
t.goto(5000,-100)
t.goto(5000,-5000)
t.goto(-5000,-5000)
t.goto(-5000,-100)
t.end_fill()








t.penup()
t.goto(100,0)
t.pendown()
#circle - radius
t.pencolor('pink')
t.fillcolor('pink')
t.begin_fill()
t.circle(25)
t.setheading(90)
t.circle(25)
t.setheading(180)
t.circle(25)
t.setheading(270)
t.circle(25)
t.end_fill()
t.penup()
t.goto(100, -15)
t.pendown()
t.setheading(0)
t.fillcolor('yellow')
t.begin_fill()
t.circle(15)
t.end_fill()


t.penup()
t.goto(250,250)
t.pendown()
t.pencolor('yellow')
t.fillcolor('yellow')
t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()
t.goto(0,-400)
t.pendown()
t.pencolor('blue')
t.fillcolor('blue')
t.begin_fill()
t.circle(150)
t.end_fill()







t.penup()
t.goto(-200,400)
t.pendown()
t.pencolor('white')
t.fillcolor('white')
t.begin_fill()
t.circle(50)
t.end_fill()


t.penup()
t.goto(-250,400)
t.pendown()
t.pencolor('white')
t.fillcolor('white')
t.begin_fill()
t.circle(50)
t.end_fill()




t.penup()
t.goto(100,0)
t.pendown()
t.pencolor("green")
t.pensize(8)
t.goto(100,-100)
t.pensize(1)


t.penup()
t.goto(-50,100)
t.pendown()
t.pencolor('brown')
t.pensize(20)
t.goto(-50,-100)
t.pencolor('green')
t.fillcolor('green')
t.begin_fill()

t.penup()
t.goto(-50,100)
t.pendown()
t.circle(50)

t.end_fill()

t.penup()
t.goto(-200,200)
t.pendown()
t.pencolor('brown')
t.pensize(20)
t.goto(-200,-100)
t.pencolor('green')
t.fillcolor('green')
t.begin_fill()
t.penup()
t.goto(-200,100)
t.pendown()
t.circle(50)
t.end_fill()

t.penup()
t.goto(-100,300)
t.begin_fill()
t.pencolor("white")
t.fillcolor("white")
t.pendown()
t.circle(20)
t.end_fill()

t.penup()
t.goto(-130,300)
t.begin_fill()
t.pencolor("white")
t.fillcolor("white")
t.pendown()
t.circle(20)
t.end_fill()

t.penup()
t.goto(-160,300)
t.begin_fill()
t.pencolor("white")
t.fillcolor("white")
t.pendown()
t.circle(20)
t.end_fill()

t.penup()
t.goto(-145,280)
t.begin_fill()
t.pencolor("white")
t.fillcolor("white")
t.pendown()
t.circle(20)
t.end_fill()

t.penup()
t.goto(-125,280)
t.begin_fill()
t.pencolor("white")
t.fillcolor("white")
t.pendown()
t.circle(20)
t.end_fill()


t.penup()
t.goto(300,-150)
t.pencolor("green")
t.begin_fill()
t.fillcolor("green")
t.pendown()
t.circle(75)
t.end_fill()



turtle.done()



































