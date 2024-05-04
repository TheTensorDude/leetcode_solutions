select
    ifnull(
        (
            select
                salary
            from
                Employee
            group by
                salary
            order by
                salary desc
            limit
                1 offset 1
        ),
        null
    ) as SecondHighestSalary;


-- Another way
select
    max(salary) as SecondHighestSalary
from
    Employee
where
    salary not in (
        select
            max(salary)
        from
            Employee
    );