# key={'shambhu','ritik',"aryan"}
# values={'3','5','8'}
# data=dict(zip(key,values))
# print(data)
# data['harsh']='9'
# print(data)
# print("hello world")
# print("helloworld\t"*5)
# dict1={"ritik":"45",
#        "shambhu":"13",
#        "harsh":'1',
#        "aryan":"8"}
# a=input("enter word: ")
# print(dict1["ritik"])
# list=[5,6,8,3]
# print(6 in list)
# if 9 in list:
#     print("yes in list")
# else:
#     print("not in list")
# a=int(input("enter your age: "))
# if a in range(5,80):
#     print("you can drive")
# elif a==18:
#     print("first you come  we check your driving")
# else:
#     print("you can't drive")


# reading for loops
# list1=["sham","ritik","aryan","harsh"]
#we can also do this by tuples
# list1=("sham","ritik","aryan","harsh")
#we can also do this by tuples of tuples
# list1=[["ritik",2],["sham",3],["harsh",4],["aryan",5]]
# print(list1)this is print elements in a line whit brackets.
# print(list1[0],list1[1],list1[2],list1[3])this is also print element in a line wihtout a bracket.
# for item in list1:
#     print(item)
# items=[int,float,"ritik",3,5,7,3,6,7,566,7,55]
# for item in items:
#     if str(item).isnumeric() and item>=6:
#         print(item)
#for while loop
# a=int(input("enter a number of cholate: "))
# i=1
# while i<=a:
#     print(i)
#     i=i+1
# print("finish toffi")
#i=0
# while(True):
#     if i+1<5:
#         i=i+1
#         continue
#     print(i+1, end=" ")
#     if(i==44):
#         break
#     i=i+1

          # use of while whith break and continue

# while(True):
#     a = int(input("Enter a number: "))
#     if a>100:
#         print("congrats you type more than 100")
#         break
#     else:
#         print("try again!")
#         continue
#a=int(input("enter 1st number: "))
#b=int(input("enter 2nd number: "))
# try:
#     print("The sum of these two number is",
#           a+b)
# except Exception as e:          @$#This is valid only for e word@#$%!
#     print(e)
#
#
# print("The line is  very important")

# File IO Basics
"""
"r"-open file for reading.
"w"-open file for writing.
"x"-creates file if not exists
"a"-add more content to a file.
"t"-text mode
"b"-binary mode
"+"-read and writeu

"""
# n=18
# number_of_quesses=1
# print("Number of guesses is limited only 9 times: ")
# while (number_of_quesses<=9):
#     quess_number = int(input("Guess the number: "))
#     if quess_number<18:
#         print("You enter less number please inter grater number.")
#     elif quess_number>18:
#         print("You enter greater number please inter less number.")
#     else:
#         print("You win.")
#         print(number_of_quesses,"no of quesses  goes to be finished.")
#         break
#     print(9-number_of_quesses,"no.of guesses left")
#     number_of_quesses=number_of_quesses+1
#
# if(number_of_quesses>9):
#     print("game over")

# n=18
# i=1
# print("Number of guesses is limited only 9 times:")
# while (i<=9):
#     a = int(input("Guess the number: "))
#     if a<18:
#         print("You enter less number please inter grater number.")
#     elif a>18:
#         print("You enter greater number please inter less number.")
#     else:
#         print("You win.")
#         print(i,"no of guesses you took to find a number.")
#         break
#     print(9-i,"no.of guesses left")
#     i=i+1
#
# if(i>9):
#     print("game over")

# f=open("ritik.txt","w")
# a=f.write("I am a good boy\n")     !@#$for open a file!@##@#
# print(a)
# f.close()
# a="i am a good boy"
# print(len(a))        # for no of length !@#


#for read and write both#
# f=open("ritik.txt","r+")
# print(f.read())
# f.write("Thank you")  #we can write in file#