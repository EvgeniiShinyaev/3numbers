from functools import reduce
users = [
    {"name": "Alice", "expenses": [100, 50, 75, 200]},
    {"name": "Bob", "expenses": [50, 75, 80, 100]},
    {"name": "Charlie", "expenses": [200, 300, 50, 150]},
    {"name": "David", "expenses": [100, 200, 300, 400]},
    {"name": "Eve", "expenses": [150, 250, 90, 180]},
    {"name": "Frank", "expenses": [50, 75, 80, 100]},
    {"name": "Grace", "expenses": [200, 300, 50, 150]},
    {"name": "Hank", "expenses": [100, 200, 300, 400]},
    {"name": "Ivy", "expenses": [150, 250, 90, 180]},
    {"name": "Jack", "expenses": [50, 75, 80, 100]},
    {"name": "Katie", "expenses": [200, 300, 50, 150]},
    {"name": "Liam", "expenses": [100, 200, 300, 400]},
    {"name": "Mia", "expenses": [150, 250, 90, 180]},
    {"name": "Noah", "expenses": [50, 75, 80, 100]},
    {"name": "Olivia", "expenses": [200, 300, 50, 150]},
    {"name": "Peter", "expenses": [100, 200, 300, 400]},
    {"name": "Quinn", "expenses": [150, 250, 90, 180]},
    {"name": "Rachel", "expenses": [50, 75, 80, 100]},
    {"name": "Sam", "expenses": [200, 300, 50, 150]}
]


# Функция для вычисления общей суммы расходов пользователя
def calculate_total_expenses(user):
    return reduce(lambda x, y: x + y, user["expenses"], 0)

# Заданные критерии для фильтрации (например, расходы больше 300)
criteria = {"expenses": 1000}

def calculate_total_expenses(user):
    return reduce(lambda x, y: x + y, user["expenses"], 0)

# Рассчет общей суммы расходов для каждого пользователя
total_expenses_per_user = list(map(calculate_total_expenses, users))

# Фильтрация пользователей по заданным критериям
filtered_users = list(filter(lambda user: "expenses" not in criteria or calculate_total_expenses(user) >= criteria["expenses"], users))

# Вычисление общей суммы расходов всех отфильтрованных пользователей
total_expenses_all_users = reduce(lambda x, y: x + y, total_expenses_per_user, 0)

print("Отфильтрованные пользователи:")
for user in filtered_users:
    print(user)

print("Общие расходы каждого пользователя:", total_expenses_per_user)
print("Общая сумма расходов всех отфильтрованных пользователей:", total_expenses_all_users)