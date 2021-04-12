g = open("Question","w")

g.write('Question 1: How many colonies did the U.S. consist of\n')
g.write('a.  \n')
g.write('b.  \n')
g.write('c.  \n')
g.write('d.  \n')

g.close()
read = open("Questions", "r")
print(read.read(5))
answer_1 = "d"
question_1 = input()
if question_1 == answer_1:
  print(f"Congratulations you chose the correct answer of {answer_1}! Onto question 2!\n")
else:
  print(f"You chose the incorrect answer of {question_1}. The correct answer was{answer_1}. Onto question 2\n")




