SELECT e1.name
FROM Employee e1
WHERE 5 <= (
    SELECT COUNT(*)
    FROM Employee e2
    WHERE e2.managerId = e1.id
);
