# Define sets
math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}

# To generate a set with all unique students
print(math_students | biology_students)

# To generate a set with students who are in both courses
print(math_students & biology_students)