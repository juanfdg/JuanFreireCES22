import turtle

def star(t):
    for i in range(5):
        t.forward(100)
        t.right(144)

wn = turtle.Screen()
wn.bgcolor('lightgreen')
pen = turtle.Pen()
pen.color('purple')

for i in range(5):
    star(pen)
    pen.forward(100)
    pen.penup()
    pen.forward(350)
    pen.pendown()
    pen.right(144)

wn.mainloop()
