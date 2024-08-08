import json

with open("orders_july_2023.json", "r") as my_file:
    orders = json.load(my_file)

print(orders)
print(type(orders))

#1.Какой номер самого дорого заказа за июль?:
max_price = 0
max_order = ''
for order_num, orders_data in orders.items():
    price = orders_data['price']
    if price > max_price:
        max_order = order_num
        max_price = price
print(f'Номер заказа с самой большой стоимостью за июль: {max_order}, стоимость заказа: {max_price}')

#2.Какой номер заказа с самым большим количеством товаров?:
max_quantity = 0
max_order = ''
for order_num, orders_data in orders.items():
    quantity = orders_data['quantity']
    if quantity > max_quantity:
        max_order = order_num
        max_quantity = quantity
print(f'Номер заказа с самым большим количеством товаров: {max_order}')

#3.В какой день в июле было сделано больше всего заказов?:
max_quantity = 0
date = ''
for order_num, orders_data in orders.items():
    quantity = orders_data['quantity']
    if quantity > max_quantity:
        date = orders_data.get('date')
        max_quantity = quantity
print(f'Больше всего заказов было сделано: {date}')

#4.Какой пользователь сделал самое большое количество заказов за июль?:
max_quantity = 0
user_id = ''
for order_num, orders_data in orders.items():
    quantity = orders_data['quantity']
    if quantity > max_quantity:
        user_id = orders_data.get('user_id')
        max_quantity = quantity
print(f'Пользователь, который сделал самое большое количество заказов за июль: {user_id}')

#5.У какого пользователя самая большая суммарная стоимость заказов за июль?:
max_price = 0
user_id = ''
for orders_num, orders_data in orders.items():
    price = orders_data['price']
    if price > max_price:
        user_id = orders_data.get('user_id')
        max_price = price
print(f'Пользователь с самой большой суммарной стоимостью заказов за июль: {user_id}')

#6.Какая средняя стоимость заказа была в июле?:
sum_all, count = 0, 0
for order, data in orders.items():
    sum_all += data['price']
    count += 1
print(f'Средняя стоимость заказов в июле: {sum_all/count:.3}')

#7.Какая средняя стоимость товаров в июле?:
sum_all, count = 0, 0
for order, data in orders.items():
    sum_all += data['price']
    count += data['quantity']
print(f'Средняя стоимость товаров в июле: {sum_all/count:.3}')