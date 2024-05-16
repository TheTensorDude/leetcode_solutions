select
    user_id,
    tweet_date,
    round(
        avg(tweet_count) over(
            PARTITION BY user_id
            ORDER BY
                tweet_date ROWS BETWEEN 2 PRECEDING
                AND CURRENT ROW
        ),
        2
    ) as rolling_avg_3d
from
    tweets;