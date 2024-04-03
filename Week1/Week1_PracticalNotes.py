#Week 1 Python Notes

print("This returns text or a variable")

help(print) #Get a help page about the item

print(f"x / y = {(x/y)}") # Uses a f string literal, which means value is between {} and the rest is text

variable[-1] #Last value
variable[-2] #Second last value

variableName.find('l') #Finds the first instance of l in the string
variable = "Hello" * 5 #Returns five hellos

#A splice of a list is itself a list so we can have the index of a new list given after the inital splice as well as a letter index if needed
fruits[2:-1][0][-1]

#Method is function that acts directly on an object
print(topic.count("i"))

#Creating our own functions
def cat_twice(str1, str2):
   cat = str1 + str2
   print(cat) # this is part of the function
   print(cat) # this is part of the function
   
def circle_area(radius):
    area = pi * radius ** 2 # calculate the area of the circle using the radius argument
    return area # use return to get a value back from the function
    
    