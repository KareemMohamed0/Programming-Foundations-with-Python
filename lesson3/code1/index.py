import turtle


def draw_square(brad):
    for i in range(0, 4):
        brad.forward(100)
        brad.right(90)


def draw_arc():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    for i in range(0, 360, 10):
        draw_square(brad)
        brad.right(10)
    # angie = turtle.Turtle()
    # angie.shape("arrow")
    # angie.color("blue")
    # angie.circle(100)
    window.exitonclick()


draw_arc()
