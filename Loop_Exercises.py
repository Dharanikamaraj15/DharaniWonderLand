# print("Program to print 1 to 20")
# n=1
# while(n<=10):
#     print(n)
#     n+=1

# print("Printing even numbers from 1 to 50 ")   
 
#Write a program to print even numbers from 1 to 50

# print("Program to print even numbers from 1 to 50 using FOR Loop")
# for num in range(1,51):
#     if num%2==0:
#         print(num)
    

# print("Program to print even numbers from 1 to 50 using while Loop")
# num=2
# while(num<=50):
#     print(num)
#     num+=2

#brea statement 
# for i in range(10):
#     if i == 5:
#         break
#    print(i)
#continue means it leaves that value and print other values.

# for i in range(6):
#    if i == 2:
#        continue
#    print(i)

#print("Count characters in the string Generative AI") -- not able to understand

# text= "Generative AI"
# for i in text:
#     i+=1
#     print(i)



        
# Write a program to print even numbers from 1 to 50 in python 

# for num in range(1, 51):
#     if num % 2 == 0:
#         print(num)

# using while print even numbers from 1 to 50 in python

# num = 2

# while num <= 50:
#     print(num)
#     num += 2

# Count characters in the string "Generative AI" using loops in python

# text = "Generative AI"
# count = 0

# for char in text:
#     count += 1

# print("Number of characters:", count)

#Create a number guessing loop in python 
print("Guessing number program")
secret_number = 2
while True:
    guess = int(input("Guess the number: "))

    if guess == secret_number:
        print("Correct! You guessed the number.")
        break
    else:
        print("Try again!")
        print("End than you!")