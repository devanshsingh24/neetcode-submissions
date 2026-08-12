-- Write your query below
select a.name, coalesce(sum(distance),0) as travelled_distance
from users as a
left join rides as b
on a.id=b.user_id
group by a.id, a.name
order by travelled_distance desc
