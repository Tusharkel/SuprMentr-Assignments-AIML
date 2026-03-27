'''
*Assignment (28/02/2026)*

*Assignment Name* : Storytelling with Graphs
*Description* : Create bar chart, pie chart, histogram and write a short data story explaining trends..
'''

import matplotlib.pyplot as plt
students = ['A','B','C','D','E','F','G','H','I','J']
study_hours = [5,7,8,10,12,15,16,18,20,22]
marks = [50,55,60,65,72,80,85,90,92,95]
plt.figure()
plt.bar(students, marks)
plt.title("Marks scored by Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
labels = ["0-10 hrs","10-15 hrs","15-20 hrs","20+ hrs"]
sizes = [3,2,3,2]  
plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Study Hours Distribution")
plt.show()
plt.figure()
plt.hist(marks, bins=5)
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()
'''
The bar chart shows that students who studied more hours generally scored higher marks. The pie chart indicates that most students studied between 15–20 hours per week. The histogram shows that the majority of marks fall between 70 and 95, suggesting overall strong performance. This trend suggests a positive relationship between study time and academic performance.
'''