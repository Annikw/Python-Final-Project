from unicodedata import category
import requests
import random

#----------------Data cleaning-------------------------
'''
Create functions for data cleaning
'''
#define function that automatically replaces multiple substrings in string
def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

#define dictionary that takes the to-be replaced string as key and the replacements as values
replacement_values = {"#quot;": "'", "quot;": "'", "#039;": "'", "039;": "'"}

#iterate through response data and clean all questions
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


"""
#----------------Creating dictionaries for all possible Question settings-------------------------
''' the dictionaries will allow the user to choose the category, difficulty and question type of the questions in the quiz
'''

#Dictionary for the categories
Categories = {0 : "Random", 9 : 'General Knowledge', 10 : 'Entertainment: Books', 11: 'Entertainment: Film', 12 : 'Entertainment: Music',
        13 : 'Entertainment: Musicals & Theatres', 14: 'Entertainment: Television', 15:'Entertainment: Video Games', 16 :'Entertainment: Board Games',
        17 : 'Science & Nature', 18:'Science: Computers', 19: 'Science: Mathematics', 20 : 'Mythology', 21 : 'Sports', 22: 'Geography',
        23 : 'History', 24 : 'Politics', 25 : 'Art', 26:'Celebrities', 27 : 'Animals', 28 : 'Vehicles', 29 :  'Entertainment: Comics',
        30 : 'Science: Gadgets', 31: 'Entertainment: Japanese Anime & Manga', 32 : 'Entertainment: Cartoon & Animations'}

#Dictionary for the difficulty
Difficulty = {1: "easy", 2: "medium", 3: "hard"}

#Dictionary for the type: Allows the user to type 1 or 2, and will user the other dict to format the answer for the URL
Type1 = {1 : "True/False", 2 : "Multiple"}
Type = {"True/False" : "boolean", "Multiple" : "multiple"}

#----------------Designing the User Interaction-------------------------
'''In this section, we are asking the user to give input in terms of categories, difficulty, number of questions, and type of question to allow
the user to create a customized test design.
Choices are saved into variables'''

print("Hi, Welcome!")

print("Here is the Menu:")

#----------------CATEGORY------------

#Print the number and the category
for i in Categories:
    print(i, Categories[i])

check_loop = True
while check_loop:
    #Input Category
    Chose_Cat = 0
    Chosen_Cat = int(input("Please, input here a (valid) number for a category: "))
    #Check valid category
    try:
        print('You have chosen :', Categories[Chosen_Cat])
        check_loop = False
    except:
        check_loop = True

print('\n')

#----------------DIFFICULTY------------
print('Great, which difficulty ? ')
for i in Difficulty:
    print(i, Difficulty[i])

#Check valid input
check_loop = True
while check_loop:
    Chosen_Diff = int(input("Please, input here a valid number for a difficulty: "))
    try:
        print('You have chosen :', Difficulty[Chosen_Diff])
        check_loop = False
    except:
        check_loop = True

print('\n')

#----------------NB QUESTIONS------------
NB_Questions = 0
#Check valid input
while NB_Questions < 1 or NB_Questions >50:
    NB_Questions = int(input('How many Questions ? (<50) '))

print('\n')

#----------------TYPE------------
print('Finally, which type ? ')
for i in Type1:
    print(i, Type1[i])

#Check valid input
check_loop = True
while check_loop:
    Chosen_type = int(input("Please, input here a valid number for a difficulty: "))
    try:
        print('You have chosen :', Type[Type1[Chosen_type]])
        check_loop = False
    except:
        check_loop = True


print('\n')
print("Your", str(Difficulty[Chosen_Diff]), str(NB_Questions), "quizz about", str(Categories[Chosen_Cat]), "is about to start.")


#----------------Retrieving data from API based on user's choices-------------------------

url = "https://opentdb.com/api.php?amount="+str(NB_Questions)+ "&category=" + str(Chosen_Cat) + "&difficulty=" + str(Difficulty[Chosen_Diff]) +"&type=" + str(Type[Type1[Chosen_type]])

response = requests.get(url)

Score = 0

#Check that we have enough questions for the constrains
#(Sometimes, the API doesn't generate any questions: e.g. Cat:27, Questions:40, Level: Hard, Type: Multiple)


#--------------------------------Non OOP based approach-------------------------
#Q from Annik: what happens if the number of questions is equal to the length of the response??

if len(response.json()['results']) == 0:
    print("Sorry, we don't have any question with these requirments .. ")
    # --> When OOP, makes it redirect the user to the "form" class, where the user input it's choices
else:
    if len(response.json()['results']) < NB_Questions:
        print("Sorry, there are only", len(response.json()['results']), "available.. Let's start anyway!")
        NB_Questions = len(response.json()['results'])

    for i in range(NB_Questions):
        print(response.json()['results'][i]['question'])
        list_answers = []
        list_answers.append(response.json()['results'][i]['correct_answer'])
        for j in response.json()['results'][i]['incorrect_answers']:
            list_answers.append(j)
        list_answers = random.sample(list_answers, len(list_answers))


        #4 options if multiple choice
        if int(Chosen_type) == 2:
            keys_dict_multiple = [1, 2, 3, 4]
            questions_dict = {1: str(list_answers[0]), 2: str(list_answers[1]), 3: str(list_answers[2]), 4: str(list_answers[3])}

        #2 options if True/False
        elif int(Chosen_type) == 1:
            keys_dict_boolean = [1, 2]
            questions_dict = {1: str(list_answers[0]), 2: str(list_answers[1])}


        for question in questions_dict:
            print(question, questions_dict[question])

        answered = input("Input the number corresponding to the answer: ")

        if questions_dict[int(answered)] == response.json()['results'][i]['correct_answer']:
            print("correct answer")
            Score += 1
            print("Current Score: ", Score,"/",(i+1))
        else:
            print("Wrong answer, the correct asnwer was: ", response.json()['results'][i]['correct_answer'])
            print("Current Score: ", Score, "/", (i + 1))


    print("\n")
    print("You final score is:", Score,"/",(NB_Questions), "or", (Score/NB_Questions)*100,"%" )


"""
#--------------------------------OOP based approach try-out------------
'''Note from Annik: here we could also try to always extract a mix of difficulties from the API by selecting 'Any difficulty' 
This way, based on whether the previous answer was right or wrong --> the next question could have a different difficulty (the professor proposed
this when talking to him in class)'''

'''
Note from Wilm:
The quiz is now automatically adjusting difficulty based on the previous answer. 
I think it might be easiest if we only take True/False questions. That would make the coding part easier with only minor 
reduction in functionality, since we will never actually use the quiz in real life.
We should keep in mind that we now need a much larger set of questions, since we have to adjust to their skill level. The current code
automatically redirects the user to a different difficulty level if we run out of questions for any one difficulty. 

'''

#download test data
url = "https://opentdb.com/api.php?amount=10&type=boolean" #10 True/False questions of any difficulty
response = requests.get(url)
response_json = response.json()


#clean data
clean_dataset(response_json) 

#here we are creating a class for all the questions, not sure whether it will be necessary but it is quite easy and might make it easier to work with Quiz class after? 
#@Wilm feel free to change though
class Question:    
    def __init__(self, category, q_type, difficulty, question, correct_answer, incorrect_answers):        
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
    def __init__(self, number_questions_total, q_list_easy, q_list_medium, q_list_hard):
        
        self.number_questions_total = number_questions_total
        self.question_score = 0
        
        self.question_list_easy = q_list_easy #list of easy questions
        self.question_list_medium = q_list_medium
        self.question_list_hard = q_list_hard
    
        self.q_num_easy = 0 #counter for easy questions
        self.q_num_medium = 0
        self.q_num_hard = 0
        
        self.difficulty_level = 1 #1 for easy, 2 for medium and 3 for hard
        
    def next_question_easy(self):
        try:
            current_question = self.question_list_easy[self.q_num_easy]
            self.q_num_easy += 1

            user_answer = input(f"{self.q_num_easy + self.q_num_medium + self.q_num_hard} {current_question.question} (True/False): ")        
            if self.check_answer(user_answer, current_question.correct_answer):
                self.difficulty_level = 2
        except IndexError:
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



#q_list would either represent the objects from class questions OR just the response['results'] directly --> to be checked (EDIT WILM: Using instances of class Questions) 

# we can probably use some of the functions from here https://towardsaws.com/how-to-create-a-quiz-program-using-python-object-oriented-programming-concept-oops-62eaa639343b
        
        

#---------- Run the Quiz --------------
number_questions_total = 5 #define how many questions we want to ask our user
quiz = Quiz(number_questions_total, question_list_easy, question_list_medium, question_list_hard)


while quiz.remaining_questions():
    if quiz.difficulty_level == 1:
        quiz.next_question_easy()
    elif quiz.difficulty_level == 2:
        quiz.next_question_medium()
    else:
        quiz.next_question_hard()   

print(f"Your final score is: {quiz.question_score}")
