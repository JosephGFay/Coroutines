import os
from colorama import init
from termcolor import colored
init()

class Question:

  def __init__(self, num, question):
    self.num = num
    self.question = question
    print(colored(f"\nQuestion # {num}", 'blue'), end='')
    print(f"{question}", end='')

class Answer:
  def __init__(self, answer):
    self.answer = answer
    print(colored("\tAnswer:", 'green'), end=' ')
    print(answer)

class SubQuestion():
  def __init__(self, num, question):
    self.num = num
    self.question = question
    print(f"\n\t{num}. {question}")

def clear_terminal():
  os.system('clear')

def exercise(func):
  def wrapper():
    print('')
    print(colored(f"EXERCISES WITH {str(func.__name__.upper())}",'red').center(90,'_'))
    func()
  return wrapper

def header_red(string):
  print(colored(string, 'red'))

def header_blue(string):
  print(colored(string, 'blue'))

def header_green(string):
  print(colored(string, 'green'))

def terminal_input():
  inp = input(colored("\n@ITSE-1302-M2:-~ ", 'blue'))
  return inp

def list_files(list):
  count = 1
  for i in list:
    print(f"\t{count}. {i.__name__}.py")
    count += 1
  
  
  
