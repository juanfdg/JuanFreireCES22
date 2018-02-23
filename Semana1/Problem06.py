import turtle

wn = turtle.Screen()
pen = turtle.Pen()

for i in range(3):
    pen.forward(50)
    pen.left(120)

for i in range(4):
    pen.forward(50)
    pen.left(90)

for i in range(6):
    pen.forward(50)
    pen.left(60)

for i in range(8):
    pen.forward(50)
    pen.left(45)

wn.mainloop()
