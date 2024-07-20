SELECT student_id, COUNT(*) as graded_assignments
FROM assignments
WHERE state = 'GRADED'
GROUP BY student_id;