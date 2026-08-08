-- Write your query below
select employee_id, salary from employees
where employee_id%2!=0 and left(name,1) !='M' 