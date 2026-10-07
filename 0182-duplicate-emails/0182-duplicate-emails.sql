# Write your MySQL query statement below
select email 
from Person 

GROUP BY email
HAVING COUNT(email) > 1;
