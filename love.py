import turtle

# Fungsi untuk menggambar hati
def draw_heart():
    turtle.color('red')
    turtle.begin_fill()
    turtle.fillcolor('red')
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50, 200)
    turtle.right(140)
    turtle.circle(50, 200)
    turtle.forward(133)
    turtle.end_fill()

# Mengatur posisi awal
turtle.penup()
turtle.goto(0, -150)
turtle.pendown()

# Menggambar simbol love
draw_heart()

# Menutup jendela ketika di-klik
turtle.exitonclick()
