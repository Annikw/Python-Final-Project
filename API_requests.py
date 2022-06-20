#DATA CONNECTION

#https://opentdb.com/api_config.php

#manually generated API https://opentdb.com/api.php?amount=10&category=10&difficulty=easy&type=multiple

#simple creating an API manually to test
from tkinter import MULTIPLE
from unicodedata import category
import requests
response = requests.get("https://opentdb.com/api.php?amount=10&category=10&difficulty=easy&type=multiple")
print(response.headers)

#next would be automating the request based on how many function in which difficulty level etc we want

#CODE

#DATA CONNECTION

#Creating the base class 'Question' 

class Questions:
    """
    Question is the base class for different types of stock.

    Attributes
    ----------
    XX : str
        Indicates the season in which the stock object is being sold i.e. SS22 (Spring/ Summer 22)
    XX : float
        Indicates the price of the stock object in euros
    """
    def __init__(self, question: str, correct_answer: str, wrong_answers: str, category: str, multiple: str) -> None:
        self.question = question
        self.correct_answer = correct_answer
        self.wrong_answer = wrong_answers
        self.category = category_
        self.multiple = multiple_

#Creating the classes 'easy', 'medium' and 'difficult question' which inherit the base class
#we are creating a list for each object of the class --> so that it can later be stores in the question data base
 

 #we could do inheritance for easy medium and difficult question but I dont think it is necessary really
 class Easy_question(Question):
    """
    The Easy_question class inherits the Question class and contains information about the object only relevant for the easy questions

    Attributes
    ----------
    XXX: todo
     ...
    """
    def __repr__(self):
        return ",".join([str(self.question), str(self.correct_answer),str(self.wrong_answer), str(self.category), str(self.multiple) ])
    def __init__(self, question: str, correct_answer: str, wrong_answer: str, category: str, multiple: str) -> None:
        super().__init__(question, correct_answer, wrong_answer, category, multiple)
    

class Quiz:
    #here is where we actually mix and match the questions together to form a quiz which users can take
    #I copied in my code from the warehousing so that we see how functions and the way the information is saved could look like.
    #An idea would be to save all the questions of the quiz in a list. See below:


class Warehouse:
    """
    The warehouse class provides functionalities of stock count; stock removal & add-in and stock transfer.

    Attributes
    ----------
    location:
      Indicates the location of the warehouse. As 'Europe' is by far the biggest warehouse it is the default argument.
    shirt_stock: 
      Takes objects of the class 'Shirt' as input. It is a list of Shirt[s]. 
    pants_stock: 
      Takes objects of the class 'Pants' as input. It is a list of Pants.
    blouse_stock: 
      Takes objects of the class 'Blouse' as input. It is a list of Blouse[s].
    """
    def __init__(self, location: str = 'Europe', shirt_stock: list = [], pants_stock: list = [], blouse_stock: list = []):
        self.location = location
        self.shirt_stock = shirt_stock
        self.pants_stock = pants_stock
        self.blouse_stock = blouse_stock

#Print stock count functions
    def print_stock_count_shirt(self):
        length = len(self.shirt_stock)
        print(f"There is {length} shirt[s] in the warehouse")
    
    def print_stock_count_pants(self):
        length = len(self.pants_stock)
        print(f"There is {length} pants in the warehouse")

    def print_stock_count_blouse(self):
        length = len(self.blouse_stock)
        print(f"There is {length} blouse[s] in the warehouse")

#Get stock functions
    def get_stock_shirt(self):
        return self.shirt_stock

    def get_stock_pants(self):
        return self.pants_stock

    def get_stock_blouse(self):
        return self.blouse_stock

#Add stock functions
#TODO in all following: use descriptive variable names instead of x
    def add_stock_shirt(self, shirt_input: Shirt):
        self.shirt_stock.append(shirt_input)

    def add_stock_pants(self, pants_input: Pants):
        self.pants_stock.append(pants_input)
    
    def add_stock_blouse(self, blouse_input: Blouse):
        self.blouse_stock.append(blouse_input)

#Update/ take out stock functions
    def remove_stock_shirt(self, shirt_input: Shirt):
        self.shirt_stock.remove(shirt_input)

    def remove_stock_pants(self, pants_input: Pants):
        self.pants_stock.remove(pants_input)
    
    def remove_stock_blouse(self, blouse_input: Blouse):
        self.blouse_stock.remove(blouse_input)