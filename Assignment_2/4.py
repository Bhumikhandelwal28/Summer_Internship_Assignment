#  Enter the students detail
name=input(print("Enter the name of the student"))
student_class=int(input(print("Enter the class of the student")))

marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

total_marks = sum(marks)
percentage = (total_marks / 500) * 100

# Display result
print("\n--- Student Result ---")
print(f"Name       : {name}")
print(f"Class      : {student_class}")
print(f"Percentage : {percentage:.2f}%")

if percentage>=60:
        print("Grade A")
elif percentage>=50:
        print("Grade B")
elif percentage>=40:
        print("Grade C")
elif percentage >= 33:
        print("Grade D")
else:
    print("Fail")
