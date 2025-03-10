# employes
#
# SELECT name, salary
# from employes
# WHERE salary > (
#     SELECT AVG(salary)
#     from employes
# )
#
# SELECT salary
# FROM employes
# ORDER BY salary DESC
# offset 2
# limit 1
#
#
# SELECT email
# from users
# GROUP BY email
# HAVING COUNT(email) > 1
#
# departmant_employee
#
# SELECT id, name
# FROM employes em
# LEFT JOIN departmant_employee de
#     ON em.id = de.user_id
#
# GROUP BY em.id
# HAVING COUNT(de.user_id) > 1
#


