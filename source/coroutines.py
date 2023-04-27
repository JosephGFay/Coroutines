from utils import Answer, Question, exercise

@exercise
def coroutines():
  
  #1 
  Question(1, """
    Create a coroutine named 'square' that prints the square of any sent value
  """)

  def square():
    while True:
      val = yield
      Answer(f'send({val}): {val**2}')

  sq = square()
  next(sq)
  sq.send(10)

  #2 
  Question(2, """
    Implement the minimize coroutine that keeps and prints the minimum value that 
    is sent to the function
  """)

  def minimize():
    init = True
    while True:
      if init:
        init = False
        min = yield
        Answer(f"send({min}): {min}")

      val = yield

      if val < min:
        min = val

      print(f"\t   send({val}): {min}", end='\n  ')

  min = minimize()
  next(min)
  min.send(5)
  min.send(7)
  min.send(1)
  min.send(0)
