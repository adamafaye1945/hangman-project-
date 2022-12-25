import turtle
from turtle import textinput
import requests

t = turtle.Turtle()
def drawing_the_hangman(step):
    if step == 5 :
        x = 35
        y = 70
        t.penup()
        t.goto(x,y)
        t.ht()
        t.pendown()
        t.color("red")
        t.circle(25)
    if step == 4:
        t.penup()
        t.seth(270)
        t.pendown()
        t.fd(80)
        t.color("red")
      
    if step == 3:
        x = 35
        y = 55
        t.goto(x,y)
        t.penup()
        t.seth(360)
        t.pendown()
        t.fd(50)
        t.color("red")
      
    if step ==2:
        x = 35
        y = 55
        t.goto(x,y)
        t.penup()
        t.seth(180)
        t.pendown()
        t.fd(50)
      
        t.color("red")
      
    if step == 1:
        t.penup()
        x = 35
        y = -10
        t.goto(x,y)
        t.seth(240)
        t.pendown()
        t.fd(70)
        t.color("red")
      
    if step == 0:
        x = 35
        y = -10
        t.goto(x,y)
        t.penup()
        t.seth(300)
        t.pendown()
        t.fd(70)
        t.color("red")
def prompt(prompt):
    return textinput('Hangman', prompt = prompt)

def get_word():
    url = 'https://random-word-api.herokuapp.com/word'
    params = {
        'number':5
    }
    data = requests.get(url= url,params= params).json()
    return data    