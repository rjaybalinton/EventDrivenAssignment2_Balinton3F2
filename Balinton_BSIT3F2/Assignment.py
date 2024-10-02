students = ['John', 'Maria', 'David', 'Samantha']
selected_student = []

while True:
    try:
        index = int(input("Enter an index (0-3): "))
        if 0 <= index < len(students):
            selected_student.append(students[index])
            print("Student at index", index, ":", selected_student[0])
            break
        else:
            print("Invalid index. Please enter an integer between 0 and 3.")
    except ValueError:
        print("Please enter a valid integer.")

print(" ")

numbers = (1, 4, 7, 10, 13, 16)

odd_numbers = []
odd_sum = 0
odd_count = 0

for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)
        odd_sum += num
        odd_count += 1

if odd_count > 0:
    odd_average = odd_sum / odd_count
    print("Odd numbers:", odd_numbers)
    print("Average of odd numbers:", odd_average)
else:
    print("No odd numbers found.")

print(" ")

people = {'profile': {'John': 19, 'Emily': 21, 'Sarah': 25, 'Tom': 18}}

older_than_19 = []
below_or_equal_19 = []

for name, age in people['profile'].items():
    if age > 19:
        older_than_19.append(name)
    else:
        below_or_equal_19.append(name)

print("People older than 19:", older_than_19)
print("People 19 or younger:", below_or_equal_19)

print(" ")

numbers = [1, 3, 2, 4, 3, 1, 2, 5, 10]

duplicates = []
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

if duplicates:
    print("Duplicate numbers:", duplicates)
else:
    print("No duplicate numbers found.")

print(" ")

students_scores = [('John', 85), ('Maria', 92), ('Tom', 76), ('Sarah', 90)]

highest_score = 0
highest_scorer = []

for student in students_scores:
    if student[1] > highest_score:
        highest_score = student[1]
        highest_scorer = []  
        highest_scorer.append(student[0])

print("Student with the highest score:", highest_scorer[0], "Score:", highest_score)
