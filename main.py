print("------------------------------HISTORY TRIVIA GAME------------------------------")
print()
print("                          Created by Mitchell Marczak\n")
print()

print("The rules of this history trivia game are simple, answer using one of the options given, and have fun. All you need to do is put the letter for the answer you think is right, make sure not to use capitals. Good luck and have fun! Now let's get started!\n")
g = open("Questions","w")

g.write('Question 1: How many colonies did the U.S. consist of originally?\n')
g.write('a. 8  \n')
g.write('b. 12 \n')
g.write('c. 10 \n')
g.write('d. 13 \n')

g.write('Question 2: \n')
g.write('a.  \n')
g.write('b.  \n')
g.write('c.  \n')
g.write('d.  \n')

g.write('Question 3: \n')
g.write('a.  \n')
g.write('b.  \n')
g.write('c.  \n')
g.write('d.  \n')

g.write('Question 4: \n')
g.write('a.  \n')
g.write('b.  \n')
g.write('c.  \n')
g.write('d.  \n')

g.write('Question 5: \n')
g.write('a.  \n')
g.write('b.  \n')
g.write('c.  \n')
g.write('d.  \n')
g.close()

g = open("Answers", "w")
g.write("d\n")
g.write("c\n")
g.write("a\n")
g.write("d\n")
g.write("a\n")

g.close()
read = open("Answers", "r")
answer1 = read.read(1) 
answer2 = read.read(2)
answer3 = read.read(3)
answer4 = read.read(4)
answer5 = read.read(5)

read = open("Questions", "r")

#for i in range(0, 5):
  #print(read.readline())

for i in range(0, 5):
  print(read.readline())

correct_answers = 0
incorrect_answers = 0
question_1 = input()
print()

if question_1 == answer1:
  print(f"Your answer of {answer1} was correct!\n")
  correct_answers += 1
else:
  print(f"Your answer of {question_1} was incorrect! The correct answer was {answer1}!\n")
  incorrect_answers += 1

for i in range(0, 5):
  print(read.readline())

question_2 = input()
print()

if question_2 == answer2:
  print(f"Your answer of {answer2} was correct!\n")
  correct_answers += 1
else:
  print(f"Your answer of {question_2} was incorrect! The correct answer was {answer2}!\n")
  incorrect_answers += 1

for i in range(0, 5):
  print(read.readline())

question_3 = input()
print()

if question_3 == answer3:
  print(f"Your answer of {answer3} was correct!\n")
  correct_answers += 1
else:
  print(f"Your answer of {question_3} was incorrect! The correct answer was {answer3}!\n")
  incorrect_answers += 1

for i in range(0, 5):
  print(read.readline())

question_4 = input()
print()

if question_4 == answer4:
  print(f"Your answer of {answer4} was correct!\n")
  correct_answers += 1
else:
  print(f"Your answer of {question_4} was incorrect! The correct answer was {answer4}!\n")
  incorrect_answers += 1

for i in range(0, 5):
  print(read.readline())

question_5 = input()
print()

if question_5 == answer5:
  print(f"Your answer of {answer5} was correct!\n")
  correct_answers += 1
else:
  print(f"Your answer of {question_3} was incorrect! The correct answer was {answer5}!\n")
  incorrect_answers += 1









