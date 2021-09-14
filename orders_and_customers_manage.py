import re
from random import randint


class Dishes:

    """Creating new dish for category"""

    def __init__(self, name: str, price, weight: float, time_of_preparing,
                 amount: int, identifier, newest_identifier=True):
        self._name = name
        self._price = price
        self._weight = weight
        self._time_of_preparing = time_of_preparing
        self._amount = amount
        self._id = identifier
        if newest_identifier:
            with open("info_dishes.txt", "a", encoding="UTF-8") as dishes_file:
                dishes_file.write(f"{self.name}|{self.price}|{self._weight}|{self._time_of_preparing}|{self._amount}|{self._id}\n")

    @property
    def get_dish_info(self):
        return f"{self.name} коштує {self.price}, має вагу {self.weight} грам," \
               f" готується {self.time_of_preparing} хвилин. Залишилося {self.amount} штук на складі"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if (isinstance(value, float) or isinstance(value, int)) and value > 0:
            self._price = value
            with open("info_dishes.txt", "r", encoding="UTF-8") as dishes_file:
                all_dishes = dishes_file.readlines()
                for string_index, string_row in enumerate(all_dishes):
                    array_row = string_row.split("|")
                    if array_row[0] == self._name:
                        array_row[1] = str(value)
                        all_dishes[string_index] = "|".join(map(str, array_row))
            with open("info_dishes.txt", "w", encoding="UTF-8") as dishes_file:
                for row in all_dishes:
                    dishes_file.write(row)
            return f"Ціну змінено!"
        else:
            return f"Перевірте правильність значення для поля 'ціна'!"

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if (isinstance(value, float) or isinstance(value, int)) and value > 0:
            with open("info_dishes.txt", "r", encoding="UTF-8") as dishes_file:
                all_dishes = dishes_file.readlines()
                for string_index, string_row in enumerate(all_dishes):
                    array_row = string_row.split("|")
                    if array_row[0] == self._name:
                        array_row[2] = str(value)
                        all_dishes[string_index] = "|".join(map(str, array_row))
            with open("info_dishes.txt", "w", encoding="UTF-8") as dishes_file:
                for row in all_dishes:
                    dishes_file.write(row)
            self._weight = value
            return f"Вагу змінено!"
        else:
            return f"Перевірте правильність значення для поля 'вага'!"

    @property
    def time_of_preparing(self):
        return self._time_of_preparing

    @time_of_preparing.setter
    def time_of_preparing(self, value):
        if isinstance(value, int) and value > 0:
            with open("info_dishes.txt", "r", encoding="UTF-8") as dishes_file:
                all_dishes = dishes_file.readlines()
                for string_index, string_row in enumerate(all_dishes):
                    array_row = string_row.split("|")
                    if array_row[0] == self._name:
                        array_row[3] = str(value)
                        all_dishes[string_index] = "|".join(map(str, array_row))
            with open("info_dishes.txt", "w", encoding="UTF-8") as dishes_file:
                for row in all_dishes:
                    dishes_file.write(row)
            self._time_of_preparing = value
            return f"Час приготування змінено!"
        else:
            return f"Перевірте правильність значення для поля 'час приготування'!"

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if isinstance(value, int) and value > 0:
            with open("info_dishes.txt", "r", encoding="UTF-8") as dishes_file:
                all_dishes = dishes_file.readlines()
                for string_index, string_row in enumerate(all_dishes):
                    array_row = string_row.split("|")
                    if array_row[0] == self._name:
                        array_row[4] = str(value)
                        all_dishes[string_index] = "|".join(map(str, array_row))
            with open("info_dishes.txt", "w", encoding="UTF-8") as dishes_file:
                for row in all_dishes:
                    dishes_file.write(row)
            self._amount = value
            return f"Кількість змінено!"
        else:
            return f"Перевірте правильність значення для поля 'кількість в наявності'!"

    # reducing amount when the dish is ordered by customer
    def reducing_amount(self):
        self._amount -= 1

    def increasing_amount(self):
        self._amount += 1


class Categories(Dishes):

    """Creating new category with
    ability to create to create new dishes"""

    _all_id = []

    def __init__(self, name, id=None):
        self.name = name
        if not id:                                                      # identifier for saving in txt file
            self._id = randint(1, (len(Food.all_categories) + 5) ** 2)
            while self._id in Categories._all_id:
                self._id = randint(0, (len(Food.all_categories) + 5) ** 2)
            Categories._all_id.append(self._id)
        else:
            self._id = id
            Categories._all_id.append(id)
        self.list_of_dishes = []    # dishes list of some category

        if not id:
            with open("info_categories.txt", "a", encoding="UTF-8") as categories_file:
                categories_file.write(f"{self.name}|{self.id}\n")

    # adding new dishes to some category
    def add_new_dish(self, name, price, weight, time_of_preparing, amount, identifier=None, newest_identifier=True):
        for category in Food.all_categories:
            for dish in category.list_of_dishes:
                if dish.name == name:
                    return f"Така страва вже зареєстрована. Перевірте правильність написання!"
        self.list_of_dishes.append(Dishes(name, price, weight, time_of_preparing, amount, self.id, newest_identifier))
        return f"Страва успішно зареєстрована!"

    # searching dish in the category and delete it
    def delete_dish(self, name_of_dish):
        for dish_index in range(len(self.list_of_dishes)):
            if self.list_of_dishes[dish_index].name == name_of_dish:
                Orders.deleting_dishes_from_orders_file(name_of_dish)
                Orders.deleting_dishes_from_customer_list(name_of_dish)
                with open("info_dishes.txt", "r", encoding="UTF-8") as info_dishes_file:
                    all_dishes = info_dishes_file.readlines()
                with open("info_dishes.txt", "w", encoding="UTF-8") as info_dishes_file:
                    for row in all_dishes:
                        array_row = row.split("|")
                        if array_row[0] != name_of_dish:
                            info_dishes_file.write(row)
                self.list_of_dishes.pop(dish_index)
                return f"Страва була видалена!"
        return f"Упс! Щось пішло не так!"

    @property
    def id(self):
        return self._id

    def remove_id_from_list(self):
        Categories._all_id.remove(self._id)

    # return sorted list of dishes
    def sorted_dishes(self):
        return sorted(self.list_of_dishes, key=lambda x: x.name, reverse=False)


class Food(Categories):

    """Common list of each category and
    ability to create new categories"""

    all_categories = []    # common list of all categories

    @staticmethod
    # creating new category and adding it to common list
    def create_new_category(name: str):
        for categories in Food.all_categories:
            if not name or "|" in name:
                return f"Перевірте правильність вводу!"
            if categories.name == name:
                return f"Така категорія вже зареєстрована!"
        Food.all_categories.append(Categories(name))
        return f"Категорія успішно додана!"

    @staticmethod
    # loading all categories that was saved into txt file
    def create_new_category_from_database():
        with open("info_categories.txt", "r", encoding="UTF-8") as categories_file:
            all_categories_from_file = categories_file.readlines()
            for string_row in all_categories_from_file:
                array_row = string_row.split("|")
                array_row[len(array_row)-1] = re.sub("\n", "", array_row[len(array_row)-1])
                Food.all_categories.append(Categories(array_row[0], int(array_row[1])))

    @staticmethod
    # recovering info about dishes in categories from database
    def add_new_dish_from_database():
        with open("info_dishes.txt", "r", encoding="UTF-8") as dishes_file:
            all_dishes_from_file = dishes_file.readlines()
            for string_row in all_dishes_from_file:
                array_row = string_row.split("|")
                array_row[len(array_row) - 1] = re.sub("\n", "", array_row[len(array_row) - 1])
                for category in Food.all_categories:
                    if category.id == int(array_row[len(array_row)-1]):
                        category.add_new_dish(array_row[0], float(array_row[1]), float(array_row[2]),
                                              float(array_row[3]), float(array_row[4]), category.id, False)

    @staticmethod
    def add_dish(name_of_category, name_of_dish, price, weight, time_of_preparing, amount):
        if price > 0 and weight > 0 and time_of_preparing > 0 and amount > 0 and ("|" not in name_of_dish):
            for category in Food.all_categories:
                if category.name == name_of_category:
                    return category.add_new_dish(name_of_dish, price, weight, time_of_preparing, amount)
        return f"Перевірте правильність вводу"

    # finding category in common list and deleting it
    @staticmethod
    def delete_category(name_of_category: str):
        deleting_category = None
        was_in_list = False
        list_of_dish_names = []
        for category in Food.all_categories:
            if category.name == name_of_category:
                was_in_list = True
                category.remove_id_from_list()
                list_of_dish_names = [dish.name for dish in category.list_of_dishes]
                deleting_category = category
                break
        if deleting_category:
            # for index in range(len(list_of_dish_names)):
            for dish in list_of_dish_names:
                # deleting_category.delete_dish(list_of_dish_names[index])
                Food.delete_the_dish(dish)
            Food.all_categories.remove(deleting_category)
            # deleting info about category from info_categories.txt file
            with open("info_categories.txt", "r", encoding="UTF-8") as categories_file:
                all_categories_from_file = categories_file.readlines()
            with open("info_categories.txt", "w", encoding="UTF-8") as categories_file:
                for row in all_categories_from_file:
                    array_row = row.split("|")
                    if array_row[0] != name_of_category:
                        categories_file.write(row)
        if deleting_category not in Food.all_categories and was_in_list:
            return f"Категорія успішно видалена!"
        return f"Упс! Щось пішло не так!"

    @staticmethod
    def get_dish(name):
        for category in Food.all_categories:
            for dish in category.list_of_dishes:
                if dish.name == name and dish.amount > 0:
                    return dish

    # full deleting dish from program and database
    @staticmethod
    def delete_the_dish(name_of_dish):
        answer = None
        for category in Food.all_categories:
            if answer == f"Страва була видалена!":
                return answer
            else:
                answer = category.delete_dish(name_of_dish)
        return answer


    @staticmethod
    def change_price(dish_name, new_value):
        answer_dish = None
        for category in Food.all_categories:
            for dish in category.list_of_dishes:
                if dish.name == dish_name:
                    answer_dish = dish
                    dish.price = new_value
        if answer_dish.price == new_value:
            return f"Ціну змінено!"
        return f"Перевірте правильність вводу!"

    @staticmethod
    def amount(dish_name, new_value):
        answer_dish = None
        for category in Food.all_categories:
            for dish in category.list_of_dishes:
                if dish.name == dish_name:
                    dish.amount = new_value
                    answer_dish = dish
        if answer_dish.amount == new_value:
            return f"Кількість змінено!"
        return f"Перевірте правильність вводу!"

    @staticmethod
    def weight(dish_name, new_value):
        answer_dish = None
        for category in Food.all_categories:
            for dish in category.list_of_dishes:
                if dish.name == dish_name:
                    dish.weight = new_value
                    answer_dish = dish
        if answer_dish.weight == new_value:
            return f"Вагу змінено!"
        return f"Перевірте правильність вводу!"

    @staticmethod
    def time_of_preparing(dish_name, new_value):
        answer_dish = None
        for category in Food.all_categories:
            for dish in category.list_of_dishes:
                if dish.name == dish_name:
                    dish.time_of_preparing = new_value
                    answer_dish = dish
        if answer_dish.time_of_preparing == new_value:
            return f"Час приготування змінено!"
        return f"Перевірте правильність вводу!"

    @staticmethod
    def change_category_name(old_name, new_name):
        for category in Food.all_categories:
            if category.name == old_name and "|" not in new_name:
                category.name = new_name
                with open("info_categories.txt", "r", encoding="UTF-8") as categories_file:
                    all_categories_from_file = categories_file.readlines()
                with open("info_categories.txt", "w", encoding="UTF-8") as categories_file:
                    for row in all_categories_from_file:
                        if row.split("|")[0] == old_name:
                            row = re.sub(old_name, new_name, row)
                            categories_file.write(row)
                            continue
                        categories_file.write(row)
                return f"Назву категорії змінено!"
        return f"Невдалося знайти категорію!"

    @staticmethod
    def sorted_list_of_categories():
        return sorted(Food.all_categories, key=lambda x: x.name, reverse=False)

    @staticmethod
    def search_for_category_name(name_of_category: str):
        array_with_names = []
        for category in Food.all_categories:
            if name_of_category in category.name:
                array_with_names.append(category.name)
        return array_with_names

    @staticmethod
    def search_for_dish_name(name_of_dish: str):
        array_with_dishes = []
        for category in Food.all_categories:
            for dish in category.list_of_dishes:
                if name_of_dish in dish.name:
                    array_with_dishes.append(dish)
        return array_with_dishes


class Customer:

    _order_identifiers = []     # identifiers of every created customer to saving them and their orders to file and

    def __init__(self, name, identifier=-1):
        self.name = name
        self.ordered_dishes = []    # list of ordered dishes
        self._sum_to_pay = 0.0    # price that customer must pay for dishes
        if identifier != -1:    # to do reverse filling of the program from txt
            self._order_identifier = identifier
            Customer._order_identifiers.append(self._order_identifier)
        elif identifier == -1:
            self._order_identifier = randint(1, ((len(Customer._order_identifiers) + 5) ** 2))
            while self._order_identifier in Customer._order_identifiers:    # if identifier is in list -> redefine it
                self._order_identifier = randint(0, (len(Customer._order_identifiers) + 5) ** 2)
            Customer._order_identifiers.append(self._order_identifier)      # saving identifier to common list
            self.saving_to_customers_file()

    @property
    def order_identifier(self):
        return self._order_identifier

    @property
    # running through all objects in ordered_dishes list and summing the price of every dish
    def sum_to_pay(self):
        sum = 0
        for dish in self.ordered_dishes:
            sum += dish.price
        return sum

    @sum_to_pay.setter
    def sum_to_pay(self, value):
        self._sum_to_pay = value

    # saving info about ordered dishes of customer to database
    def saving_to_customers_file(self):
        with open("customers.txt", "a", encoding="UTF-8") as customers_file:  # saving customer to file
            customers_file.write(f"{self.name}|{self.order_identifier}\n")

    # adding the dish to the dish list
    def add_dish(self, dish: Dishes, newest_identifies=True):
        if dish.amount > 0:     # checking amount of dish
            self.ordered_dishes.append(dish)
            self.sum_to_pay += dish.price
            dish.reducing_amount()
            if newest_identifies:
                self.save_dish(dish)
        else:
            return f"Вибачте. На даний час ця страва недоступна!"

    # save info about dish to database
    def save_dish(self, dish: Dishes):
        with open("orders.txt", "a", encoding="UTF-8") as orders_file:  # saving customer`s ordered dishes to file
            orders_file.write(f"{dish.name}|{self._order_identifier}\n")

    # cancel ordering some dish by customer
    def remove_dish(self, name_of_dish: str):
        for dish in self.ordered_dishes:
            if dish.name == name_of_dish:
                with open("orders.txt", "r", encoding="UTF-8") as orders_file:
                    all_orders = orders_file.readlines()
                # opening file with orders and deleting from it dish with name and special customer`s identifier
                with open("orders.txt", "w", encoding="UTF-8") as orders_file:
                    for row in all_orders:
                        array_row = row.split("|")
                        array_row[len(array_row)-1] = re.sub("\n", "", array_row[len(array_row)-1])
                        if (array_row[0] == name_of_dish) and (float(array_row[1]) == self._order_identifier):
                            self.sum_to_pay -= dish.price
                            self.ordered_dishes.remove(dish)
                            dish.increasing_amount()
                            continue
                        orders_file.write(row)
                if not self.ordered_dishes:
                    Orders.delete_the_customer(self.name)
                return f"Замовлення {name_of_dish} скасовано!"
        return f"Перевірте правильність написання страви!"

    # used when after deleting the dish in customer`s orders list remained no dishes
    def delete_id(self):
        Customer._order_identifiers.remove(self._order_identifier)


class Orders(Customer):

    """creating customers and editing ordered"""

    all_customers = []

    @staticmethod
    # creating new customer and adding it to common customer`s list
    def create_new_customer(name: str):
        for customer in Orders.all_customers:
            if customer.name == name:
                return f"Користувач із таким іменем вже зареєстрований та має замовлення!"
        if "|" in name:
            return f"Символ '|' неприпустимий у будь-яких назвах!"
        Orders.all_customers.append(Customer(name))
        return f"Зареєстровано успішно!"

    @staticmethod
    # filling to recover the information from database
    def create_new_customer_from_database():
        with open("customers.txt", "r", encoding="UTF-8") as customers_file:
            all_customers_from_file = customers_file.readlines()
            for string_row in all_customers_from_file:
                array_row = string_row.split("|")
                array_row[len(array_row)-1] = re.sub("\n", "", array_row[len(array_row)-1])
                Orders.all_customers.append(Customer((array_row[0]), int(array_row[1])))

    @staticmethod
    # to make an order for some customer
    def make_an_order(name_of_customer, name_of_dish):
        for customer in Orders.all_customers:
            if customer.name == name_of_customer:
                if isinstance(Food.get_dish(name_of_dish), Dishes):
                    customer.add_dish(Food.get_dish(name_of_dish))

    @staticmethod
    # upload all dishes into customer`s list of orders
    def add_dish_from_database():
        with open("orders.txt", "r", encoding="UTF-8") as orders_file:
            all_dishes_from_file = orders_file.readlines()
            for string_row in all_dishes_from_file:
                array_row = string_row.split("|")
                array_row[len(array_row)-1] = re.sub("\n", "", array_row[len(array_row)-1])
                for customer in Orders.all_customers:
                    if customer.order_identifier == int(array_row[1]):
                        if isinstance(Food.get_dish(array_row[0]), Dishes):
                            customer.add_dish(Food.get_dish(array_row[0]), False)

    @staticmethod
    # used for searching information about customer
    def search_for_name(name: str):
        for customer in Orders.all_customers:
            if customer.name == name:
                return customer.ordered_dishes


    @staticmethod
    # removing dish from file with orders
    def deleting_dishes_from_orders_file(name_of_dish, id=None):
        with open("orders.txt", "r", encoding="UTF-8") as orders_file:
            all_dishes_from_file = orders_file.readlines()
        with open("orders.txt", "w", encoding="UTF-8") as orders_file:
            new_info = []
            for row in all_dishes_from_file:
                array_row = row.split("|")
                if not id:
                    if name_of_dish != array_row[0]:
                        new_info.append(row)
                elif id:
                    if int(array_row[1]) != id:
                        new_info.append(row)
            for row in new_info:
                orders_file.write(row)

    @staticmethod
    def sum_to_pay_customer(name_of_customer: str):
        for customer in Orders.all_customers:
            if name_of_customer == customer.name:
                return customer.sum_to_pay

    @staticmethod
    # used when some dish from Dishes class was deleted
    def deleting_dishes_from_customer_list(name_of_dish):
        for customer_index in range(len(Orders.all_customers)):
            for dish in Orders.all_customers[customer_index].ordered_dishes:
                if dish.name == name_of_dish:
                    while dish in Orders.all_customers[customer_index].ordered_dishes:
                        if dish.name == name_of_dish:
                            Orders.all_customers[customer_index].ordered_dishes.remove(dish)
                            Orders.all_customers[customer_index].sum_to_pay -= dish.price
                    break
        for customer in Orders.all_customers.copy():
            if not customer.ordered_dishes:
                Orders.delete_the_customer(customer.name)

    @staticmethod
    # cancel the order of some customer
    def cancel_ordering_dish(name_of_customer, name_of_dish):
        for customer in Orders.all_customers:
            if customer.name == name_of_customer:
                answer = customer.remove_dish(name_of_dish)
                return answer
        return f"Упс! Щось пішло не так!"

    @staticmethod
    # deleting the customer from common customers list
    def delete_the_customer(name_of_customer: str):
        for customer in Orders.all_customers:
            if customer.name == name_of_customer:
                for dish in customer.ordered_dishes:
                    Orders.deleting_dishes_from_orders_file(dish.name, customer.order_identifier)
                with open("customers.txt", "r", encoding="UTF-8") as customers_file:
                    all_customers_from_file = customers_file.readlines()
                with open("customers.txt", "w", encoding="UTF-8") as customers_file:
                    for row in all_customers_from_file:
                        if row.split("|")[0] != name_of_customer and row.split("|")[1] != customer.order_identifier:
                            customers_file.write(row)
                customer.delete_id()
                Orders.all_customers.remove(customer)
                return f"Замовника видалено"
        return f"Упс!Щось пішло не так! Перевірте правильність вводу!"
