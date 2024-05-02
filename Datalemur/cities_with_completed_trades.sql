SELECT city,
       Count(order_id) AS total_orders
FROM   trades AS tr
       INNER JOIN users AS us
               ON tr.user_id = us.user_id
WHERE  tr.status = 'Completed'
GROUP  BY city
ORDER  BY total_orders DESC
LIMIT  3; 