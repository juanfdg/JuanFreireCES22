import turtle

wn = turtle.Screen()
pen = turtle.Pen()

wn.bgcolor('lightgreen')
pen.color('blue')
pen.shape('turtle')

pen.stamp()

for i in range(12):
    pen.hideturtle()
    pen.forward(100)
    pen.showturtle()
    pen.stamp()
    pen.hideturtle()
    pen.back(100)
    pen.right(30)

wn.mainloop()
