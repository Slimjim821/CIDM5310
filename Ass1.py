import random

random.seed(0)
salaries = [round(random.random()*1000000, -3) for _ in range(100)]
print(salaries)
