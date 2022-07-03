"""
Architecture/execution model

*   The program allows users to answer trivia questions which are tailored to the user's preferences. Users are able to choose between different 
    categories and the number of answers that they want to get.
*   The difficulty of the questions will adapt on the user's skills (questions will get easier when questions are answered wrong and the other way around)
*   Dictionaries are created which save all possible categories from which the user can choose from for the quiz. This allows us to cross-check whether the specifications 
    given by the users are feasible.
*   The user interface creates a simple way for the user to give their choices on which an API will be retrieved. The choices will be saved in variables.
*   Questions are retrieved from an open API: https://opentdb.com/
*   The class 'Questions' is created in which question details and content can be saved as object and to be able to further use these objects to create quizzes
*   Creating the 'Quiz' class allows us to integrate different functions such as checking the answers.
*   A user interface is created to allow our users to practise their trivia skills. The program includes tools such as a score taking which allows
    the user to track and improve their performance.
    Furthermore, the user will have the chance to restart the program right after the quiz ends so that there is no limit in the amount of times
    the user can practise. Lastly, a timer is included for the user to measure and increase the speed in which they answer questions.


Technical specifications

*   The class Question has the attributes category, q_type, difficulty, question, correct_answer, incorrect_answers. It saves all information about each
    specific question.
*   The class Quiz has the attributes number_questions_total, q_list_easy, q_list_medium, q_list_hard. It saves the different questions which are part of the quiz 
    and divides it by level of difficulty. The class Quiz includes the most essential functions for the user to effectively interact with the Quiz. The functions include:
    next_question_easy, next_question_medium, next_question_hard, remaining questions, and checking the answer.

Directory

1. Creating dictionaries for Question settings
2. Designing the User interaction: choosing the category & number of questions
3. Cleaning data & Retrieving data from API based on user's choices
4. OOP based approach for Questions and Quiz
5. Running the Quiz
"""

from unicodedata import category
import random
import requests
import time


#--------------------------------OOP based approach for Questions and Quiz---------------------------------
class Question:    
    def _init_(self, category, q_type, difficulty, question, correct_answer, incorrect_answers):        
        self.category = category
        self.type = q_type
        self.difficulty = difficulty
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers

question_list_easy = []
question_list_medium = []
question_list_hard = []

for i in response_json['results']:
    new_question = Question(category = i['category'], q_type = i['type'], 
                            difficulty = i['difficulty'], question = i['question'], correct_answer = i['correct_answer'], incorrect_answers= i['incorrect_answers'])
    
    if i['difficulty'] == 'easy':
        question_list_easy.append(new_question)
    elif i['difficulty'] == 'medium':
        question_list_medium.append(new_question)
    else:
        question_list_hard.append(new_question)
    
class Quiz:
    def _init_(self, number_questions_total, q_list_easy, q_list_medium, q_list_hard):
        
        self.number_questions_total = number_questions_total
        self.question_score = 0
        
        # NOTE: use a dictionary here (e.g. self.questions["easy"], ...)
        self.question_list_easy = q_list_easy #list of easy questions
        self.question_list_medium = q_list_medium
        self.question_list_hard = q_list_hard
    
        # NOTE: use dictionary here, could even combine with above
        self.q_num_easy = 0 #counter for easy questions
        self.q_num_medium = 0
        self.q_num_hard = 0
        
        self.difficulty_level = 1 #1 for easy, 2 for medium and 3 for hard
        
        #response time variable
        self.start_time=0
        self.end_time=0
        self.time_diff=0

        
    # NOTE: if you use a dictionary it would be easy to combine all the following three methods into one and providing "easy"/"medium"/"difficult" as a key to the method 
    def next_question_easy(self):
        try:
            current_question = self.question_list_easy[self.q_num_easy]
            self.q_num_easy += 1

            self.start_time= time.time
            user_answer = input(f"{self.q_num_easy + self.q_num_medium + self.q_num_hard} {current_question.question} (True/False): ")  
            self.end_time= time.time   
            self.time_diff=self.end_time-self.start_time   
            if self.check_answer(user_answer, current_question.correct_answer):
                self.difficulty_level = 2
        except IndexError:
            # NOTE: if the level 2 represents medium than you could represent this using e.g. an enum to make it easy to read
            self.difficulty_level = 2 #redirect to medium difficulty if we don't have any easy questions in dataset

    def next_question_medium(self):
        try:
            current_question = self.question_list_medium[self.q_num_medium]
            self.q_num_medium += 1

            self.start_time=time.time
            user_answer = input(f"{self.q_num_easy + self.q_num_medium + self.q_num_hard} {current_question.question} (True/False): ")
            self.end_time=time.time
            self.time_diff=self.end_time-self.start_time

            if self.check_answer(user_answer, current_question.correct_answer):
                self.difficulty_level = 3
            else:
                self.difficulty_level = 1
        except IndexError:
            self.difficulty_level = 1
            
    def next_question_hard(self):
        try:
            current_question = self.question_list_hard[self.q_num_hard]
            self.q_num_hard += 1

            self.start_time=time.time()
            user_answer = input(f"{self.q_num_easy + self.q_num_medium + self.q_num_hard} {current_question.question} (True/False): ")
            self.end_time= time.time()
            self.time_diff=self.end_time-self.start_time
            if self.check_answer(user_answer, current_question.correct_answer):
                self.difficulty_level = 3
            else:
                self.difficulty_level = 2
        except IndexError:
            self.difficulty_level = 2
        
    def remaining_questions(self):
        return (self.q_num_easy + self.q_num_medium + self.q_num_hard) < self.number_questions_total

    def check_answer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            self.question_score += 1
            print("Awesome, You got it right!")
            print(f"Your current score is: {self.question_score}/{self.q_num_easy + self.q_num_medium + self.q_num_hard}\n")
            return True
        else:
            print("Oops, you got it wrong!")
            print(f"The correct answer was: {answer}")
            print(f"Your current score is: {self.question_score}/{self.q_num_easy + self.q_num_medium + self.q_num_hard}\n")
            return False 


#------------------------- Running the Quiz ---------------------------------
quiz = Quiz(NB_Questions, question_list_easy, question_list_medium, question_list_hard)

while quiz.remaining_questions():
    # NOTE: see above this could be a single method quiz.next_question as the state of difficulty level is already kept by quiz and does not need to be exposed here
    if quiz.difficulty_level == 1:
        quiz.next_question_easy()
    elif quiz.difficulty_level == 2:
        quiz.next_question_medium()
    else:
        quiz.next_question_hard()   

print(f"Your final score is: {quiz.question_score}")

#code will start from here------------------
if __name__=="__main__":
#----------------Creating dictionaries for Question settings-------------------------
    Categories = {0 : "Random", 9 : 'General Knowledge', 10 : 'Entertainment: Books', 11: 'Entertainment: Film', 12 : 'Entertainment: Music',
        13 : 'Entertainment: Musicals & Theatres', 14: 'Entertainment: Television', 15:'Entertainment: Video Games', 16 :'Entertainment: Board Games',
        17 : 'Science & Nature', 18:'Science: Computers', 19: 'Science: Mathematics', 20 : 'Mythology', 21 : 'Sports', 22: 'Geography',
        23 : 'History', 24 : 'Politics', 25 : 'Art', 26:'Celebrities', 27 : 'Animals', 28 : 'Vehicles', 29 :  'Entertainment: Comics',
        30 : 'Science: Gadgets', 31: 'Entertainment: Japanese Anime & Manga', 32 : 'Entertainment: Cartoon & Animations'}


#----------------Designing the User interaction: choosing the category-----------------

    print("Hi, Welcome!")

    print("Here is the Menu:")

#-----CATEGORY-----

#Print the number and the category
    for i in Categories:
        print(i, Categories[i])

# NOTE: can get rid of this variable and instead use a while true: with a break
    check_loop = True
    while check_loop:
        #Input Category
        # NOTE: use snake case (lower case beginning)
        Chose_Cat = 0
        # NOTE: validate that the user input is actually a number and recover if not
        Chosen_Cat = int(input("Please, input here a (valid) number for a category: "))
        #Check valid category
        try:
            print('You have chosen :', Categories[Chosen_Cat])
            check_loop = False
        except:
            check_loop = True

    print('\n')

    #-----NB QUESTIONS-----
    # NOTE: better variable naming and move this all into a function
    NB_Questions = 0
    #Check valid input
    while NB_Questions < 1 or NB_Questions >50:
         # NOTE: recover if not integer input
        NB_Questions = int(input('How many Questions ? (<30) '))
    print('\n')

    #----------------Cleaning data & Retrieving data from API based on user's choices-------------------------

    #Data cleaning
    def replace_all(text, dic):
        for i, j in dic.items():
            text = text.replace(i, j)
        return text

    replacement_values = {"#quot;": "'", "quot;": "'", "#039;": "'", "039;": "'"}

    def clean_dataset(dataset):
        for d in dataset["results"]:
            d["question"] = d["question"].replace("&", "")
            d["question"] = replace_all(d["question"], replacement_values)

        d["correct_answer"] = d["correct_answer"].replace("&", "")
        d["correct_answer"] = replace_all(d["correct_answer"], replacement_values)
        
        for item in d["incorrect_answers"][0:3]:
            item = item.replace("&", "")
            item = replace_all(item, replacement_values)
            d["incorrect_answers"].append(item)
        del d["incorrect_answers"][0:3]
        return dataset

#Retrieving data
    buffer = 20
    url = "https://opentdb.com/api.php?amount="+str(NB_Questions+ buffer)+ "&category=" + str(Chosen_Cat) + "&type=boolean"

    response = requests.get(url)
    response_json = clean_dataset(response.json())






# NOTE: could wrap the whole program to allow to start another quiz after this round
#@Sudanshu could you look into this?

# NOTE: add additional features: a timer? Showing the level of difficulty when asking a question? Something else?
# NOTE: Wrap code in a function and call it using if name == 'main'
# NOTE: Move classes to separate files 
#@Sudanshu