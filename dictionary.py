#List examples
# def who():
#     neighbours = ["Semenyo","Son","Njambi", "Hazy"]
#     print(neighbours)
#
# who()
#this has worked succesfully

#who are they- so we create a dictionary
#note the equals after defining the dictionary, the pairs are in quotes, the pairs en in commas
#the pairs are separated by full colons
myLife = {
    "Semenyo" : "Bournemouth",
    "Son": "Mali safi ya totte",
    "Njambi" : "Twin",
    "Hazy": "Roommate",
}
#if you want to access the dict, call on it. Len, type etc
#eg
# print(myLife)
# print(myLife["Njambi"])
# print(len(myLife))
# print(type(myLife))

#now if you want to append the list, use list.append, eg
# neighbours = ["Semenyo","Son","Njambi", "Hazy"]
# neighbours.append("Saruni")
# print(neighbours)

#that has worked well, now to the grading part

#now appending the dictionary
# myLife = {
#     "Semenyo" : "Bournemouth",
#     "Son": "Mali safi ya totte",
#     "Njambi" : "Twin",
#     "Hazy": "Roommate",
# }
# myLife["Morgan"] = "Shmoko"
# print(myLife)

# #getting into the grading bit
# student_Marks = {
#     "Mathematics" : 80,
#     "English" : 88,
#     "Kiswahili" : 90,
#     "Science" : 78,
#     "Social" : 70,
# }
# #to append in the dict do this
# student_Marks["CRE"]= 50
# print(student_Marks)
# #to get the subjects in the dictionary use a for clause
#
# for subjects in student_Marks:
#     print(subjects)
# #to print a single value this is how to call it
# print(student_Marks["Social"])
#
# #to print the marks in that dict, use another for clause
# for marks in student_Marks:
#     print(student_Marks[marks])


#getting into the grading bit
student_Marks = {
    "Mathematics" : 80,
    "English" : 88,
    "Kiswahili" : 90,
    "Science" : 78,
    "Social" : 70,
}
#to append in the dict do this
student_Marks["CRE"]= 50
print(student_Marks)
#to get the subjects in the dictionary use a for clause

for subjects in student_Marks:
    print(subjects)
#to print a single value this is how to call it
print(student_Marks["Social"])

#to print the marks in that dict, use another for clause
for marks in student_Marks:
    print(student_Marks[marks])

#now to getting the total, we first star by assigning total, a value of zeo. then the for loop using
#the for loop statement written will reiterate as it adds all the values
#in marks till it arrives at an answer

#here is the for loops statement

total = 0
for marks in student_Marks:
    total += student_Marks[marks]
print(total)

#you can also write it as
total = 0
for marks in student_Marks:
    total = total + student_Marks[marks]
print(total)
average = total/len(student_Marks)
print("The average is ",average)
#now to get the average value, we get the total and divide by the dictionary





