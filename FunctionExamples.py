#FunctionExamples.py

import turtle

def drawSquare(myTurtle):
  for i in range(4):
    myTurtle.forward(100)
    myTurtle.right(90)

def main():
  bob = turtle.Turtle()
  drawSquare(bob)

main()

input("Press enter to quit.")
