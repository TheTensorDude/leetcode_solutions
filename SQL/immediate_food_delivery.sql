SELECT
    ROUND(
        (
            COUNT(*) / (
                SELECT
                    COUNT(DISTINCT customer_id)
                FROM
                    Delivery
            )
        ) * 100,
        2
    ) AS immediate_percentage
FROM
    Delivery
WHERE
    -- Also an Immediate order
    order_date = customer_pref_delivery_date -- It should be a first order
    AND (customer_id, order_date) IN (
        -- Subquery to list all the first order er user
        SELECT
            customer_id,
            MIN(order_date)
        FROM
            Delivery
        GROUP BY
            customer_id
    );