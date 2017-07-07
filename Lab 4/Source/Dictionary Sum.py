#function for calculating average marks
def student_avg_marks(list_of_dicts):
    #taking one tuple at a time and finding avg
    for d in list_of_dicts:
        a = d.pop('mid_1')
        b = d.pop('mid_2')
        d['Final'] = (a+b)/2
    return list_of_dicts

#list of student marks tuples
student_marks = [
  {'id' : 1, 'subject' : 'Mathematics', 'mid_1' : 12, 'mid_2' : 18},
  {'id' : 1, 'subject' : 'Chemistry', 'mid_1' : 15, 'mid_2' : 20},
  {'id' : 2, 'subject' : 'Chemistry', 'mid_1' : 13, 'mid_2' : 17},
  {'id' : 3, 'subject' : 'Physics', 'mid_1' : 11, 'mid_2' : 19}
]
print(student_avg_marks(student_marks))
