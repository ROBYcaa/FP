import turtle



def rechtecke():
    t.reset()
    # r1
    for _ in range(2):
        t.forward(200)  # Breite
        t.left(90)
        t.forward(100)  # Höhe
        t.left(90)

    # r2
    t.up()
    t.goto(75, 25)
    t.down()
    for _ in range(2):
        t.forward(50)  # Breite
        t.left(90)
        t.forward(25)  # Höhe
        t.left(90)



def herz():
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
    t.forward(224)



def haeuser():
    t.reset()

    def haus():
        # Haus

        for _ in range(4):
            t.forward(100)
            t.left(90)

        # Dach

        for _ in range(3):
            t.forward(100)
            t.left(120)

        # Tür
        t.up()
        t.down()
        for _ in range(2):
            t.forward(20)
            t.left(90)


        # Fenster
        t.up()
        t.down()
        for _ in range(4):
            t.forward(20)
            t.left(90)

    t.up()
    t.goto(-150, 0)
    t.down()
    haus()

    t.up()
    t.goto(100, 0)
    t.down()
    haus()



t = turtle.Pen()
t.speed(1)

while True:

    print("1. Rechtecke")
    print("2. Herz")
    print("3. Haeuser")
    auswahl = input()

    if auswahl == "1":
        rechtecke()
    elif auswahl == "2":
        herz()
    elif auswahl == "3":
        haeuser()


turtle.done()
