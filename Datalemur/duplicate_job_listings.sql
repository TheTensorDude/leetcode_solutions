select
    count(distinct company_id) as duplicate_companies
from
    (
        select
            company_id,
            title,
            description,
            count(distinct job_id) as dupl
        from
            job_listings
        group by
            company_id,
            title,
            description
        having
            count(distinct job_id) > 1
    ) as joke;