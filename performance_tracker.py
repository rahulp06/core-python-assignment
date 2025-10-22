def track_performance():
    n = int(input("Enter number of students: "))
    students = {}
    for i in range(n):
        name = input("Enter student name: ")
        marks = list(map(int, input("Enter marks separated by spaces: ").split()))
        students[name] = marks
    averages = {x: round(sum(y)/len(y), 2) for x, y in students.items()}
    top = max(averages, key=averages.get)
    print("Average Marks:", averages)
    print("Top Performer:", top)

if __name__ == "__main__":
    track_performance()
