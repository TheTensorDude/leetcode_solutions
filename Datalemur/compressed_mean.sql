SELECT
    ROUND(
        SUM(item_count :: DECIMAL * order_occurrences) / SUM(order_occurrences),
        1
    ) AS average_item_count
FROM
    items_per_order;