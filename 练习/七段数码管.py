import turtle as t
import time
def drawGap():
    t.penup()
    t.fd(5)
def drawLine(draw):
    drawGap()
    t.pendown() if draw else t.penup()
    t.fd(40)
    drawGap()
    t.right(90)
def drawDigit(digit):
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    t.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    t.left(180)
    t.penup()
    t.fd(20)
def drawDate(date):
    t.pencolor("red")
    for i in date:
        if i == '-':
            t.write("年",font=("Arial",18,"normal"))
            t.pencolor("green")
            t.fd(40)
        elif i == '=':
            t.write("月",font=("Arial",18,"normal"))
        elif i == '+':
            t.write("日",font=("Arial",18,"normal"))
        else :
            drawDigit(eval(i))
def main():
    t.setup()
    t.penup()
    t.fd(-300)
    t.pensize(5)
    drawDate(time.strftime("%Y-%m=%d+",time.gmtime()))
    t.hideturtle()
    t.done()
main()
