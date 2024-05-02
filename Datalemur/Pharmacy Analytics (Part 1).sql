select
    drug,
    sum(total_sales) - sum(cogs) as total_profit
from
    pharmacy_sales
group by
    drug
order by
    total_profit desc
limit
    3;