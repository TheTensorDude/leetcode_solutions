select
    eu.unique_id,
    e.name
from
    Employee as e
    left join EmployeeUNI as eu on eu.id = e.id;