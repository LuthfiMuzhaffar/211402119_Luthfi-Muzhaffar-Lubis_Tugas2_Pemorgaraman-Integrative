# List to store grades
grades = []

# Take grades input until -1 is seen
while True:
    grade = input("Input grade (or -1 to end): ")
    if grade == '-1':
        break
    grades.append(int(grade))

# Calculate average
average = sum(grades) // len(grades)

# Output average
print("Average:", average)

# Output grades in order
for grade in grades:
    print(grade)
