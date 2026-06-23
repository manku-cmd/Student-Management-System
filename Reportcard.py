# information
# name
while True:
    name = input("Enter your name: ")
    if name == "":
        print("Name not provided")
    elif name.isalpha():
        print("Name:", name)
        break
    else:
        print("Name should be in alphabets only")
#  rollno.
while True:
    rollno = input("Enter your roll number: ")
    if rollno == "":
        print("Roll number not provided")
    elif not rollno.isnumeric():
        print("Roll number should be in numerics only")
    elif int(rollno) > 100 or int(rollno) < 1:
        print("Roll number should be between 1 to 100")
    elif rollno.isnumeric():
        print("Roll number:", rollno)
        break
    else:
        print("Roll number should be in numerics only")
# class        
while True:
    class_name=input("Enter your class: ")
    if class_name=="":
        print("Class not provided")
    elif not class_name.isdigit():
        print("Class should be in numerics only")
    elif int(class_name) < 1 or int(class_name) > 12:
        print("Class should be between 1 to 12")
    elif class_name.isdigit():
        print("Class:", class_name)
        break
    else:
        print("Class should be in numerics only")
# section
while True:
    section=input("Enter your section: ")
    if section=="":
        print("Section not provided")
    elif not section.isalpha():
        print("Section should be in alphabets only")
    elif len(section) != 1 or not section.isalpha() or not section.isupper():
        print("Section should be a single uppercase letter")
    elif section < "A" or section > "Z":
        print("Section should be between A to Z and in uppercase")
    elif section.isalpha() and section.isupper():
        print("Section:", section)
        break
    else:
        print("Section should be in alphabets only")
# subjects
subjects = ["Math", "Science", "English", "Computer", "Hindi"]
marks = []

i = 0
while i < len(subjects):

    mark = input(f"Enter marks for {subjects[i]}: ")

    if mark == "":
        print("Marks not provided")

    elif not mark.isnumeric():
        print("Marks should be in numerics only")

    elif int(mark) < 0 or int(mark) > 100:
        print("Marks should be between 0 to 100")

    else:
        marks.append(int(mark))
        print("Marks:", mark)
        i += 1
# total marks
total_marks = sum(marks)
print("Total Marks:", total_marks)
percentage = (total_marks / len(subjects))
print("Percentage:", round(percentage, 2), "%")
# grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"
print("Grade:", grade)
#  report card
print("\n===== REPORT CARD =====")
print("Name:", name)
print("Roll No:", rollno)
print("Class:", class_name)
print("Section:", section)
result = "Pass"
# displaying marks
for i in range(len(subjects)):
    status = "Pass"
    if marks[i] < 33:
        status = "Fail"
        result = "Fail"

    print(subjects[i], ":", marks[i], "-", status)

print("------------------------")
print("Total:", total_marks, "/500")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Final Result:", result)
print("========================")