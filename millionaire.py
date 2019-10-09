#EXTRA CREDIT
import random
random = random.randint(0,101)
# Who wants to be a Millionaire??
input("Welcome to Millionaire! What is your name? ")
print("Currently you have made $0")
# The progression in this "short" version of millionaire should be:

# Question One 
print("What is 1 + 1")
a1 = input("a. 1\nb. 2\nc. 3\nd. 4\ne. Phone a Friend\n>>")
if a1.lower() == "e" or a1.lower() == "Phone a Friend":
  if(random <= 85):
    print("Your instructor says the answer is b")
    print("What is 1+1 ? ")
    a1 = input("a. 1\nb. 2\nc. 3\nd. 4\ne. Phone a Friend\n>>")
  elif(random >= 86):
    print("What is 1+1? ")
    print("Your instrucor says the answer is either a, c, or d")
    a1 = input("a. 1\nb. 2\nc. 3\nd. 4\ne. Phone a Friend\n>>")
if a1.lower() == "b" or a1.lower() == "2":
  print("Correct")
  print("Currently you have made $500")
  print("Who is the 45th president of the United States?")
  a2 = input("a. Barack Obama\nb. Hillary Clinton\nc. Donald Trump\nd. Tom Brady\ne. Phone a Friend\n>>")
  if a2.lower() == "e" or a2.lower() == "Phone a Friend":
    if(random <= 85):
      print("Your instructor says the answer is c")
      print("Who is the 45th president of the United States?")
      a2 = input("a. Barack Obama\nb. Hillary Clinton\nc. Donald Trump\nd. Tom Brady\ne. Phone a Friend\n>>")
    elif(random >= 86):
      print("Who is the 45th president of the United States?")
      print("Your instrucor says the answer is either a, b, or d")
      a2 = input("a. Barack Obama\nb. Hillary Clinton\nc. Donald Trump\nd. Tom Brady\ne. Phone a Friend\n>>")
  if a2.lower() == "c" or a2.lower() == "donald trump":
    print("Correct")
    print("Currently you have made $1000")
    print("What is the capital of Michigan?")
    a3 = input("a. Detroit\nb. Lansing\nc. Los Angeles\nd. New York\ne. Phone a Friend\n>>")
    if a3.lower() == "e" or a3.lower() == "Phone a Friend":
      if(random <= 85):
        print("Your instructor says the answer is b")
        print("What is the capital of Michigan?")
        a3 = input("a. Detroit\nb. Lansing\nc. Los Angeles\nd. New York\ne. Phone a Friend\n>>")
      elif(random >= 86):
        print("What is the capital of Michigan?")
        print("Your instrucor says the answer is either a, c, or d")
        a3 = input("a. Detroit\nb. Lansing\nc. Los Angeles\nd. New York\ne. Phone a Friend\n>>")
    if a3.lower() == "b" or a3.lower() == "Lansing":
      print("Correct")
      print("Currently you have made $5000")
      print("What is 2 + 2?")
      a4 = input("a. 1\nb. 2\nc. 3\nd. 4\ne. Phone a Friend\n>>")
      if(random <= 85):
        print("Your instructor says the answer is d")
        print("What is 2 + 2?")
        a4 = input("a. 1\nb. 2\nc. 3\nd. 4\ne. Phone a Friend\n>>")
      elif(random >= 86):
        print("What is 2 + 2?")
        print("Your instrucor says the answer is either a, b, or c")
        a4 = input("a. 1\nb. 2\nc. 3\nd. 4\ne. Phone a Friend\n>>")
      if a4.lower() == "d" or a4 == "4":
        print("Correct")
        print("Currently you have made $20000")
        print("Where is Howard Univeristy located?")
        a5 = input("a. Virginia\nb. Maryland\nc. Washington DC \nd. Massachusetts\ne. Phone a Friend\n>>")
        if(random <= 85):
          print("Your instructor says the answer is c")
          print("Where is Howard Univeristy located?")
          a5 = input("a. Virginia\nb. Maryland\nc. Washington DC \nd. Massachusetts\ne. Phone a Friend\n>>")
        elif(random >= 86):
          print("Where is Howard Univeristy located?")
          print("Your instrucor says the answer is either a, b, or d")
          a5 = input("a. Virginia\nb. Maryland\nc. Washington DC \nd. Massachusetts\ne. Phone a Friend\n>>")
        if a5.lower() == "c" or a5.lower() == "Washington DC":
          print("Correct")
          print("Currently you have made $50000")
          print("What is 4+4? ")
          a6 = input("a. 16\nb. 5\nc. 4\nd. 8\ne. Phone a Friend\n>>")
          if a6.lower() == "e" or a6.lower() == "Phone a Friend":
            if(random <= 85):
              print("Your instructor says the answer is d")
              print("What is 4+4? ")
              a6 = input("a. 16\nb. 5\nc. 4\nd. 8\ne. Phone a Friend\n>>")
            elif(random >= 86):
              print("What is 4+4? ")
              print("Your instrucor says the answer is either a, b, or c")
              a6 = input("a. 16\nb. 5\nc. 4\nd. 8\ne. Phone a Friend\n>>")
          if a6.lower() == "d" or a6.lower() == "8":
            print("Correct")
            print("Currently you have made $250000")
            print("What smartphones have an apple on them?")
            a7 = input("a. Samsung\nb. Android\nc. Apple\nd. Google\ne. Phone a Friend\n>>")
            if(random <= 85):
              print("Your instructor says the answer is c")
              print("What smartphones have an apple on them?")
              a7 = input("a. Samsung\nb. Android\nc. Apple\nd. Google\ne. Phone a Friend\n>>")
            elif(random >= 86):
              print("What smartphones have an apple on them?")
              print("Your instrucor says the answer is either a, b, or d")
              a7 = input("a. Samsung\nb. Android\nc. Apple\nd. Google\ne. Phone a Friend\n>>")
            if a7.lower() == "c" or a7.lower() == "Apple":
                print("Correct")
                print("Currently you have made $500000")
                print("What animal is the mascot of the football team in Detroit?")
                a8 = input("a. Lions\nb. Tigers\nc. Bears\nd. OhMy\nPhone a Friend\n>>")
                if(random <= 85):
                  print("Your instructor says the answer is c")
                  print("What animal is the mascot of the football team in Detroit?")
                  a8 = input("a. Lions\nb. Tigers\nc. Bears\nd. OhMy\ne. Phone a Friend\n>>")
                elif(random >= 86):
                  print("What animal is the mascot of the football team in Detroit?")
                  print("Your instrucor says the answer is either a, b, or d")
                  a8 = input("a. Lions\nb. Tigers\nc. Bears\nd. OhMy\nPhone a Friend\n>>")
                if a8.lower() == "a" or a8.lower() == "Lions":
                  print("Correct")
                  print("Currently you have made $1000000")
                  print("You are a millionaire!")
                else:
                  print("I'm sorry, that is incorrect")
            else:
              print("I'm sorry, that is incorrect")
          else:
            print("I'm sorry, that is incorrect")
        else:
          print("I'm sorry, that is incorrect")
      else:
        print("I'm sorry, that is incorrect")
    else:
      print("I'm sorry, that is incorrect")
  else:
    print("I'm sorry, that is incorrect")
else:
  print("I'm sorry, that is incorrect")

# # Question Two


# # Question Three



# # Question Four



# # Question Five 


# #Question Six


#Question Seven



#Question Eight
