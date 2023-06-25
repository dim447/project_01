def order(*args):
    list_order = []
    for name in args:
        if name == "Эспрессо" and in_stock["coffee"] >= 1:
            in_stock["coffee"] -= 1
            list_order.append(name)
        elif name == "Капучино" and in_stock["coffee"] >= 1 and in_stock["milk"] >= 3:
            in_stock["coffee"] -= 1
            in_stock["milk"] -= 3
            list_order.append(name)
        elif name == "Макиато" and in_stock["coffee"] >= 2 and in_stock["milk"] >= 1:
            in_stock["coffee"] -= 2
            in_stock["milk"] -= 1
            list_order.append(name)
        elif name == "Кофе по-венски" and in_stock["coffee"] >= 1 and in_stock["cream"] >= 2:
            in_stock["coffee"] -= 1
            in_stock["cream"] -= 2
            list_order.append(name)
        elif name == "Латте Макиато" and in_stock["coffee"] >= 1 and in_stock["milk"] >= 2 \
                and in_stock["cream"] >= 1:
            in_stock["coffee"] -= 1
            in_stock["milk"] -= 2
            in_stock["cream"] -= 1
            list_order.append(name)
        elif name == "Кон Панна" and in_stock["coffee"] >= 1 and in_stock["cream"] >= 1:
            in_stock["coffee"] -= 1
            in_stock["cream"] -= 1
            list_order.append(name)
    return '\n'.join(list_order) if len(list_order) > 0 else "К сожалению, не можем предложить Вам напиток"


in_stock = {"coffee": 4, "milk": 4, "cream": 0}
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Кон Панна"))
print(order("Капучино", "Макиато", "Эспрессо"))

