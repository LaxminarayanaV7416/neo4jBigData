MATCH(student:STUDENT)
DELETE student

// delete relationship
MATCH(stduent {name: "Laxminarayana Vadnala"}) - [rel:STUDENT_COURSE] -> (course:COURSE)
DELETE rel

// delete relationship and node
MATCH(stduent {name: "Laxminarayana Vadnala"})
DETACH DELETE rel

// delete single students 
MATCH(student :STUDENT {name: "Laxminarayana Vadnala"})
DELETE student