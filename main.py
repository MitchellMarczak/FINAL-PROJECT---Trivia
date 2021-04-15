print("------------------------------U.S. HISTORY TRIVIA GAME------------------------------")
print()
print("                            Created by Mitchell Marczak\n")
print()
print("The rules of this history trivia game are simple, answer using one of the options given, NO USING GOOGLE, and the final one is to have fun. All you need to do is put the letter (a, b, c, or d) for the answer you think is right, make sure not to use capitals. Good luck and have fun! Now let's get started!\n")
ready_check = input("Are you ready to get started? Answer 'yes' or 'no'.\n")
no = "no"
yes = "yes"
while ready_check != yes: 
  print("\nThe rules of this history trivia game are simple, answer using one of the options given, NO USING GOOGLE, and the final one is to have fun. All you need to do is put the letter (a, b, c, or d) for the answer you think is right, make sure not to use capitals. Good luck and have fun! Now let's get started!\n")
  ready_check = input("Are you ready to get started? (Answer 'yes' or 'no').\n")
  no = "no"
  yes = "yes"
  print()
g = open("Questions","w")

g.write('Question 1: What was the first state of the U.S.?\n')
g.write('a. Georgia\n')
g.write('b. New Jersey\n')
g.write('c. Connecticut\n')
g.write('d. Delaware\n')

g.write('Question 2: How many states were there in the U.S. during the civil war?\n')
g.write('a. 13\n')
g.write('b. 50\n')
g.write('c. 34\n')
g.write('d. 28\n')

g.write('Question 3: How many U.S. territories are there currently?\n')
g.write('a. 16\n')
g.write('b. 14\n')
g.write('c. 8 \n')
g.write('d. 19\n')

g.write("Question 4: What was the name of President Abraham Lincoln's wife? \n")
g.write('a. Mary Arthur  \n')
g.write('b. Martha Wayles \n')
g.write('c. Marian Dolley \n')
g.write('d. Mary Todd \n')

g.write('Question 5: Who created the national anthem (The Star-Spangled Banner) of the U.S.? \n')
g.write('a. John McHenry\n')
g.write('b. Francis Key\n')
g.write('c. John Smith\n')
g.write('d. Henry Key\n')
g.close()

g = open("Answers", "w")
g.write("d\n")
g.write("c\n")
g.write("a\n")
g.write("d\n")
g.write("b")
g.close()

read = open("Answers", "r")
answers_set = (read.read(1), read.read(1), read.read(1), read.read(1), read.read(1), read.read(1), read.read(1), read.read(1), read.read(1))

read = open("Questions", "r")
print()
#for i in range(0, 5):
  #print(read.readline())
possible_choices = {"a", "b", "c", "d"}
for i in range(0, 5):
  print(read.readline())

correct_answers = 0
incorrect_answers = 0
final_score = 0
users_answer = input("Your answer: ")
print()
if users_answer in possible_choices:
  if users_answer == answers_set[0]:
    print(f"Your answer of '{answers_set[0]}' was correct!\n")
    correct_answers += 1
  else:
    print(f"Your answer of '{users_answer}' was incorrect!\n")
    incorrect_answers += 1
else:
  print("You won't be able to redo this question this attempt, so choose an actual answer next time.\n")
  incorrect_answers += 1


for i in range(0, 5):
  print(read.readline())

users_answer = input("Your answer: ")
print()

if users_answer in possible_choices:
  if users_answer == answers_set[2]:
    print(f"Your answer of '{answers_set[2]}' was correct!\n")
    correct_answers += 1
  else:
    print(f"Your answer of '{users_answer}' was incorrect!\n")
    incorrect_answers += 1
else:
  print("You won't be able to redo this question this attempt, so choose an actual answer next time.\n")
  incorrect_answers += 1

for i in range(0, 5):
  print(read.readline())

users_answer = input("Your answer: ")
print()
if users_answer in possible_choices:
  if users_answer == answers_set[4]:
    print(f"Your answer of '{answers_set[4]}' was correct!\n")
    correct_answers += 1
  else:
    print(f"Your answer of '{users_answer}' was incorrect!\n")
    incorrect_answers += 1
else:
  print("You won't be able to redo this question this attempt, so choose an actual answer next time.\n")
  incorrect_answers += 1

for i in range(0, 5):
  print(read.readline())

users_answer = input("Your answer: ")
print()
if users_answer in possible_choices:
  if users_answer == answers_set[6]:
    print(f"Your answer of '{answers_set[6]}' was correct!\n")
    correct_answers += 1
  else:
    print(f"Your answer of '{users_answer}' was incorrect!\n")
    incorrect_answers += 1
else:
  print("You won't be able to redo this question this attempt, so choose an actual answer next time.\n")
  incorrect_answers += 1

for i in range(0, 5):
  print(read.readline())

users_answer = input("Your answer: ")
print()
if users_answer in possible_choices:
  if users_answer == answers_set[8]:
    print(f"Your answer of \"{answers_set[8]}\" was correct!\n")
    correct_answers += 1
  else:
    print(f"Your answer of '{users_answer}' incorrect!\n")
    incorrect_answers += 1
else:
  print("You won't be able to redo this question this attempt, so choose an actual answer next time.\n")
  incorrect_answers += 1

final_score = (correct_answers/(correct_answers + incorrect_answers) * 100)
print("                                       All Done!                              ")
print(f"                            Your final score was a {final_score}%!")  
print('               You got %d questions correct and %d questions incorrect!' % (correct_answers, incorrect_answers))
print("")
print("                       I hope you enjoyed! Thanks for playing!\n ")
print("                             Created by Mitchell Marczak")
