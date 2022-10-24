# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest_score = 0
for high in student_scores:
    if high > highest_score:
        highest_score = high
print(highest_score)
maximum = 0
for m in range(len(student_scores)):
    if student_scores[m] > maximum:
        maximum = student_scores[m]
print(f"The highest score in the class is:{maximum}")
