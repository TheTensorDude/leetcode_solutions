select
    name as person_name
from
    (
        select
            turn as Turn,
            person_id as ID,
            person_name as name,
            weight as Weight,
            SUM(weight) OVER(
                ORDER BY
                    turn
            ) as total_weight
        from
            Queue
    ) as cumul
where
    total_weight <= 1000
order by
    total_weight desc
limit
    1;