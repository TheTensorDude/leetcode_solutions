-- RANK() skips when there is same item
-- DENSE_RANK() will not skip
select
    Department,
    Employee,
    Salary
from
    (
        select
            d.name as Department,
            e.name as Employee,
            e.salary as Salary,
            DENSE_RANK() OVER(
                PARTITION BY d.name
                ORDER BY
                    e.salary DESC
            ) as r
        from
            Employee as e
            inner join Department as d on e.departmentId = d.id
    ) as t
where
    r < 4;