student = {}
num=int(input("Enter no of student:- "))
for i in range(1, num+1):
    print(f"Enter information for Student {i}:")
    name = input("Enter Name: ")
    percentage = input("Enter Percentage Marks: ")
    
    student[name] = [percentage]

print("\nStudent Information:")
for name, percentage in student.items():
    print(f"{name}: {percentage}%")
