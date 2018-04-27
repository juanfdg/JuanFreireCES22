import turtle

def star(t):
    for i in range(5):
        t.forward(100)
        t.right(144)

wn = turtle.Screen()
pen = turtle.Pen()
star(pen)

wn.mainloop()
