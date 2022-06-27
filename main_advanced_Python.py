"""
*Architecture/execution model*

*   The program allows users to answer trivia questions which are tailored to the user's preferences. Users are able to choose between different 
    categories and the number of answers that they want to get.
*   The difficulty of the questions will adapt on the user's skills (will get easier when questions are answered wrong and the other way around)
*   Dictionaries are created which save all possible categories from which the user can choose from for the quiz. This allows
    us to cross-check whether the specifications given by the users are feasible.
*   The user interface creates a simple way for the user to give their choices on which an API will be retrieved.
*   Questions are retrieved from an open API
*   The class 'Questions' is created in which question details and content can be saved as object and to be able to further use these objects to create quizzes
*   Creating the 'Quiz' class allows us to integrate different functions such as checking the answers.
*   A user interface is created to allow our users to practise their trivia skills.

*Technical specifications*

*   The class Question has the attributes category, q_type, difficulty, question, correct_answer, incorrect_answers.
*   The class Quiz has the attributes number_questions_total, q_list_easy, q_list_medium, q_list_hard.

*Directory*

1. Creating dictionaries for Question settings
2. Designing the User interaction: choosing the category
3. Retrieving data from API based on user's choices
4. OOP based approach: Creating the Question Class
5. OOP based approach: Creating the Quiz Class
6. Running the Quiz
"""

from unicodedata import category
import requests
import random

# NOTE: Standardize formatting of comments
# NOTE: Move classes to separate files
# NOTE: Wrap code in a function and call it using if _name_ == '_main_'
# NOTE: Use functions to encapsulate concepts. 
#       e.g. instead of comments such as "Retrieving data from API based on user's choices" create a function called 'retrieve_questions', ...



#----------------Creating dictionaries for Question settings-------------------------
'''the dictionaries will allow the user to choose the different categories'''

#Dictionary for the categories
Categories = {0 : "Random", 9 : 'General Knowledge', 10 : 'Entertainment: Books', 11: 'Entertainment: Film', 12 : 'Entertainment: Music',
        13 : 'Entertainment: Musicals & Theatres', 14: 'Entertainment: Television', 15:'Entertainment: Video Games', 16 :'Entertainment: Board Games',
        17 : 'Science & Nature', 18:'Science: Computers', 19: 'Science: Mathematics', 20 : 'Mythology', 21 : 'Sports', 22: 'Geography',
        23 : 'History', 24 : 'Politics', 25 : 'Art', 26:'Celebrities', 27 : 'Animals', 28 : 'Vehicles', 29 :  'Entertainment: Comics',
        30 : 'Science: Gadgets', 31: 'Entertainment: Japanese Anime & Manga', 32 : 'Entertainment: Cartoon & Animations'}


#----------------Designing the User interaction: choosing the category-------------------------
'''In this section, we are asking the user to give input in terms of categories, difficulty, number of questions, and type of question to allow
the user to create a customized test design.
Choices are saved into variables'''

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
    # NOTE: this should not be stored in the same variable as this is confusing. Keep the user`s choice and do the buffering somewhere else
    NB_Questions = NB_Questions + 20 #proposal here is to always add 20 questions more so that we can always adjust the difficulty level. --> Buffer
print('\n')

#----------------Retrieving data from API based on user's choices-------------------------

# NOTE: what is this used for?
Score = 0

#url for choosing only category and number of questions
# NOTE: abstract the API logic away behind a function or even create a `question_api` class to interact with
url = "https://opentdb.com/api.php?amount="+str(NB_Questions)+ "&category=" + str(Chosen_Cat) + "&type=boolean"

response = requests.get(url)
response_json = response.json()

#--------------------------------OOP based approach---------------------------------
'''Note from Annik: here we could also try to always extract a mix of difficulties from the API by selecting 'Any difficulty' 
This way, based on whether the previous answer was right or wrong --> the next question could have a different difficulty (the professor proposed
this when talking to him in class)

Note from Wilm:
The quiz is now automatically adjusting difficulty based on the previous answer. 
I think it might be easiest if we only take True/False questions. That would make the coding part easier with only minor 
reduction in functionality, since we will never actually use the quiz in real life.
We should keep in mind that we now need a much larger set of questions, since we have to adjust to their skill level. The current code
automatically redirects the user to a different difficulty level if we run out of questions for any one difficulty. 
'''

#Creating Question as the class including all details for each question (questions as the objects of the class)
class Question:    
    def init(self, category, q_type, difficulty, question, correct_answer, incorrect_answers):        
        self.category = category
        self.type = q_type
        self.difficulty = difficulty
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers

#add instances of the class to lists, based on their difficulty
question_list_easy = []
question_list_medium = []
question_list_hard = []

for i in response_json['results']:
    new_question = Question(category = i['category'], q_type = i['type'], difficulty = i['difficulty'], question = i['question'],
                        correct_answer = i['correct_answer'], incorrect_answers= i['incorrect_answers'])
    
    if i['difficulty'] == 'easy':
        question_list_easy.append(new_question)
    elif i['difficulty'] == 'medium':
        question_list_medium.append(new_question)
    else:
        question_list_hard.append(new_question)

#with these instances of class Question, we can now create Quizzes.
    
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
        
    # NOTE: if you use a dictionary it would be easy to combine all the following three methods into one and providing "easy"/"medium"/"difficult" as a key to the method 
    def next_question_easy(self):
        try:
            current_question = self.question_list_easy[self.q_num_easy]
            self.q_num_easy += 1

            user_answer = input(f"{self.q_num_easy + self.q_num_medium + self.q_num_hard} {current_question.question} (True/False): ")        
            if self.check_answer(user_answer, current_question.correct_answer):
                self.difficulty_level = 2
        except IndexError:
            # NOTE: if the level 2 represents medium than you could represent this using e.g. an enum to make it easy to read
            self.difficulty_level = 2 #redirect to medium difficulty if we don't have any easy questions in dataset

    def next_question_medium(self):
        try:
            current_question = self.question_list_medium[self.q_num_medium]
            self.q_num_medium += 1

            user_answer = input(f"{self.q_num_easy + self.q_num_medium + self.q_num_hard} {current_question.question} (True/False): ")
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

            user_answer = input(f"{self.q_num_easy + self.q_num_medium + self.q_num_hard} {current_question.question} (True/False): ")
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
# NOTE: shouldn't this be coming from the user input?
number_questions_total = 5 #define how many questions we want to ask our user
quiz = Quiz(number_questions_total, question_list_easy, question_list_medium, question_list_hard)


while quiz.remaining_questions():
    # NOTE: see above this could be a single method quiz.next_question as the state of difficulty level is already kept by quiz and does not need to be exposed here
    if quiz.difficulty_level == 1:
        quiz.next_question_easy()
    elif quiz.difficulty_level == 2:
        quiz.next_question_medium()
    else:
        quiz.next_question_hard()   

print(f"Your final score is: {quiz.question_score}")

# NOTE: could wrap the whole program to allow to start another quiz after this round
# NOTE: additional features could be a score board, ...
