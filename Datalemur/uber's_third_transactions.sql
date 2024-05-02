select
    user_id,
    spend,
    transaction_date
from
    (
        select
            user_id,
            spend,
            transaction_date,
            RANK() OVER (
                PARTITION BY user_id
                ORDER BY
                    transaction_date ASC
            ) AS r
        from
            transactions
    ) as dummy
where
    r = 3;