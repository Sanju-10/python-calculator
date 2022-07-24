



#Add
from turtle import clear


def add(n1,n2):
  return n1+n2

#Subtract
def subtract(n1,n2):
  return n1-n2

#Multiply
def multiply(n1,n2):
  return n1*n2

#Divide
def divide(n1,n2):
  return n1/n2

#Operations
operations={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}


def calculator():
  #take number 1 as the input
  num1=float(input("What's the first number?: ")) 
  for symbol in operations:
    print(symbol)
  decision=True;
  while decision:    
    #take operation as the input
    operation_symbol=input("Pick an operation from the line above: ")

    #take number 2 as the input
    num2=float(input("What's the next number?: "))

    #call the function according to the symbol
    def calculation(n1,n2,symbol):
      return operations[symbol](n1,n2)

    answer=float(calculation(num1,num2,operation_symbol))

    print(f"{num1} {operation_symbol} {num2} = {answer}") 

    # operation_symbol=input("Pick another operation: ")
    # num3=int(input("What's the next number?: "))
    # second_answer=int(calculation(first_answer,num3,operation_symbol))

    # print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
      #take decision
    decision_input=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation.: " ).lower()
    if(decision_input=="y"):
      num1=answer;
    else:
      decision=False
      calculator() 

calculator()