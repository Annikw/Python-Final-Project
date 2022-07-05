"""
ARCHITECTURE
*   The program allows users to answer trivia questions which are tailored to the user's preferences. Users are able to choose between different categories and the number of answers that they want to get 
    The user interface creates a simple way for the user to give their choices on which an API will be retrieved. The choices will be saved in variables and the choice of category will be cross-checked with a dictionary that contains all the different categories to ensure that users do not pick any category that doesnt exist. 
*   Questions are retrieved from an open API: https://opentdb.com/ 
*   The difficulty of the questions will adapt on the user's skills (questions will get easier when questions are answered wrongly and the other way around) 
*   Creating the 'Quiz' class allows us to save all the different questions which will be asked in one specific Quiz. It also allows us to give different functionalities into the program by integrating different functions 
*   The functionalities of the program are summarized here: 
*   Tailored to user preferences 
*   Adaptable difficulty level 
*   Score tracking 
*   Scores in the form of questions answered correctly out of total questions are tracked throughout the game 
*   At the end of each game, the final score can be seen by the user 
*   Restarting program 
    *   Users can restart the quiz after the quiz ends so that there is no limit in the number of times the user can practise 
    
TECHNICAL SPECIFICATIONS
*  The class Quiz has the attributes number_questions_total, q_list_easy, q_list_medium, q_list_hard. It saves the different questions which are part of the quiz and divides it by level of difficulty. The class Quiz includes the most essential functions for the user to effectively interact with the Quiz. The functions include: 
    *  next_question_easy 
    *  next_question_medium 
    *  next_question_hard 
    *  remaining questions
    *  checking the answer
*  The class docstring defines its attributes in more detail. Therefore, please find further specifications in the code below. 

LICENSE: MIT LICENSE
Copyright (c) 2022 Annikw
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

DIRECTORY
1. OOP based approach for the class Quiz 
2. Function to run the quiz 
3. Designing the User interaction: choosing the category & number of questions
4. Cleaning data & Retrieving data from API based on user's choices 
5. Running and restarting the Quiz 
"""
from unicodedata import category
import random
import requests

# --------------------------------OOP based approach for Questions and Quiz---------------------------------
class Quiz:
    """
    The Quiz class contains information about each quiz which is created for the User. It contains all the questions of the quiz.
    Attributes
    ----------
    number_questions_total: int
        Indicates the amount of questions that the user wants to answer.
    q_list_easy: list
        Indicates all the questions of difficulty 'easy' in form of a list of objects of the class Questions
    q_list_medium: list
        Indicates all the questions of difficulty 'medium' in form of a list of objects of the class Questions
    q_list_hard: list
        Indicates all the questions of difficulty 'hard' in form of a list of objects of the class Questions""" 

    def __init__(self, number_questions_total: int, q_list_easy: list, q_list_medium: list, q_list_hard: list):

        self.number_questions_total = number_questions_total
        self.question_score = 0
        
        self.question_list_easy = q_list_easy  # list of easy questions
        self.question_list_medium = q_list_medium
        self.question_list_hard = q_list_hard

        self.q_num_easy = 0  # counter for easy questions
        self.q_num_medium = 0
        self.q_num_hard = 0

        self.difficulty_level = 1  # 1 for easy, 2 for medium and 3 for hard
    # NOTE: for future --> use dictionaries to combine functions
    
    def next_question_easy(self):
        try:
            current_question = question_list_easy[self.q_num_easy]
            print("Difficulty of the Question:", current_question[2],":")
            self.q_num_easy += 1

            while True:
                user_answer = input(
                    f"{self.q_num_easy + self.q_num_medium + self.q_num_hard} {current_question[3]} (True/False): ")
                if user_answer == "True" or user_answer == "False":
                    break
                else:
                    print("please, answer True or False")

            if self.check_answer(user_answer, current_question[4])==True:
                self.difficulty_level = 2
        except IndexError:
            self.difficulty_level = 2  # redirect to medium difficulty if we don't have any easy questions in dataset

    def next_question_medium(self):
        try:
            current_question = question_list_medium[self.q_num_medium]
            print("Difficulty of the Question:", current_question[2], ":")
            self.q_num_medium += 1

            while True:
                user_answer = input(
                    f"{self.q_num_easy + self.q_num_medium + self.q_num_hard} {current_question[3]} (True/False): ")
                if user_answer == "True" or user_answer == "False":
                    break
                else:
                    print("please, answer True or False")

            if self.check_answer(user_answer, current_question[4])==True:
                self.difficulty_level = 3
            else:
                self.difficulty_level = 1
        except IndexError:
            self.difficulty_level = 2

    def next_question_hard(self):
        try:
            current_question = question_list_hard[self.q_num_hard]
            print("Difficulty of the Question:", current_question[2], ":")
            self.q_num_hard += 1

            while True:
                user_answer = input(
                    f"{self.q_num_easy + self.q_num_medium + self.q_num_hard} {current_question[3]} (True/False): ")
                if user_answer == "True" or user_answer == "False":
                    break
                else:
                    print("please, answer True or False")

            if self.check_answer(user_answer, current_question[4])==True:
                self.difficulty_level = 3
            else:
                self.difficulty_level = 2
        except IndexError:
            self.difficulty_level = 1

    def remaining_questions(self):
        return (self.q_num_easy + self.q_num_medium + self.q_num_hard) < self.number_questions_total

    def check_answer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            self.question_score += 1
            print("Awesome, You got it right!")
            print(
                f"Your current score is: {self.question_score}/{self.q_num_easy + self.q_num_medium + self.q_num_hard}\n")
            return True
        else:
            print("Oops, you got it wrong!")
            print(f"The correct answer was: {answer}")
            print(
                f"Your current score is: {self.question_score}/{self.q_num_easy + self.q_num_medium + self.q_num_hard}\n")
            return False

        # ------------------------- Function to run the quiz ---------------------------------

    def run_quiz(self):
        self.quiz = Quiz(NB_Questions, question_list_easy, question_list_medium, question_list_hard)
        while self.quiz.remaining_questions():
            if self.quiz.difficulty_level == 1:
                self.quiz.next_question_easy()
            elif self.quiz.difficulty_level == 2:
                self.quiz.next_question_medium()
            else:
                self.quiz.next_question_hard()

        print(f"Your final score is: {self.quiz.question_score}")

# code will start from here------------------
if __name__ == "__main__":
    
    # ----------------Designing the User interaction: choosing the category & number of questions-----------------
    def Chosen_Category():
        # -----CATEGORY-----
        Categories = {0: "Random", 9: 'General Knowledge', 10: 'Entertainment: Books', 11: 'Entertainment: Film',
                      12: 'Entertainment: Music',
                      13: 'Entertainment: Musicals & Theatres', 14: 'Entertainment: Television',
                      15: 'Entertainment: Video Games', 16: 'Entertainment: Board Games',
                      17: 'Science & Nature', 18: 'Science: Computers', 19: 'Science: Mathematics', 20: 'Mythology',
                      21: 'Sports', 22: 'Geography',
                      23: 'History', 24: 'Politics', 25: 'Art', 26: 'Celebrities', 27: 'Animals', 28: 'Vehicles',
                      29: 'Entertainment: Comics',
                      30: 'Science: Gadgets', 31: 'Entertainment: Japanese Anime & Manga',
                      32: 'Entertainment: Cartoon & Animations'}

        print("Hi, Welcome!")
        print("Here is the Menu:")

        for i in Categories:
            print(i, Categories[i])
        check_loop = True
        while check_loop:
            # Input Category
            Chose_Cat = 0
            Chosen_Cat = int(input("Please, input here a (valid) number for a category: "))
            # Check valid category
            try:
                print('You have chosen :', Categories[Chosen_Cat])
                check_loop = False
            except:
                check_loop = True
        print('\n')
        return Chosen_Cat

    def Chosen_NB_Questions():

        # -----NB QUESTIONS-----
        NB_Questions = 0
        # Check valid input
        while NB_Questions < 1 or NB_Questions > 30:
            NB_Questions = int(input('How many Questions ? (<30) '))
        print('\n')
        return NB_Questions

        # ----------------Cleaning data & Retrieving data from API based on user's choices-------------------------
    def replace_all(text, dic):
        for i, j in dic.items():
            text = text.replace(i, j)
        return text

    def clean_dataset(dataset):
        replacement_values = {"#quot;": "'", "quot;": "'", "#039;": "'", "039;": "'"}
        for d in dataset["results"]:
            try:
                d["question"] = d["question"].replace("&", "")
                d["question"] = replace_all(d["question"], replacement_values)
            except:
                pass

            try:
                d["correct_answer"] = d["correct_answer"].replace("&", "")
                d["correct_answer"] = replace_all(d["correct_answer"], replacement_values)
            except:
                pass

            for item in d["incorrect_answers"][0:3]:
                try:
                    item = item.replace("&", "")
                    item = replace_all(item, replacement_values)
                    d["incorrect_answers"].append(item)
                    del d["incorrect_answers"][0:3]
                except:
                    pass
        return dataset

    def get_Questions(url1,url2,url3,buffer, NB_Questions, Chosen_Cat):

        NB_Questions_Available = NB_Questions + 1 + buffer

        #Check if there are enough questions, if not, get the max amount of questions possible
        not_enough_question = True
        Wanted_Questions = NB_Questions_Available
        while not_enough_question:
            if Wanted_Questions >= 1:
                Wanted_Questions -= 1
                url = str(url1) + str(Wanted_Questions) + str(url2) + str(Chosen_Cat) + str(url3)
                response = requests.get(url)
                if len(response.json()['results']) == 0:
                    print("Loading the questions ...")
                else:
                    not_enough_question = False
            else:
                pass

        if len(response.json()['results']) < NB_Questions:
            print("sorry, it appeears that only",len(response.json()['results']) ,"questions were available! let's start anyway!")
            NB_Questions = len(response.json()['results'])

        response_json = clean_dataset(response.json())

        question_list_easy = []
        question_list_medium = []
        question_list_hard = []
        for i in response_json['results']:
            new_question = [i['category'], i['type'],i['difficulty'],i['question'], i['correct_answer']]
            if i["correct_answer"] == "True":
                new_question.append("False")
            else:
                new_question.append('True')
            if i['difficulty'] == 'easy':
                question_list_easy.append(new_question)
            elif i['difficulty'] == 'medium':
                question_list_medium.append(new_question)
            else:
                question_list_hard.append(new_question)

        return NB_Questions, question_list_easy, question_list_medium, question_list_hard

        # ----------------Running and restarting the Quiz-------------------------

    restart = True
    check = True
    while restart:
        check = True
        buffer = 10
        Chosen_Cat = Chosen_Category()
        NB_Questions = Chosen_NB_Questions()
        url1 = "https://opentdb.com/api.php?amount="
        url2 = "&category="
        url3 = "&type=boolean"
        NB_Questions, question_list_easy, question_list_medium, question_list_hard = get_Questions(url1,url2,url3,buffer, NB_Questions, Chosen_Cat)
        Quiz(NB_Questions,question_list_easy,question_list_medium,question_list_hard).run_quiz()

        while check:
            play_again = input("Would you like to play again? (Yes/No) ")
            if play_again == "No" or play_again == "Yes":
                check = False
            else:
                pass
        if play_again == "Yes":
            print("Let's play again!")
        else:
            restart = False