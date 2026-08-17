-- Write your query below
--select distinct on (student_id) student_id, exam_id, score from exam_results
--order by student_id, score desc, exam_id;

-- ans2
SELECT student_id, exam_id, score FROM exam_results
WHERE (student_id, exam_id) IN (
    SELECT student_id,
           MIN(exam_id) AS exam_id FROM exam_results
    WHERE score = (
        SELECT MAX(score) FROM exam_results e2
        WHERE e2.student_id = exam_results.student_id
    )
    GROUP BY student_id
)
ORDER BY student_id;
