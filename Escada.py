import turtle

a = turtle.Screen()
turtle.speed(0)

def quadrado(posx, posy,lado):
    turtle.showturtle()
    # posicioan
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.pendown()

    # desenha
    for i in range(4):
        turtle.forward(lado)
        turtle.left(90)
    turtle.hideturtle()

def pir_quadrados(n,posx, posy,lado):
    for i in range(1, n+1):
        # desenha linha i
        # posiciona
        # desenha

        for j in range(1,i+1):
            quadrado(turtle.xcor(),turtle.ycor(), lado)
            turtle.setx(turtle.xcor()+lado)

            # muda de linha
        turtle.penup()
        turtle.goto(posx,turtle.ycor()-lado)
        turtle.pendown()
    turtle.hideturtle()

quadrado(-100,280,50)
pir_quadrados(10,-100,280,50)

a.exitonclick()