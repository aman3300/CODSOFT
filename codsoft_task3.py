# This is a simple quiz game program.
ini = 0 #initial value incase if user want to play again
for i in range(5):
    print("Do You Want To Play?\n")
    print("1.Yes")
    print("2.No")
    temp = int(input()) #takes user input if he wants to play
    if temp ==1:
        score = 0  #Initial Score is 0.
        print("score currently is: \n", score)
        print("********Each Correct Answer Increase Score By 5********")
        for x in range(5):
            if x == 0:
                print("Which school did Harry Potter attend?:")
                print("1.Hogwart")
                print("2.HighImpact")
                print("3.Sacred Heart Academy")
                print("4.Nexus Academy")
                a = int(input())
                if a == 1:  #1 is correct answer
                    print("Correct answer.")
                    score = score+5   #Each correct answer increase score by 5.
                    print ("********Score is", score)
                else:
                    print("OOPS! Wrong answer")
                    ("Score is:",score)
                    print("********Score is:",score)
                    print("Correct Answer is: Hogwart")  #Prints the correct answer if user choose wrong answer
            
            elif x == 1:  #second question
                print("Harry Potter Middle Name Is what:")
                print("1.Michael")
                print("2.Davidson")
                print("3.James")
                print("4.Julian")
                a = int(input())
                if a == 3:  # 3 is correct answer
                    print("Correct answer.")
                    score = score+5
                    print ("********Score is", score)
                else:
                    print("OOPS! Wrong answer")
                    print("********Score is:",score)
                    print("Correct Answer is: James")  #Prints the correct answer if user choose wrong answer
                
            elif x == 2:  #third question
                print("Who was Harry Potter's pet?:")
                print("1.Dog")
                print("2.Owl")
                print("3.Cat")
                print("4.Monkey")
                a = int(input())
                if a == 2:  # 2 is correct answer
                    print("Correct answer.")
                    score = score+5
                    print ("********Score is", score)
                else:
                    print("OOPS! Wrong answer")
                    print("********Score is:",score)
                    print("Correct Answer is:Owl") #Prints correct answer if user chooses wrong one
            elif x == 3:  #Fourth question
                print("Where did Olympics originally start:")
                print("1.China")
                print("2.USA")
                print("3.Spain")
                print("4.Greece")
                a = int(input())
                if a == 4:  # 4 is correct answer
                    print("Correct answer.")
                    score = score+5
                    print ("********Score is", score)
                else:
                    print("OOPS! Wrong answer")
                    print("********Score is:",score)
                    print("Correct Answer is:Greece") #Prints correct answer if user chooses wrong one

            elif x == 4:  #Fifth question
                print("What organ does snakes use to Smell?:")
                print("1.Nose")
                print("2.Tongue")
                print("3.Cheeks")
                print("4.Teeth")
                a = int(input())
                if a == 2:  # 2 is correct answer
                    print("Correct answer.")
                    score = score+5
                    print ("********Score is", score)
                else:
                    print("OOPS! Wrong answer")
                    print("********Score is:",score)
                    print("Correct Answer is:Tongue") #Prints correct answer if user chooses wrong one


    else:
        print("Have a Good Day!!")
        break; #Breaks the playing loop if user wants to exit