import turtle

wn = turtle.Screen()
pen = turtle.Pen()
side = 100

path = [(45,side*2**(1/2)), (90,side*(1/2)**(1/2)), (90,side*(1/2)**(1/2)), (90,side*2**(1/2)),
        (135,side), (90,side), (90,side), (90,side)]

def follow_path(pen, path):
    for (angle, distance) in path:
        pen.left(angle)
        pen.forward(distance)


follow_path(pen, path)
wn.mainloop()

