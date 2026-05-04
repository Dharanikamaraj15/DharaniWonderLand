# def welcome():
#     print("Welcome to learn Functions")
# welcome()

# def add (a,b):
#     print(a+b)
# add(1,2)


# def add(a,b):
#     return a+b
# result = add(2,3)
# print(result)

 #Built in function.
# print("Dharani")
# name="Dharani"
# print(len(name))
# print(type(name))

#User Defined Functions

# def square(n):
#     return(n*n)
# print(square(3))

#Function Arguments: 
#Positional Arguments: 
# def greeting(name):
#     print("Hello", name)
# greeting("harani")

#Recursive function- A Function that calls itself again and again
def recursive(n):
   if n == 1:
       return 1
   return n * recursive(n-1)
print(recursive(5))