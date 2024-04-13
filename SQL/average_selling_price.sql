select
    p.product_id,
    IFNULL(
        round(sum(p.price * u.units) / sum(u.units), 2),
        0
    ) as average_price
from
    Prices as p
    left join UnitsSold as u on p.product_id = u.product_id
    and u.purchase_date between p.start_date
    and p.end_date
group by
    p.product_id;

-- Use case statement

SELECT
    p.product_id,
    CASE
        WHEN ROUND(SUM(p.price * u.units) / SUM(u.units), 2) IS NOT NULL THEN
            ROUND(SUM(p.price * u.units) / SUM(u.units), 2)
        ELSE
            0
    END AS average_price
FROM
    Prices AS p
LEFT JOIN
    UnitsSold AS u ON p.product_id = u.product_id
                AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY
    p.product_id;