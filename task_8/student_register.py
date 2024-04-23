num_of_exam_attendees = int(input(" How many Stududents will be attending todays exam: \n "))

with open ('reg_form.txt', 'w+') as rf:
    for num in range(num_of_exam_attendees):
        student_id = input(" Please enter the following students ID no.")
        rf.write(student_id + '\n')
        rf.write('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n')

with open ('reg_form.txt', 'r') as rf:
    for line in rf:
        print(line)