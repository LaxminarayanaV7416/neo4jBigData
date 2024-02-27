// udpate the attributes
MATCH (student:STUDENT {name : "Laxminarayana Vadnala"}) 
SET student.age = 26
RETURN student

MATCH (course:COURSE) - [sub:COURSE_SUBJECT] -> (subj : SUBJECT)
RETURN course, sub, subj


MATCH (student:STUDENT) -[stud_course:STUDENT_COURSE] -> (course:COURSE) - [sub:COURSE_SUBJECT] -> (subj : SUBJECT)
WHERE student.name = "Laxminarayana Vadnala" AND subj.name = "Machine Learning"
return student,course, stud_course, sub, subj

