# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: ")) #added int( since input is marks

exam_3 = int(input("Input exam grade three: ")) #changed str to int since its marks
#all input marks should be int since we are doing calculations with it

grades = [exam_one, exam_two, exam_3] #seperated values with commas and changed three to 3 as per above name
avg = 0 #sum is a built in function so changed name to avg
for grade in grades: #list name is grades so added s
  avg = avg + grade  #changed sum to avg just like above

avg = avg / len(grades) #sum to avg, grdes to grades

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90: #added colon
    letter_grade = "B"
elif avg >= 70 and avg < 80: #changed > to >=, 69 to 70
    letter_grade = "C"  #quotes should be same
elif avg >= 60 and avg < 70: #no.s & operators changed
    letter_grade = "D"
else:  #elif chnaged to else since its last condition
    letter_grade = "F"

print("Exam: ", end='')  #Changed these 2 lines to display like sample given above
print(*grades, sep=',')
print("Average:", int(avg)) #str changed to int to display like sample
print("Grade: " + letter_grade)

if letter_grade is "F": #- changed to _ as per name above
    print ("Student is failing.") #brackets added
else:
    print ("Student is passing.") #brackets added
