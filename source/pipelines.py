from utils import Answer, Question, exercise
import math

@exercise
def pipelines():
  

  #1 
  Question(1, """
    Implement a producer-consumer pipeline where the values square by the producer are sent
    to two consumers. One Should store and print the minimum value sent so far and the other
    the maximum value.
  """)

  def square(cons):
    print('\t[Initialized]: Square Producer')
    while True:
      value = yield
      for con in cons:
        con.send(value**2)

  def min():
    init = True
    print("\t[Initialized]: Min Consumer")
    while True:
      if init:
        init = False
        minimum = yield
        print(f"\tmin.send({int(math.sqrt(minimum))}): {minimum}")
      value = yield

      if value < minimum:
        minimum = value

      print(f"\tmin.send({int(math.sqrt(value))}): {minimum}")

  def max():
    init = True
    print("\t[Initialized]: Max Consumer")
    while True:
      if init:
        init = False
        maximum = yield
        print(f"\tmax.send({int(math.sqrt(maximum))}): {maximum}")
      value = yield

      if value > maximum:
        maximum = value

      print(f"\tmax.send({int(math.sqrt(value))}): {maximum}")

  Answer("")
  maximum = max()
  next(maximum)  # Initialize
  minimum = min()
  next(minimum)  # Initialize
  sq = square([maximum, minimum])
  next(sq)  # Initialize
  sq.send(50)
  print('')
  sq.send(20)
  print('')
  sq.send(60)
  print('')
  sq.send(0)

  #2 
  Question(2, """
    Implement a producer-consumer pipeline where the values square by the producer 
    are dispatched to two consumers, one at a time. The first value should be sent 
    to consumer 1, the second value to consumer 2, third value to consumer 1 again, 
    and so on. Closing the producer should force the consumers to print a list with 
    the numbers that each one obtained.
  """)
  
  def square(consumer_list):
    print("\t[Initialized]: Square Producer")
    
    try:
      while True:
        for i in range(len(consumer_list)):
            value = yield
            consumer_list[i].send(value**2)
    except GeneratorExit:
      print('\tSquare producer exitting..')
      for consumer in consumer_list:
        consumer.close()
  
  
  def consumer(name):
    print(f"\t[Initialized]: {name} Consumer ")
    consumed = []
    try:
      while True:
        value = yield
        consumed.append(value)
    except GeneratorExit:
      print(f'\t[Closing]: {name}')
      print(f"\t{name}: {consumed}")
      
      
  Answer("")
  even = consumer('Even')
  next(even)
  odd = consumer('Odd')
  next(odd)
  sq = square([even, odd])
  next(sq)
  
  for i in range(10):
    print(f'\tsq.send({i}): {i}')
    sq.send(i)
  
  sq.close()

