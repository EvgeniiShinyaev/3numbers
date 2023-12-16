from functools import reduce
orders = [
    {"order_id": 1, "customer_id": 101, "amount": 150.0},
    {"order_id": 2, "customer_id": 102, "amount": 200.0},
    {"order_id": 3, "customer_id": 101, "amount": 75.0},
    {"order_id": 4, "customer_id": 103, "amount": 100.0},
    {"order_id": 5, "customer_id": 101, "amount": 50.0},
    {"order_id": 6, "customer_id": 102, "amount": 90.0},
    {"order_id": 7, "customer_id": 103, "amount": 120.0},
    {"order_id": 8, "customer_id": 104, "amount": 180.0},
    {"order_id": 9, "customer_id": 105, "amount": 220.0},
    {"order_id": 10, "customer_id": 104, "amount": 75.0},
    {"order_id": 11, "customer_id": 105, "amount": 60.0},
    {"order_id": 12, "customer_id": 101, "amount": 80.0},
    {"order_id": 13, "customer_id": 106, "amount": 150.0},
    {"order_id": 14, "customer_id": 107, "amount": 200.0},
    {"order_id": 15, "customer_id": 106, "amount": 75.0},
    {"order_id": 16, "customer_id": 108, "amount": 100.0},
    {"order_id": 17, "customer_id": 107, "amount": 50.0},
    {"order_id": 18, "customer_id": 108, "amount": 90.0},
    {"order_id": 19, "customer_id": 109, "amount": 120.0},
    {"order_id": 20, "customer_id": 110, "amount": 180.0},
]


# Заданный идентификатор клиента
target_customer_id = 101

# Функция для фильтрации заказов только для определенного клиента
filtered_orders = list(filter(lambda order: order["customer_id"] == target_customer_id, orders))
# Функция для извлечения стоимости заказа из заказа
def get_order_amount(order):
    return order["amount"]

# Используем map для извлечения стоимости заказов
order_amounts = list(map(get_order_amount, filtered_orders))

# Функция для подсчета суммы заказов данного клиента
def calculate_total_amount(total, amount):
    return total + amount

total_amount = reduce(calculate_total_amount, order_amounts, 0)

# Функция для подсчета средней стоимости заказов данного клиента
total_orders = len(order_amounts)
average_amount = total_amount / total_orders if total_orders > 0 else 0

print(f"Заказы для клиента с ID {target_customer_id}:")
for order in filtered_orders:
    print(f"order ID: {order['order_id']}, Сумма: {order['amount']}")

print(f"Общая сумма заказов: {total_amount}")
print(f"Средняя стоимость заказов: {average_amount}")


