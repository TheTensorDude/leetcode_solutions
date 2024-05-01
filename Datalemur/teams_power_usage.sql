select
    sender_id,
    count(message_id) as message_count
from
    messages
where
    DATE_PART('month', sent_date) = 8
    AND DATE_PART('year', sent_date) = 2022
group by
    sender_id
order by
    message_count desc
limit
    2;