def shopping_list(budget, **kwargs):
    starting_budget = budget
    my_dict = kwargs

    if starting_budget < 100:
        return "You do not have enough budget."

    completed_shopping = []

    for product, values in my_dict.items():
        price = my_dict[product][0]
        qty = my_dict[product][1]
        total_price = price * qty

        if total_price <= starting_budget:
            completed_shopping.append(f"You bought {product} for {total_price:.2f} leva.")
            starting_budget -= total_price

        if len(completed_shopping) == 5:
            return '\n'.join(completed_shopping)

    return '\n'.join(completed_shopping)


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))

# print(shopping_list(104,
#                     cola=(1.20, 2),
#                     candies=(0.25, 15),
#                     bread=(1.80, 1),
#                     pie=(10.50, 5),
#                     tomatoes=(4.20, 1),
#                     milk=(2.50, 2),
#                     juice=(2, 3),
#                     eggs=(3, 1),
#                     ))
