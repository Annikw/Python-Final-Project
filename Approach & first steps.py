#DATA CONNECTION

#https://opentdb.com/api_config.php

#manually generated API https://opentdb.com/api.php?amount=10&category=10&difficulty=easy&type=multiple

#simple creating an API manually to test
#from tkinter import MULTIPLE
#from unicodedata import category
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

class Quiz:
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
    #here is where we actually mix and match the questions together to form a quiz which users can take
    #I copied in my code from the warehousing so that we see how functions and the way the information is saved could look like.
    #An idea would be to save all the questions of the quiz in a list. See below:

    def __init__(self, category: str = 'Entertainment: Books', questions_easy: list = [], questions_medium: list = [], questions_difficult: list = []):
        self.category = category
        self.questions_easy = questions_easy
        self.questions_medium = questions_medium
        self.questions_difficult = questions_difficult

#Get Question details functions
    def get_questions_easy(self):
        return self.questions_easy

    def get_questions_medium(self):
        return self.questions_medium

    def get_questions_difficult(self):
        return self.questions_difficult

#Add stock functions
    def add_questions_easy(self, easy_input: questions_easy):
        self.questions_easy.append(easy_input)

    def add_questions_medium(self, medium_input: questions_medium):
        self.questions_medium.append(medium_input)

    def add_questions_difficult(self, difficult_input: questions_difficult):
        self.questions_difficult.append(difficult_input)
