import turtle
def cube( taille , color_1 ,color_2 ,color_3):
    turtle.down()

    turtle.color(color_1)
    turtle.begin_fill()
    for i in range (2):
        turtle.forward(taille)
        turtle.right(120)
        turtle.forward(taille)
        turtle.right(60)
    turtle.end_fill()

    #

    turtle.color(color_2)

    turtle.begin_fill()
    turtle.forward(taille)
    turtle.left(120)
    turtle.forward(taille)
    turtle.left(60)
    turtle.forward(taille)
    turtle.left(120)
    turtle.forward(taille)
    turtle.end_fill()
    #

    turtle.color(color_3)

    turtle.begin_fill()
    turtle.right(60)
    turtle.forward(taille)
    turtle.right(120)
    turtle.forward(taille)
    turtle.right(60)
    turtle.forward(taille)
    turtle.right(120)
    turtle.forward(taille)
    turtle.end_fill()

    turtle.color(color_3)
    turtle.left(60)
    turtle.up()

    turtle.forward(taille*3)
coter = 100
ligne= 2
def clone(ligne,coter,fin,bep):
    turtle.goto(fin,bep)
    for i in range(ligne):
      cube(coter,"red","blue","black")

    turtle.goto((coter+(coter/2))+bep,(coter-coter*0.13))

    for i in range(ligne):
      cube(coter,"red","blue","black")
    

    turtle.color("green")
   

  
    
clone(ligne,coter,0,0)
clone(ligne,coter,0,175)
