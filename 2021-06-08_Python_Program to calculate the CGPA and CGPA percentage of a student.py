#program to calculate the CGPA and CGPA percentage of a student
"Computer Programming Tutor_June7,2021"

def ComputeCgpa(marks,n):
    # Variable to store the grades in every subject
    grade = [0]*n
    Sum =0
    #Computing Grades
    for i in range(n):
        grade[i] = (marks[i]/10)
    #Computing the Sum of Grades
    for i in range(n):
        Sum +=grade[i]
        #Computing The CGPA
    cgpa = Sum /n
    return cgpa
n =8
marks = [45,78,78,99,67,89,56,78]
cgpa = ComputeCgpa(marks,n)
print ("CGPA=","%.1f" %cgpa)
print("CGPA Percentage=","%.2f" %(cgpa*9.5))
