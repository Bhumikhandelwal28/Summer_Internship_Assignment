#  Enter the students detail
name=input(print("Enter the name of the student"))
student_class=int(input(print("Enter the class of the student")))

marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

total_marks = sum(marks)
percentage = (total_marks / 500) * 100

if percentage<23:
        print("fail")
elif percentage<50:
        print("average")
elif percentage<80:
        print("good")
else:
        print("Excellent")

# Display result
print("\n--- Student Result ---")
print(f"Name       : {name}")
print(f"Class      : {student_class}")
print(f"Percentage : {percentage:.2f}%")
