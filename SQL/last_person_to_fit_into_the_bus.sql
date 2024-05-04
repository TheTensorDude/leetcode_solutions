select
    *,
    SUM(weight) OVER (
        ORDER BY
            turn ROWS BETWEEN UNBOUNDED PRECEDING
            AND CURRENT ROW
    ) as bus_weight
from
    Queue;