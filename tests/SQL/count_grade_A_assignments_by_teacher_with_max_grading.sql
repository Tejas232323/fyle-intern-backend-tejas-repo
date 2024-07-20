SELECT COUNT(*) as grade_a_count
FROM assignments a
JOIN (
    SELECT teacher_id, COUNT(*) as graded_count
    FROM assignments
    WHERE state = 'GRADED'
    GROUP BY teacher_id
    ORDER BY graded_count DESC
    LIMIT 1
) t ON a.teacher_id = t.teacher_id
WHERE a.grade = 'A' AND a.state = 'GRADED';