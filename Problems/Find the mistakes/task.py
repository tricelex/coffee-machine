class MyClass:
    n_objects = 0

    def __new__(cls):
        if cls.n_objects < 5:
            cls.n_objects += 1
            return object.__new__(cls)
        return None

    def __str__(self):
        return f'An object of {self.__class__.__name__}'


# mm = MyClass()
# print(mm)

# # Write your code here
# water = 400
# milk = 540
# bean = 120
# money = 550
# cup = 9
#
#
# def not_enough(item):
#     print(f'Sorry, not enough {item}!')
#
#
# def take(total_cash):
#     print(f'I gave you {total_cash}\n')
#
#
# def state(water, milk, bean, money, cup):
#     print(f'The coffee machine has:')
#     print(f'{water} of water')
#     print(f'{milk} of milk')
#     print(f'{bean} of coffee beans')
#     print(f'{cup} of disposable cups')
#     print(f'${money} of money\n')
#
#
# def fill():
#     list_of_globals = globals()
#     new_water = int(input('Write how many ml of water do you want to add:\n'))
#     new_milk = int(input('Write how many ml of milk do you want to add:\n'))
#     new_bean = int(input('Write how many grams of coffee beans do you want to add:\n'))
#     new_cups = int(input('Write how many disposable cups of coffee do you want to add:\n'))
#     print('')
#     list_of_globals['water'] += new_water
#     list_of_globals['milk'] += new_milk
#     list_of_globals['bean'] += new_bean
#     list_of_globals['cup'] += new_cups
#
#
# def buy_espresso():
#     list_of_globals = globals()
#     list_of_globals['water'] -= 250
#     list_of_globals['bean'] -= 16
#     list_of_globals['money'] += 4
#     list_of_globals['cup'] -= 1
#     print('I have enough resources, making you a coffee!')
#
#
# def buy_latte():
#     list_of_globals = globals()
#     if list_of_globals['water'] < 350:
#         return not_enough('water')
#     list_of_globals['water'] -= 350
#     list_of_globals['milk'] -= 75
#     list_of_globals['bean'] -= 20
#     list_of_globals['money'] += 7
#     list_of_globals['cup'] -= 1
#     print('I have enough resources, making you a coffee!')
#
#
# def buy_cappuccino():
#     list_of_globals = globals()
#     list_of_globals['water'] -= 200
#     list_of_globals['milk'] -= 100
#     list_of_globals['bean'] -= 12
#     list_of_globals['money'] += 6
#     list_of_globals['cup'] -= 1
#     print('I have enough resources, making you a coffee!')
#
#
# def buy():
#     choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
#     if choice == '1':
#         buy_espresso()
#     elif choice == '2':
#         buy_latte()
#     elif choice == '3':
#         buy_cappuccino()
#     elif choice == 'back':
#         return
#
#
# check = True
# while True:
#     action = input('write action (buy, fill, take, remaining, exit):\n ')
#     if action == 'buy':
#         buy()
#     elif action == 'fill':
#         fill()
#     elif action == 'take':
#         take(money)
#         money = 0
#     elif action == 'remaining':
#         state(water, milk, bean, money, cup)
#     elif action == 'exit':
#         break
#
