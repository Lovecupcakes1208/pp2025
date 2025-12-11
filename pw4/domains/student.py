import numpy as np

class Student:
    def __init__(self, sid, name, dob):
        self.sid = sid
        self.name = name
        self.dob = dob
        self.marks = {} 
        self.gpa = 0.0

    def add_mark(self, course_id, mark):
        self.marks[course_id] = mark

    def cal_gpa(self, courses):
        score_list = []
        credit_list = []
        
        for course in courses:
            if course.cid in self.marks:
                score_list.append(self.marks[course.cid])
                credit_list.append(course.credits)
        
        if credit_list and np.sum(credit_list) > 0:
            self.gpa = np.average(score_list, weights=credit_list)
        else:
            self.gpa = 0.0

    def __str__(self):
        return f"{self.name} (ID: {self.sid})"