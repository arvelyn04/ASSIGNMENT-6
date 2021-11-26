import random

yourScore=0
questions = {}

for i in range(10):
    int_a = random.randint(0,99)
    int_b = random.randint(0,99)
    operators = ['+']
    operator_value = random.choice(operators)
    question = str(int_a)+" "+operator_value+" "+str(int_b)
    answer = str(eval(question))
    question+=": "
    
    questions.update({question:answer})

for q in questions.keys():
    your_answer=input(q)
    if questions.get(q)==your_answer:
        print("CORRECT!")
        yourScore+=1
    else:
        print("INCORRECT!")

print("YOU GOT "+str(yourScore)+" CORRECT ANSWERS, GOOD JOB!")

