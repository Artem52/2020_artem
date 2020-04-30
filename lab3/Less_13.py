import turtle

turtle.shape("turtle")
i=1
j=1
t=0
q=0.1
w=1
p=0
l=0.55
k=1.3
o=0
def krug (t):
    while i<=10 and j<=10:
        turtle.forward(i)
        turtle.left(j)
        t+=1
        if t == 360:
            break

def krug_eye (p):
    while q <= 10 and w <= 10:
        turtle.forward(q)
        turtle.left(w)
        p+=1
        if p == 360:
            break

def krug_smile (o):
    while l <= 10 and k <= 10:
        turtle.forward(l)
        turtle.right(k)
        o+=1
        if o == 140:
            break


x=0
y=0
turtle.goto(x,y)

turtle.begin_fill()
krug(t)
turtle.color('yellow')
turtle.end_fill()
turtle.penup()

turtle.goto(-25, 70) #Рисуем левый глаз


turtle.pendown()
turtle.color('black')
turtle.begin_fill()
krug_eye(p)
turtle.color('blue')
turtle.end_fill()
turtle.color('black')
turtle.penup()
turtle.goto(25,70)  #Рисуем правый глаз
turtle.pendown()
turtle.begin_fill()
krug_eye(p)
turtle.color('blue')
turtle.end_fill()


turtle.penup()  # Рисуем нос
turtle.color('black')
turtle.width(3)
turtle.goto(0, 65)
turtle.pendown()
turtle.right(90)
turtle.forward(15)


turtle.penup() #Рисуем рот
turtle.color('red')
turtle.width(4)
turtle.goto(25, 30)
turtle.pendown()
krug_smile(o)

turtle.penup()
turtle.goto(100,100)