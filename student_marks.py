python
student_marks.py

students = ["Ayanda", "natasha", "anesu", "mutale", "gamu"]
marks = [85, 92, 78, 88, 95]

total = sum(marks)
average = total / len(marks)

def assign_grade(scores):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"

print("-- Student Marks Summary --")
for i in range(len(students)):
    grade = assign_grade(marks[i])
    print(f"{students[i]}: {marks[i]} – Grade {grade}")

print(f"\nAverage marks: {average:.1f}")
