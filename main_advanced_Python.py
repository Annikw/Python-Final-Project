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



# --------------------------------OOP based approach for Questions and Quiz---------------------------------
'''
class Question:
    def __init__(self, category, q_type, difficulty, question, correct_answer, incorrect_answers):
        self.category = category
        self.type = q_type
        self.difficulty = difficulty
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers

'''




class Quiz:
    def __init__(self, number_questions_total, q_list_easy, q_list_medium, q_list_hard):

        self.number_questions_total = number_questions_total
        self.question_score = 0

        # NOTE: use a dictionary here (e.g. self.questions["easy"], ...)
        self.question_list_easy = q_list_easy  # list of easy questions
        self.question_list_medium = q_list_medium
        self.question_list_hard = q_list_hard

        # NOTE: use dictionary here, could even combine with above
        self.q_num_easy = 0  # counter for easy questions
        self.q_num_medium = 0
        self.q_num_hard = 0

        self.difficulty_level = 1  # 1 for easy, 2 for medium and 3 for hard



    # NOTE: if you use a dictionary it would be easy to combine all the following three methods into one and providing "easy"/"medium"/"difficult" as a key to the method
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

            if self.check_answer(user_answer, current_question[4]):
                self.difficulty_level = 2
        except IndexError:
            # NOTE: if the level 2 represents medium than you could represent this using e.g. an enum to make it easy to read
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


            if self.check_answer(user_answer, current_question[4]):
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

            if self.check_answer(user_answer, current_question[4]):
                self.difficulty_level = 3
            else:
                self.difficulty_level = 2
        except IndexError:
            self.difficulty_level = 1

    def remaining_questions(self):
        return ((self.q_num_easy + self.q_num_medium + self.q_num_hard) < self.number_questions_total)

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

        # ------------------------- Running the Quiz ---------------------------------


    def run_quiz(self):
        self.quiz = Quiz(NB_Questions, question_list_easy, question_list_medium, question_list_hard)
        while self.quiz.remaining_questions():
            # NOTE: see above this could be a single method quiz.next_question as the state of difficulty level is already kept by quiz and does not need to be exposed here
            if self.quiz.difficulty_level == 1:
                self.quiz.next_question_easy()
            elif self.quiz.difficulty_level == 2:
                self.quiz.next_question_medium()
            else:
                self.quiz.next_question_hard()

        print(f"Your final score is: {self.quiz.question_score}")

# code will start from here------------------
if __name__ == "__main__":
    # ----------------Creating dictionaries for Question settings-------------------------

    def Chosen_Category():
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

        # ----------------Designing the User interaction: choosing the category-----------------
        print("Hi, Welcome!")
        print("Here is the Menu:")
        # -----CATEGORY-----
        # Print the number and the category
        for i in Categories:
            print(i, Categories[i])
        # NOTE: can get rid of this variable and instead use a while true: with a break
        check_loop = True
        while check_loop:
            # Input Category
            # NOTE: use snake case (lower case beginning)
            Chose_Cat = 0
            # NOTE: validate that the user input is actually a number and recover if not
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
        # NOTE: better variable naming and move this all into a function
        NB_Questions = 0
        # Check valid input
        while NB_Questions < 1 or NB_Questions > 30:
            # NOTE: recover if not integer input
            NB_Questions = int(input('How many Questions ? (<30) '))
        print('\n')
        return NB_Questions


        # ----------------Cleaning data & Retrieving data from API based on user's choices-------------------------
        # Data cleaning
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

        #print(question_list_easy, question_list_medium, question_list_hard)

        return NB_Questions, question_list_easy, question_list_medium, question_list_hard


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


        #url = "https://opentdb.com/api.php?amount=10&category=18&type=boolean
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




    #print(question_list_easy[0])
# NOTE: could wrap the whole program to allow to start another quiz after this round
# @Sudanshu could you look into this?

# NOTE: add additional features: a timer? Showing the level of difficulty when asking a question? Something else?
# NOTE: Wrap code in a function and call it using if name == 'main'
# NOTE: Move classes to separate files
# @Sudanshu