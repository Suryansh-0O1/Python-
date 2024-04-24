student_heights = input("Enter heights with a space in between each: ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
TH=0
ST=0
for H in student_heights:
  TH+=H
print(f"total height = {TH}")
for S in student_heights:
  ST+=1
print(f"number of students = {ST}")
print(f"average height = {round(TH/ST)}")