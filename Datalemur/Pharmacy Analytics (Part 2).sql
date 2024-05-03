select
    manufacturer,
    count(product_id) as drug_count,
    abs(sum(total_sales - cogs)) as total_loss
from
    pharmacy_sales
where
    total_sales - cogs <= 0
group by
    manufacturer
ORDER BY
    total_loss DESC;
