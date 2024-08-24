#write a program that calculate and display the looop...
#given numberic score (eg A,B,c, d, f)
#multiple condition if,elif,else,
#input the score from the user
#display the corresponding grade
#A = 90-100, B= 80-89, C= 70-79, D= 60-69, F= below 60/ 0-59
#step1: logic building
#input, score, float, output will string,
score = float(input("Enter your score: "))
#step 2: >=90 and <=100 A
#step 3: >=80 and <=89 B
#step 4: >=70 and <=79 C
#step 5: >=60 and <=69 D
#step 6: <60 F
if score >= 90 and score <= 100:
    print("Your grade is A")
    #step 7: elif score >= 80 and score <= 89:
elif score >= 80 and score <= 89:
    print("Your grade is B")
    #step 8: elif score >= 70 and score <= 79:
elif score >= 70 and score <= 79:
    print("Your grade is C")
    #step 9: elif score >= 60 and score <= 69:
elif score >= 60 and score <= 69:
    print("Your grade is D")

elif score >=0 and score <= 59:
    print("Your grade is F")
    #step 10: else:
else:
    print("invalid score")

