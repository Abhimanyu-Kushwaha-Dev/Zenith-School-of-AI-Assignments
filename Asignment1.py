"""
Find the maximum number in a list
Count how many numbers are greater than 75
"""


n=int(input("Enter the number of entries:"))
marks = []
c=0

for i in range(n):
    item = input(f"Enter number {i+1}: ")
    marks.append(item)

print("Max marks is: ",max(marks))

for i in range(n):
    c=c+1 if int(marks[i]) > 75 else c
print("Numbers greater than 75 are: ",c)