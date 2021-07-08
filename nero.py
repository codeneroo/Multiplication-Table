'''
num = 5
for i in range(1, 11):
	print(num, "x", i, "=", num*i)
print("Thanks for playing") 
'''
import random
print("\n ************** Multiplication Practice Application ****************\n")
question_number = int(input("How many questions do you want? "))
qna = []
correct = 0
i = 0
while i < question_number:
	num1 = random.randint(1,11)
	num2 = random.randint(1,11)
	print(num1, "x", num2, "=")
	answer = int(input())
	actual_answer = num1*num2

	
	if answer == actual_answer:
		correct +=1
	else:
		qna.append(" ".join((str(num1), "x", str(num2), "=", str(actual_answer))))
	i += 1


for i in qna:
	print('The correct answers were: ', i)
print("\nThanks for playing this game!") 
print("\nThe number of correct answers were ", correct,"!")
print("\nThe % "+"of correct answers were", correct*100/question_number,"%")