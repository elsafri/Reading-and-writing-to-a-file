from pprint import pprint
with open('Cook_book.txt', encoding = "UTF-8") as file:
    recipes = {}
    for line in file:
        meal = line.strip()
        ingredients_count = int(file.readline())
        ingredients = []
        for _ in range(ingredients_count):
            ingr = file.readline().strip()
            ingredient_name, quantity, measure = ingr.split('|')
            ingredients.append(
                {'ingredient_name': ingredient_name,
                 'quantity': quantity,
                 'measure': measure}
            )

        recipes[meal] = ingredients
        file.readline()
def get_shop_list_by_dishes(dishes, person_count):
     total_ingredients = []
     count =[]
     for dish in dishes:
         if dish in recipes:
             for lists in recipes[dish]:
                 if lists.get('ingredient_name') not in total_ingredients:
                     total_ingredients.append(lists.get('ingredient_name'))
                     lists.pop('ingredient_name', lists.get('ingredient_name'))
                     lists['quantity'] = int(lists['quantity']) * person_count
                     count.append(lists)
                     shop_list = dict(zip(total_ingredients, count))
                 else:
                     another_count = [shop_list[ingredient_name]]
                     for another in another_count:
                         lists['quantity'] = int(lists['quantity']) * person_count + another.get('quantity')
                     shop_list[ingredient_name] = {'measure': shop_list.get(ingredient_name).get(measure),
                                                   'quantity': lists['quantity']}
     pprint(shop_list)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)



