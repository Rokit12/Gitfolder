Print("This is git information")
#The FOR loop
# fruits = ["mangoes", "oranges", "grapes"]
# for fruit in fruits:
# 	print(fruit)


# for letter in 'fruits':
# 	print(letter)


# list = ["book", "self", "chair"]
# Using else statement with a FOR loop
# num = []
# for num in range(10, 20):
# 	for i in range(2, num):
# 		if num%i == 0:
# 			x = num/i 
# 			print(num, i, x)
# 			break
# 		else:
# 			print(num)
# 			break


# # Indexing and slicing([])
# fruits = ["orange", "apple", "grapes", "banana"]
# print(fruits[0])
# # Indexing
# print(fruits.index('orange'))

# # # Quiz:
# # # Find the index value(position value) of "Grapes"
# # print(fruits.index('grapes'))
# # print(fruits[-2])


# #Tuples
# fruits = ("oranges", "grapes", "apples")
# print(fruits)

# #Type 2 tuple
# list = ("chair", "table", 97, 56, 1990)
# print(list)

# #Type 3 tuple
# items = "bank", "school", "bus"
# print(items)

# # Accessing values in tuples
# list = ("chair", "table", 97, 56, 1990)
# print(list[3])

# Quiz:
# Access the value in position 2 and result the info
# print(list[2])

# Not Update, not changing but assigning new tuple
# items = "bank", "school", "bus"
# list = ("chair", "table", 97, 56, 1990)
# items_total = items + list
# print(items_total)

#Deleting a tuple 
# commodities = ("chair", "table", 97, 56, 1990)
# print(commodities)
# del commodities
# print(commodities)



#Python dictionaries
# dict = {"name": "Antony", "age": 27, "shop": "rice"}
# print(dict)


#Accessing Values in Dictionary
# dict = {"name": "Antony", "age": 27, "shop": "rice"}
# print("The age of Antony is: ", dict['age'])

#Updating a dictionary
# dict = {"name": "Antony", "age": 27, "shop": "soap"}
# dict['age'] = 44
# dict['shop'] = 'rice'
# print("We have updated the dictionary successfully: ", dict)

#Deleting a dictionary element
dictionary = {"name": "Antony", "age": 27, "shop": "soap"}
# #Remove a single element first
# # del dictionary
# print(dictionary)


# #Adding items in a dictionary !!!!
# dictionary = {"name": "Antony", "age": 27, "shop": "soap"} 
# dictionary['travel'] = 'Masai mara'
# print(dictionary)

# #While infinite loop
# num = 1
# while num == 1:
# 	num = input("Enter a number :")
# 	print("You entered", num)

# count = 0
# while count < 5:
# 	print(count)
# 	count += 1
# else:
# 	print(count)

# flag = 1
#Dictionary
# dictionary = {"name": "Antony", "age": 27, "shop": "soap"}
# dictionary['Household'] = "Chair"
# # print(dictionary)
# #For loop in a dictionary
# for key, value in dictionary.items():
# 	print("{} is {}".format(key, value))





#write a file in python
# f = open("session.txt", "w")
# f = open()
# f.write("Hello Class \n")
# f.writelines("This is a python Class")

#Read data in a .txt file
# f = open("session.txt", "r")
# print(f.readlines())
# f.seek()
# print(f.read(10))

#Append(adding the content in that file) texts in the file
# f = open("session.txt", "a") #append mode
# f.write("Today is the session \n")
# f.close



#while loop statement
# count = 0
# while count < 20:
# 	print(count)
# 	count += 1

# count = 0 
# while count < 20:
# 	print(count, "is less than 20")
# 	count += 1
# else:
# 	print(count, "It is not less than 20")

#Single statement
# num = 5 
# while (num):
#  print("This is a single statement")
# print("This is not right")
# .upper() #Uppercase command
# .lower() #lowercase command
# .append() # append content
# .len() #length

#The length

# name = "Antony"
# print(name.upper())

# asset = "Schooling"
# print(len(asset))

#Append() 
# fruits = ["mangoes", "banana", "oranges"]
# fruits.append("apples")
# print(fruits)

#Boolean values determines whether a statement is True or False
# print(10 > 9) # True or False
# print(10 == 9)

# a = 115
# b = 20

# # if b > a:
# # 	print("b is greater than a")
# # else:
# # 	print("b is not greater than a")



# #Args and kwargs
# # result = 0 # This is the global variable

# # def add(a, b, c):
# # 	result = a + b + c #This is the local variable
# # 	print(result)
# # 	return result
# # add(10, 20, 30)

# #Python classes
# # fruits = ["oranges", "mangoes", "apples"]
# # integers = 1, 2, 3
# # print(type(fruits))
# # print(type(integers))

# #Classes
# # class Cat:
# # 	def meow(self):
# # 		print("meow")

# # c = Cat()
# # print(c)

# # __init__() Function
# # class Population:
# # 	def __init__(self, names, age):
# # 		self.names = names
# # 		self.age = age

# # person1 = Population("John", 28)
# # person2 = Population("Naomi", 29)
# # print(person1.names)
# # print(person1.age)

# # __init__() function

# class School:
# 	def __init__(self, name, age, grade):
# 		self.name = name 
# 		self.age = age
# 		self.grade = grade

# 	def get_grade(self):
# 		return self.grade

# class Course:
# 	def __init__(self, name, max_students):
# 		self.name = name
# 		self.max_students = max_students
# 		self.students = []

# 	def sum_student(self, student):
# 		if len(self.students) < self.max_students:
# 			self.students.append(student)
# 			return True
# 		return False

# 	def get_average(self):
# 		value = 0
# 		for student in self.students:
# 			value += student.get_grade()
# 		return value / len(self.students)

# st1 = School("Ann", 20, 80)
# st2 = School("Kelvin", 30, 70)
# st3 = School("Mark", 29, 40)
# st4 = School("Naomi", 28, 75)

# course = Course("Mathmatics", 3)
# course.sum_student(st1)
# course.sum_student(st2)
# # print(course.students[0].age)
# print(course.get_average())



#Assert statements
def get_average(scores):
	assert len(scores) != 0, "List is Empty"
	return sum(scores) / len(scores)

score2 = [84, 24, 44, 66]
print("Average of score2: ", get_average(score2))

score1 = []
print("Average of score1: ", get_average(score1))

#INIT








