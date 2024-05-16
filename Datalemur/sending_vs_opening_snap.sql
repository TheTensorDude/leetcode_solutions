SELECT
    ab.age_bucket,
    ROUND(
        SUM(
            CASE
                WHEN a.activity_type = 'open' THEN time_spent
            END
        ) / SUM(
            CASE
                WHEN a.activity_type = 'open' THEN time_spent
                WHEN a.activity_type = 'send' THEN time_spent
            END
        ) * 100.0,
        2
    ) AS open_perc,
    ROUND(
        SUM(
            CASE
                WHEN a.activity_type = 'send' THEN time_spent
            END
        ) / SUM(
            CASE
                WHEN a.activity_type = 'open' THEN time_spent
                WHEN a.activity_type = 'send' THEN time_spent
            END
        ) * 100.0,
        2
    ) AS send_perc
FROM
    activities a
    LEFT JOIN age_breakdown ab on a.user_id = ab.user_id
GROUP BY
    ab.age_bucket;