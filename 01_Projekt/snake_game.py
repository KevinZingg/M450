import turtle
import time
import random

delay = 0.1

score = 0
high_score = 0

wn = turtle.Screen()
wn.title = ('snake_game')
wn.bgcolor =('white')
wn.setup (width=1000, height=700)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = 'up'


food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

pen = turtle.Turtle()
pen.speed()
pen.shape('square')
pen.color('black')
pen.penup()
pen.hideturtle()
pen.goto(0, 310)
pen.write('SCORE: 0  HIGH SCORE: 0', align='center', font=('courier', 24, 'normal'))



def go_up():
    if head.direction != 'down':
        head.direction = 'up'

def go_down():
    if head.direction != 'up':
        head.direction = 'down'

def go_left():
    if head.direction != 'right':
        head.direction = 'left'

def go_right():
    if head.direction != 'left':
        head.direction = 'right'

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)

#keyboard bindings

wn.listen()
wn.onkeypress(go_up, 'w' )
wn.onkeypress(go_up, 'W' )

wn.onkeypress(go_down, 's')
wn.onkeypress(go_down, 'S' )

wn.onkeypress(go_left, 'a')
wn.onkeypress(go_left, 'A' )

wn.onkeypress(go_right, 'd',)
wn.onkeypress(go_right, 'D' )

while True:
    wn.update()

    if head.xcor()>490 or head.xcor()<-490 or head.ycor()>340 or head.ycor()<-340:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'stop'

        for segment in segments:
            segment.goto(3000, 3000)
        segments.clear()

        score = 0

        delay = 0.1

        pen.clear()
        pen.write('SCORE: {}  HIGH SCORE: {}'.format(score, high_score), align='center', font=('courier', 24, 'normal'))

    if head.distance(food) < 20:
        x = random.randint(-490, 490)
        y = random.randint(-340, 340)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('black')
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001

        score += 10

        if score > high_score:
            high_score = score
            pen.clear()
            pen.write('SCORE: {}  HIGH SCORE: {}'.format(score, high_score), align='center', font=('courier', 24, 'normal'))

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()


    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'


            for segment in segments:
                segment.goto(1000, 1000)


            segments.clear()



            score = 0

            delay = 0.1

            pen.clear()
            pen.write('SCORE: {}  HIGH SCORE: {}'.format(score, high_score), align='center', font=('courier', 24, 'normal'))


    time.sleep(delay)
wn.mainloop()