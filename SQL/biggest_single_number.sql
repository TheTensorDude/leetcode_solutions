select
    max(num) as num
from
    (
        select
            num
        from
            MyNumbers
        group by
            num
        having
            count(*) = 1
    ) as fuck;

-- Max(number)
select
    max(num) as num
from
    (
        select
            num
        from
            MyNumbers
        where
            (num, 1) in (
                select
                    num,
                    count(*) as c
                from
                    MyNumbers
                group by
                    num
            )
    ) as tab;