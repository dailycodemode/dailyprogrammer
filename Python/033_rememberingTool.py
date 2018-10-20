# # Answer by Daily Code Mode
# from random import randint
#
# def rememberGame(question_list, answer_list):
#     correct_answer = False
#     while 1 != 2:
#         rand_num = randint(0, len(question_list) -1 )
#         while correct_answer == False:
#             print(question_list[rand_num])
#             answer = input()
#             if answer == "exit":
#                 print("Exit")
#                 break
#             if answer == answer_list[rand_num]:
#                 correct_answer = True
#                 print("CORRECT")
#
# rememberGame(["Answer for everything", "Name of blog", "Persoinality"],
#              ["Python", "Daily Code Mode", "Restatement"] )
#
# # Answer by magwhich
# import random
# answers=["42","nope"]
# questions=["what is the meaning of life the universe and   everything?","corn"]
# y_a= ""
# rando = random.randint(0,(len(questions)-1))
#
# while y_a != "exit":
#     print(questions[rando])
#     y_a=input("please enter your ansewer: ")
#     if y_a == answers[rando]:
#         print("sucess")
#         rando = random.randint(0,len(questions))
#     else :
#         print("fail")
#         rando = random.randint(0,len(questions))
#
# # Breakdown
# random.randint(0,(len(questions)-1))
# # This will give you a random number between two integers
#
#
# # Summary
# # very similar answers.