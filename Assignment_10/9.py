import matplotlib.pyplot as plt

semester = ["Sem 1", "Sem 2"]
marks = [78, 85]

plt.bar(semester, marks, color=["blue", "green"])
plt.title("Semester-wise Result Comparison")
plt.ylabel("Marks")
plt.xlabel("Semesters")
plt.ylim(0, 100)
plt.show()
