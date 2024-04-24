student_scores = input("Enter all the scores: ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
a=0
for b in student_scores:
  if b>a:
    a=b
print(f"The highest score in the class is: {a}")
