import turtle

t = turtle.Turtle()

t.forward(100)
t.penup()
t.goto(50, 0)
t.pendown()
t.left(90)
t.forward(150)
t.left(-90)
t.forward(70)
t.left(-90)
t.forward(20)
t.left(-90)


def head():
    # head
    t.circle(20)


def body():
    #body
    t.penup()
    t.goto(120, 90)
    t.left(90)
    t.pendown()
    t.forward(50)


def arm1():
    #arm1
    t.left(90)
    t.forward(50)
    t.left(-180)


def arm2():
    #arm2
    t.forward(100)
    t.left(180)
    t.forward(50)


def leg1():
    #leg1
    t.left(-90)
    t.forward(20)
    t.left(50)
    t.forward(50)
    t.backward(50)


def leg2():
    #leg2
    t.left(-100)
    t.forward(50)


Lives = 6
gs = 0 #gs = game state controls when game runs



def checklives():
    if Lives == 5:
      head()
    elif Lives == 4:
      body()
    elif Lives == 3:
      arm1()
    elif Lives == 2:
      arm2()
    elif Lives == 1:
      leg1()
    elif Lives == 0:
      leg2()


def addone(answerWrong):
  answerWrong = answerWrong + 1
  
def checkguess(Lives):
  answerWrong = 0
  guess = input("Guess a letter ")
  for index in range(len(secretword)):
      print(index)
      print(secretword[index])
      if guess == secretword[index]:
        blanks[index] = guess
      else:
        addone(answerWrong)
        Lives = Lives -1 
        
blanks = ["?", "?", "?", "?", "?"]
while Lives != 0 & gs == 0:
    checklives()
    print('lives: ' + str(Lives))
    secretword = "apple"
    #blanks = ["?", "?", "?", "?", "?"]

    #def checkguess():
        #guess = input("Guess a letter ")
        #for index in range(len(secretword)):
            #print(index)
            #print(secretword[index])
            #if guess == secretword[index]:
                #blanks[index] = guess
            #else:
              #Lives = Lives-1
    checkguess(Lives)
  
    print(blanks)
