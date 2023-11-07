import turtle


# Function to draw a rectangle
def draw_rectangle():
    t.reset()
    for _ in range(2):
        t.forward(200)  # Width
        t.left(90)
        t.forward(100)  # Height
        t.left(90)


# Function to draw a smaller rectangle inside the first one
def draw_small_rectangle():
    t.reset()
    for _ in range(2):
        t.forward(200)
        t.left(90)
        t.forward(50)  # Width
        t.left(90)


# Function to draw a heart shape
def draw_heart():
    t.reset()
    t.up()
    t.goto(0, -100)
    t.down()
    t.left(140)
    t.forward(224)
    for _ in range(200):
        t.right(1)
        t.forward(2)
    t.left(120)
    for _ in range(200):
        t.right(1)
        t.forward(2)


# Function to draw two houses
def draw_houses():
    t.reset()

    def draw_house():
        for _ in range(4):
            t.forward(100)
            t.left(90)

    def draw_roof():
        t.forward(100)
        t.left(120)
        t.forward(100)
        t.left(120)

    def draw_window():
        t.up()
        t.goto(40, 40)
        t.down()
        for _ in range(4):
            t.forward(20)
            t.left(90)

    def draw_door():
        t.up()
        t.goto(70, 0)
        t.down()
        for _ in range(2):
            t.forward(20)
            t.left(90)
            t.forward(40)
            t.left(90)

    draw_house()
    draw_roof()
    draw_window()
    draw_door()

    t.up()
    t.goto(200, 0)
    t.down()

    draw_house()
    draw_roof()
    draw_window()
    draw_door()


# Main program
t = turtle.Pen()
t.speed(1)

while True:
    print("1. Rechteck")
    print("2. Herz")
    print("3. Haus")
    choice = input()

    if choice == "1":
        draw_rectangle()
    elif choice == "2":
        draw_heart()
    elif choice == "3":
        draw_houses()
    else:
        print("Invalid choice!")



turtle.done()
