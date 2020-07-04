student_scores = {"Thomas":[25, 26.5, 28]}



student_name = input("Enter student name: ")
name = student_name.title()
for i in student_scores:
	if name == i:
		score = student_scores[i]
		print(float(sum(score)/len(score)))
		
