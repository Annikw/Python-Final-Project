import requests
import random


#Dictionary for the categories
Categories = {0 : "Random", 9 : 'General Knowledge', 10 : 'Entertainment: Books', 11: 'Entertainment: Film', 12 : 'Entertainment: Music',
        13 : 'Entertainment: Musicals & Theatres', 14: 'Entertainment: Television', 15:'Entertainment: Video Games', 16 :'Entertainment: Board Games',
        17 : 'Science & Nature', 18:'Science: Computers', 19: 'Science: Mathematics', 20 : 'Mythology', 21 : 'Sports', 22: 'Geography',
        23 : 'History', 24 : 'Politics', 25 : 'Art', 26:'Celebrities', 27 : 'Animals', 28 : 'Vehicles', 29 :  'Entertainment: Comics',
        30 : 'Science: Gadgets', 31: 'Entertainment: Japanese Anime & Manga', 32 : 'Entertainment: Cartoon & Animations'}

#Dictionary for the categories
Difficulty = {1: "easy", 2: "medium", 3: "hard"}

#Dictionary for the type: Allows the user to type 1 or 2, and will user the other dict to format the answer for the URL
Type1 = {1 : "True/False", 2 : "Multiple"}
Type = {"True/False" : "boolean", "Multiple" : "multiple"}



print("Hi, Welcome!")

print("Here is the Menu:")


#Print the number and the category
for i in Categories:
    print(i, Categories[i])

#----------------CATEGORY------------
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


url = "https://opentdb.com/api.php?amount="+str(NB_Questions)+ "&category=" + str(Chosen_Cat) + "&difficulty=" + str(Difficulty[Chosen_Diff]) +"&type=" + str(Type[Type1[Chosen_type]])

response = requests.get(url)

Score = 0

#Check that we have enough questions for the constrains
#(Sometimes, the API doesn't generate any questions: e.g. Cat:27, Questions:40, Level: Hard, Type: Multiple)

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