from tkinter import END
import tkinter as tk
from orders_and_customers_manage import *


Food.create_new_category_from_database()
Food.add_new_dish_from_database()
Orders.create_new_customer_from_database()
Orders.add_dish_from_database()


def process_of_creating_category(previous_window: tk.Toplevel, category_name: tk.StringVar):
    previous_window.destroy()
    name_of_category = category_name.get()
    answer_of_program = Food.create_new_category(name_of_category)
    info_window = tk.Toplevel()
    info_window.geometry("250x50")
    info_window.resizable(width=False, height=False)
    info_in_window = tk.Label(info_window, text=answer_of_program)
    info_in_window.grid(row=0, column=0)
    quit_button = tk.Button(info_window, text="OK", command=info_window.destroy)
    quit_button.grid(row=1, column=1)


def creating_category_button(previous_window: tk.Toplevel):
    previous_window.destroy()
    creating_menu_window = tk.Toplevel(bg="#FDD9B5")
    creating_menu_window.geometry("350x50")
    creating_menu_window.resizable(width=False, height=False)
    creating_menu_window.title = "Створення нової категорії"
    category_name = tk.StringVar()
    category_name_field = tk.Entry(creating_menu_window, textvariable=category_name, width=20)
    category_name_field.grid(row=0, column=1)
    tip_for_category_name_field = tk.Label(creating_menu_window, text="Введіть назву категорії:", bg="#FDD9B5")
    tip_for_category_name_field.grid(column=0, row=0)
    agree_button = tk.Button(creating_menu_window,
                             command=lambda: process_of_creating_category(creating_menu_window, category_name))
    agree_button["text"] = "Створити"
    agree_button.grid(row=3, column=4)


def process_of_creating_dish(previous_window: tk.Toplevel, array_with_variables):
    try:
        previous_window.destroy()
        info_window = tk.Toplevel()
        info_window.geometry("250x50")
        info_window.resizable(width=False, height=False)
        array_with_values = []
        for index in range(len(array_with_variables)):
            array_with_values.append(array_with_variables[index].get())
        answer = Food.add_dish(array_with_values[0], array_with_values[1], array_with_values[2],
                               array_with_values[3], array_with_values[4], array_with_values[5])
        tk.Label(info_window, text=answer).grid(row=0, column=0)
        tk.Button(info_window, text="OK", command=info_window.destroy).grid(row=1, column=1)
    except:
        info_window.destroy()
        exception_window = tk.Toplevel()
        exception_window.geometry("290x75")
        exception_window.resizable(width=False, height=False)
        tk.Label(exception_window, text="Перевірте правильність вводу!!!").grid(row=0, column=0)
        tk.Button(exception_window, text="ОК", command=exception_window.destroy).grid(row=1, column=1,
                                                                                      padx=20, pady=20)


def adding_dish_button(previous_window: tk.Toplevel):
    previous_window.destroy()
    adding_new_dish_window = tk.Toplevel(bg="#FDD9B5")
    tk_variables = [tk.StringVar(), tk.StringVar(), tk.DoubleVar(), tk.DoubleVar(), tk.IntVar(), tk.IntVar()]
    for index in range(len(tk_variables)):
        tk.Entry(adding_new_dish_window, textvariable=tk_variables[index], width=25).grid(column=1, row=index)
    tk.Label(adding_new_dish_window, text="Введіть назву категорії, в якій буде нова страва:",
             bg="#FDD9B5").grid(row=0, column=0, sticky="W")
    tk.Label(adding_new_dish_window, text="Введіть назву страви:", bg="#FDD9B5").grid(row=1, column=0, sticky="W")
    tk.Label(adding_new_dish_window, text="Введіть ціну для нової страви:",
             bg="#FDD9B5").grid(row=2, column=0, sticky="W")
    tk.Label(adding_new_dish_window, text="Введіть вагу для нової страви:",
             bg="#FDD9B5").grid(row=3, column=0, sticky="W")
    tk.Label(adding_new_dish_window, text="Введіть час приготування нової страви:",
             bg="#FDD9B5").grid(row=4, column=0, sticky="W")
    tk.Label(adding_new_dish_window, text="Введіть кількість нової страви на складі:",
             bg="#FDD9B5").grid(row=5, column=0, sticky="W")
    tk.Button(adding_new_dish_window, text="Створити страву", activebackground="#DD7EFE",
              command=lambda: process_of_creating_dish(adding_new_dish_window,
                                                       tk_variables)).grid(row=7, column=2, pady=15, padx=15)


def process_changing_name_category(previous_window: tk.Toplevel,
                                   old_name_var: tk.StringVar, new_name_category: tk.StringVar):
    previous_window.destroy()
    window = tk.Toplevel()
    try:
        answer = Food.change_category_name(old_name_var.get(), new_name_category.get())
        tk.Label(window, text=answer).grid(row=0, column=0, padx=30, pady=30)
        tk.Button(window, text="OK", activebackground="#DD7EFE", command=window.destroy). grid(row=1, column=1,
                                                                                               padx=10, pady=10)
    except:
        tk.Label(window, text="Упс! Щось пішло не так...").grid(row=0, column=0, padx=30, pady=30)
        tk.Button(window, text="OK", activebackground="#DD7EFE", command=window.destroy).grid(row=1, column=1,
                                                                                              padx=10, pady=10)


def changing_name_category(previous_window: tk.Toplevel):
    previous_window.destroy()
    window = tk.Toplevel(bg="#FDD9B5")
    tk.Label(window, text="Введіть стару назву категорії:", bg="#FDD9B5").grid(row=0, column=0, padx=10)
    old_name_var = tk.StringVar()
    tk.Entry(window, textvariable=old_name_var, width=25).grid(row=0, column=1)
    tk.Label(window, text="Введіть нову назву категорії:", bg="#FDD9B5").grid(row=1, column=0, padx=10)
    new_name_var = tk.StringVar()
    tk.Entry(window, textvariable=new_name_var, width=25).grid(row=1, column=1)
    tk.Button(window, text="Змінити назву", activebackground="#DD7EFE",
              command=lambda: process_changing_name_category(window, old_name_var, new_name_var)).grid(row=2, column=2,
                                                                                                       padx=20, pady=20)


def process_changing_dish_info(previous_window: tk.Toplevel, name_var: tk.StringVar, number_var, criteria: str):
    previous_window.destroy()
    window = tk.Toplevel()
    try:
        if criteria == "price":
            answer = Food.change_price(name_var.get(), number_var.get())
            tk.Label(window, text=answer).grid(row=0, column=0, padx=25, pady=25)
            tk.Button(window, text="ОК", command=window.destroy).grid(row=1, column=1, padx=30, pady=30)
        elif criteria == "weight":
            answer = Food.weight(name_var.get(), number_var.get())
            tk.Label(window, text=answer).grid(row=0, column=0, padx=25, pady=25)
            tk.Button(window, text="ОК", command=window.destroy).grid(row=1, column=1, padx=30, pady=30)
        elif criteria == "time":
            answer = Food.time_of_preparing(name_var.get(), number_var.get())
            tk.Label(window, text=answer).grid(row=0, column=0, padx=25, pady=25)
            tk.Button(window, text="ОК", command=window.destroy).grid(row=1, column=1, padx=30, pady=30)
        elif criteria == "amount":
            answer = Food.amount(name_var.get(), number_var.get())
            tk.Label(window, text=answer).grid(row=0, column=0, padx=25, pady=25)
            tk.Button(window, text="ОК", command=window.destroy).grid(row=1, column=1, padx=30, pady=30)
    except:
        tk.Label(window, text="Упс! Щось пішло не так...").grid(row=0, column=0, padx=30, pady=30)
        tk.Button(window, text="OK", activebackground="#DD7EFE", command=window.destroy).grid(row=1, column=1,
                                                                                              padx=10, pady=10)


def changing_dishes_info(previous_window: tk.Toplevel, criteria: str):
    previous_window.destroy()
    window = tk.Toplevel(bg="#FDD9B5")
    name_var = tk.StringVar()
    if criteria == "price":
        price_var = tk.DoubleVar()
        tk.Label(window, text="Введіть назву страви:", bg="#FDD9B5").grid(row=0, column=0, padx=10)
        tk.Entry(window, textvariable=name_var, width=25).grid(row=0, column=1, padx=10)
        tk.Label(window, text="Введіть нову ціну:", bg="#FDD9B5").grid(row=1, column=0, padx=10)
        tk.Entry(window, textvariable=price_var, width=10).grid(row=1, column=1, padx=10)
        tk.Button(window, text="Змінити",
                  command=lambda: process_changing_dish_info(window, name_var, price_var, criteria)).grid(row=2,
                                                                                                          column=3,
                                                                                                          padx=25,
                                                                                                          pady=25)

    elif criteria == "weight":
        weight_var = tk.DoubleVar()
        tk.Label(window, text="Введіть назву страви:", bg="#FDD9B5").grid(row=0, column=0, padx=10)
        tk.Entry(window, textvariable=name_var, width=25).grid(row=0, column=1, padx=10)
        tk.Label(window, text="Введіть нову вагу:", bg="#FDD9B5").grid(row=1, column=0, padx=10)
        tk.Entry(window, textvariable=weight_var, width=10).grid(row=1, column=1, padx=10)
        tk.Button(window, text="Змінити",
                  command=lambda: process_changing_dish_info(window, name_var, weight_var, criteria)).grid(row=2,
                                                                                                           column=3,
                                                                                                           padx=25,
                                                                                                           pady=25)

    elif criteria == "time":
        time_var = tk.IntVar()
        tk.Label(window, text="Введіть назву страви:", bg="#FDD9B5").grid(row=0, column=0, padx=10)
        tk.Entry(window, textvariable=name_var, width=25).grid(row=0, column=1, padx=10)
        tk.Label(window, text="Введіть новий час приготування:", bg="#FDD9B5").grid(row=1, column=0, padx=10)
        tk.Entry(window, textvariable=time_var, width=10).grid(row=1, column=1, padx=10)
        tk.Button(window, text="Змінити",
                  command=lambda: process_changing_dish_info(window, name_var, time_var, criteria)).grid(row=2,
                                                                                                         column=3,
                                                                                                         padx=25,
                                                                                                         pady=25)

    elif criteria == "amount":
        amount_var = tk.IntVar()
        tk.Label(window, text="Введіть назву страви:", bg="#FDD9B5").grid(row=0, column=0, padx=10)
        tk.Entry(window, textvariable=name_var, width=25).grid(row=0, column=1, padx=10)
        tk.Label(window, text="Введіть нову кількість:", bg="#FDD9B5").grid(row=1, column=0, padx=10)
        tk.Entry(window, textvariable=amount_var, width=10).grid(row=1, column=1, padx=10)
        tk.Button(window, text="Змінити",
                  command=lambda: process_changing_dish_info(window, name_var, amount_var, criteria)).grid(row=2,
                                                                                                           column=3,
                                                                                                           padx=25,
                                                                                                           pady=25)


def changing_info_button(previous_window: tk.Toplevel):
    previous_window.destroy()
    changing_info_window = tk.Toplevel(bg="#FDD9B5")
    tk.Label(changing_info_window, text="Зміна інформації категорій:", bg="#FDD9B5").grid(row=0, column=0, padx=50)
    tk.Button(changing_info_window, text="Змінити назву категорії", bg="#D7E17B",
              command=lambda: changing_name_category(changing_info_window)).grid(row=0, column=1)
    tk.Label(changing_info_window, text="Зміна інформації про страви:", bg="#FDD9B5").grid(row=1, column=0, padx=50)
    tk.Button(changing_info_window, text="Змінити ціну страви", bg="#D7E17B",
              command=lambda: changing_dishes_info(changing_info_window, "price")).grid(row=1, column=1)
    tk.Button(changing_info_window, text="Змінити вагу страви", bg="#D7E17B",
              command=lambda: changing_dishes_info(changing_info_window, "weight")).grid(row=1, column=2, padx=15)
    tk.Button(changing_info_window, text="Змінити час приготування страви", bg="#D7E17B",
              command=lambda: changing_dishes_info(changing_info_window, "time")).grid(row=1, column=3, padx=15)
    tk.Button(changing_info_window, text="Змінити кількість страви на складі", bg="#D7E17B",
              command=lambda: changing_dishes_info(changing_info_window, "amount")).grid(row=1, column=4, padx=15)


def process_deleting_category(previous_window: tk.Toplevel, name_var: tk.StringVar):
    previous_window.destroy()
    window = tk.Toplevel()
    answer = Food.delete_category(name_var.get())
    tk.Label(window, text=answer, bg="#FDD9B5").grid(row=0, column=0, padx=20, pady=20)
    tk.Button(window, text="OK", command=window.destroy).grid(row=1, column=1, padx=20, pady=20)
    for customer in Orders.all_customers:
        print(f"{customer.name}: {[dish.name for dish in customer.ordered_dishes]}")


def deleting_category_button(previous_window: tk.Toplevel):
    previous_window.destroy()
    inner_deleting_window = tk.Toplevel(bg="#FDD9B5")
    tk.Label(inner_deleting_window, text="Введіть назву категорії для видалення:", bg="#FDD9B5").grid(row=0, column=0,
                                                                                                      padx=10, pady=10)
    name_var = tk.StringVar()
    tk.Entry(inner_deleting_window, textvariable=name_var, width=25).grid(row=0, column=1, padx=10, pady=10)
    tk.Button(inner_deleting_window, text="Видалити",
              command=lambda: process_deleting_category(inner_deleting_window, name_var)).grid(row=1, column=2,
                                                                                               padx=25, pady=25)


def process_deleting_dish(previous_window: tk.Toplevel, name_of_dish: tk.StringVar):
    previous_window.destroy()
    window = tk.Toplevel()
    answer = Food.delete_the_dish(name_of_dish.get())
    tk.Label(window, text=answer, bg="#FDD9B5").grid(row=0, column=0, padx=20, pady=20)
    tk.Button(window, text="OK", command=window.destroy).grid(row=1, column=1, padx=20, pady=20)


def deleting_dish_button(previous_window: tk.Toplevel):
    previous_window.destroy()
    inner_window = tk.Toplevel(bg="#FDD9B5")
    tk.Label(inner_window, text="Введіть назву страви:", bg="#FDD9B5").grid(row=0, column=0,
                                                                            padx=10, pady=10)
    name_var = tk.StringVar()
    tk.Entry(inner_window, textvariable=name_var, width=25).grid(row=0, column=1, padx=10, pady=10)
    tk.Button(inner_window, text="Видалити",
              command=lambda: process_deleting_dish(inner_window, name_var)).grid(row=1, column=2,
                                                                                  padx=25, pady=25)


def list_of_food_button(previous_window: tk.Toplevel):
    previous_window.destroy()
    window = tk.Toplevel(bg="#FDD9B5")
    sorted_categories = Food.sorted_list_of_categories()
    for index in range(len(sorted_categories)):
        tk.Label(window, text=f"{sorted_categories[index].name}:", bg="#FDD9B5").grid(row=index, column=0, padx=10, pady=10)
        new_listbox = tk.Listbox(window, width=100)
        for dish in sorted_categories[index].sorted_dishes():
            new_listbox.insert(END, dish.get_dish_info+'\n')
        new_listbox.grid(row=index, column=1, padx=30, pady=10)


def process_of_deleting_customer(previous_window: tk.Toplevel, name_customer: tk.StringVar):
    previous_window.destroy()
    window = tk.Toplevel()
    answer = Orders.delete_the_customer(name_customer.get())
    tk.Label(window, text=answer).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(window, text="OK", command=window.destroy).grid(row=1, column=1, padx=15, pady=15)


def delete_the_customer(previous_window: tk.Toplevel):
    previous_window.destroy()
    window = tk.Toplevel(bg="#FDD9B5")
    name_of_customer_var = tk.StringVar()
    tk.Label(window, text="Введіть назву клієнта:", bg="#FDD9B5").grid(row=0, column=0, padx=10, pady=10)
    tk.Entry(window, textvariable=name_of_customer_var, width=25).grid(row=0, column=1, padx=10, pady=10)
    tk.Button(window, text="Видалити",
              command=lambda: process_of_deleting_customer(window, name_of_customer_var)).grid(row=1, column=1,
                                                                                               pady=25, padx=10)


def list_customer_and_dishes(previous_window: tk.Toplevel):
    previous_window.destroy()
    window = tk.Toplevel(bg="#FDD9B5")
    sorted_customers = sorted(Orders.all_customers, key=lambda x: x.name, reverse=False)
    for index in range(len(sorted_customers)):
        tk.Label(window, text=f"{sorted_customers[index].name} замовив(-ла):", bg="#FDD9B5").grid(row=index, column=0,
                                                                                                  padx=10,
                                                                                                  pady=10)
        tk.Label(window, text=f"Сума до сплати: {sorted_customers[index].sum_to_pay}", bg="#FDD9B5").grid(row=index,
                                                                                                          column=2,
                                                                                                          padx=10,
                                                                                                          pady=10)
        new_listbox = tk.Listbox(window, width=100)
        for dish in sorted(sorted_customers[index].ordered_dishes, key=lambda x: x.name, reverse=False):
            new_listbox.insert(END, dish.name + '\n')
        new_listbox.grid(row=index, column=1, padx=30, pady=10)


def show_price_for_order(previous_window: tk.Toplevel, name_of_customer: tk.StringVar,  list_of_vars):
    previous_window.destroy()
    window = tk.Toplevel()
    answer = Orders.create_new_customer(name_of_customer.get())
    for var in list_of_vars:
        if var.get() and var.get() != "0":
            Orders.make_an_order(name_of_customer.get(), var.get())
    answer += f" До сплати: {Orders.sum_to_pay_customer(name_of_customer.get())} Євро"
    tk.Label(window, text=answer).grid(row=0, column=0)
    tk.Button(window, text="OK", command=window.destroy)


def process_of_canceling_dish(previous_window: tk.Toplevel, name_of_customer: tk.StringVar, name_of_dish: tk.StringVar):
    previous_window.destroy()
    window = tk.Toplevel()
    answer = Orders.cancel_ordering_dish(name_of_customer.get(), name_of_dish.get())
    tk.Label(window, text=answer).grid(row=0, column=0, padx=15, pady=15)
    tk.Button(window, text="OK", command=window.destroy).grid(row=1, column=1, padx=20, pady=20)


def process_of_searching_the_category(prev_window: tk.Toplevel, name_of_dish: tk.StringVar):
    prev_window.destroy()
    window = tk.Toplevel(bg="#FDD9B5")
    all_names = Food.search_for_category_name(name_of_dish.get())
    tk.Label(window, text="Знайдені категорії:", bg="#FDD9B5").grid(row=0, column=0, padx=10, pady=10)
    last_index = 0
    for index in range(len(all_names)):
        tk.Label(window, text=all_names[index], bg="#b4feff").grid(row=index + 1, column=1, padx=10, pady=10)
        last_index = index
    tk.Button(window, text="OK", command=window.destroy).grid(row=last_index+2, column=2, padx=20, pady=20)


def searching_for_category(previous_window: tk.Toplevel):
    previous_window.destroy()
    window = tk.Toplevel(bg="#FDD9B5")
    tk.Label(window, text="Введіть назву категорії:", bg="#FDD9B5").grid(row=0, column=0, padx=15, pady=15)
    name_category_var = tk.StringVar()
    tk.Entry(window, textvariable=name_category_var, width=25).grid(row=0, column=1, padx=10, pady=15)
    tk.Button(window, text="Знайти", bg="#FDD9B5",
              command=lambda: process_of_searching_the_category(window, name_category_var)).grid(row=1, column=1,
                                                                                                 padx=30, pady=30)


def process_of_searching_the_dish(prev_window: tk.Toplevel, name_of_dish: tk.StringVar):
    prev_window.destroy()
    window = tk.Toplevel(bg="#FDD9B5")
    array_with_dishes = Food.search_for_dish_name(name_of_dish.get())
    tk.Label(window, text="Знайдені страви:", bg="#FDD9B5").grid(row=0, column=0, padx=10, pady=10)
    last_index = 0
    for index in range(len(array_with_dishes)):
        tk.Label(window, text=array_with_dishes[index].get_dish_info, bg="#b4feff").grid(row=index + 1, column=1,
                                                                                         padx=10, pady=10)
        last_index = index
    tk.Button(window, text="OK", command=window.destroy).grid(row=last_index + 2, column=2, padx=20, pady=20)


def searching_for_dish(prev_window: tk.Toplevel):
    prev_window.destroy()
    window = tk.Toplevel(bg="#FDD9B5")
    tk.Label(window, text="Введіть назву страви:", bg="#FDD9B5").grid(row=0, column=0, padx=15, pady=15)
    name_dish_var = tk.StringVar()
    tk.Entry(window, textvariable=name_dish_var, width=25).grid(row=0, column=1, padx=10, pady=15)
    tk.Button(window, text="Знайти", bg="#FDD9B5",
              command=lambda: process_of_searching_the_dish(window, name_dish_var)).grid(row=1, column=1,
                                                                                         padx=30, pady=30)


def process_of_searching_customer(prev_window: tk.Toplevel, name_customer_search: tk.StringVar):
    prev_window.destroy()
    window = tk.Toplevel(bg="#FDD9B5")
    answer = Orders.search_for_name(name_customer_search.get())
    if answer:
        tk.Label(window, text=f"{name_customer_search.get()} замовив(-ла):",
                 bg="#FDD9B5").grid(row=0, column=0, padx=20, pady=25)
        index = 1
        for dish in answer:
            tk.Label(window, text=dish.get_dish_info, bg="#b4feff").grid(row=index, column=1, padx=15, pady=10)
            index += 1
    else:
        tk.Label(window, text="На жаль, такого замовника ми не знайшли", bg="#b4feff").grid(row=0, column=0,
                                                                                            padx=40, pady=40)


def searching_for_customer_name(prev_window: tk.Toplevel):
    prev_window.destroy()
    window = tk.Toplevel(bg="#FDD9B5")
    tk.Label(window, text="Введіть назву замовника:", bg="#FDD9B5").grid(row=0, column=0, padx=20, pady=15)
    name_customer_search = tk.StringVar()
    tk.Entry(window, textvariable=name_customer_search, width=25).grid(row=0, column=1, padx=5, pady=15)
    tk.Button(window, text="OK",
              command=lambda: process_of_searching_customer(window, name_customer_search)).grid(row=1, column=1,
                                                                                                padx=25, pady=30)


def ordering_window():
    inner_ordering_window = tk.Toplevel(bg="#FDD9B5")
    inner_ordering_window.geometry("500x550")
    inner_ordering_window.resizable(width=False, height=False)
    add_category_button = tk.Button(inner_ordering_window,
                                    command=lambda: creating_category_button(inner_ordering_window))
    add_category_button["text"] = "Створити категорію"
    add_category_button["bg"] = "#ADFF50"
    add_category_button["activebackground"] = "#DD7EFE"
    add_category_button.grid(row=0, column=0, padx=35, pady=35)
    add_new_dish_button = tk.Button(inner_ordering_window, command=lambda: adding_dish_button(inner_ordering_window))
    add_new_dish_button["text"] = "Додати нову страву"
    add_new_dish_button["bg"] = "#ADFF50"
    add_new_dish_button["activebackground"] = "#DD7EFE"
    add_new_dish_button.grid(row=1, column=0, padx=35, pady=35)
    change_information_button = tk.Button(inner_ordering_window, text="Змінити інформацію категорії/страви",
                                          command=lambda: changing_info_button(inner_ordering_window))
    change_information_button["bg"] = "#18FFEE"
    change_information_button["activebackground"] = "#DD7EFE"
    change_information_button.grid(row=2, column=0, padx=35, pady=35)
    delete_the_category_button = tk.Button(inner_ordering_window, text="Видалити категорію",
                                           command=lambda: deleting_category_button(inner_ordering_window))
    delete_the_category_button["activebackground"] = "#DD7EFE"
    delete_the_category_button["bg"] = "#FE7D70"
    delete_the_category_button.grid(row=1, column=2, padx=35, pady=35)
    delete_the_dish_button = tk.Button(inner_ordering_window, text="Видалити страву",
                                       command=lambda: deleting_dish_button(inner_ordering_window))
    delete_the_dish_button["activebackground"] = "#DD7EFE"
    delete_the_dish_button["bg"] = "#FE7D70"
    delete_the_dish_button.grid(row=2, column=2, padx=35, pady=35)
    see_list_of_food = tk.Button(inner_ordering_window, text="Список категорій та їхніх страв",
                                 command=lambda: list_of_food_button(inner_ordering_window))
    see_list_of_food["activebackground"] = "#DD7EFE"
    see_list_of_food["bg"] = "#18FFEE"
    see_list_of_food.grid(row=3, column=0, padx=35, pady=35)
    search_for_categories = tk.Button(inner_ordering_window, text="Пошук за категоріями", bg="#f8caff",
                                      command=lambda: searching_for_category(inner_ordering_window))
    search_for_categories.grid(row=4, column=0, columnspan=3, padx=35, pady=35)
    search_for_dishes = tk.Button(inner_ordering_window, text="Пошук за стравами", bg="#f8caff",
                                  command=lambda: searching_for_dish(inner_ordering_window))
    search_for_dishes.grid(row=5, column=0, columnspan=3, padx=35, pady=35)


def orders_manage_window():
    inner_window = tk.Toplevel(bg="#FDD9B5")
    inner_window.geometry("635x50")
    inner_window.resizable(width=False, height=False)
    manage_all_orders_button = tk.Button(inner_window, text="Видалити клієнта",
                                         command=lambda: delete_the_customer(inner_window))
    manage_all_orders_button["bg"] = "#FE7D70"
    manage_all_orders_button["activebackground"] = "#DD7EFE"
    manage_all_orders_button.grid(row=0, column=0, padx=15, pady=15)
    see_all_customers_dish_list_button = tk.Button(inner_window,
                                                   command=lambda: list_customer_and_dishes(inner_window))
    see_all_customers_dish_list_button.config(text="Переглянути список клієнтів та їхніх замовлених страв")
    see_all_customers_dish_list_button.config(activebackground="#DD7EFE", bg="#18FFEE")
    see_all_customers_dish_list_button.grid(row=0, column=1, padx=15, pady=15)
    search_for_customer_name = tk.Button(inner_window, text="Пошук замовлення", bg="#f8caff",
                                         command=lambda: searching_for_customer_name(inner_window))
    search_for_customer_name.config(activebackground="#DD7EFE")
    search_for_customer_name.grid(row = 0, column=2, padx=15, pady=15)


def make_an_order():
    window = tk.Toplevel(bg='#FDD9B5')
    tk.Label(window, text="Введіть ім'я замовника:", bg="#FDD9B5").grid(row=0, column=0, padx=10, pady=10)
    name_var = tk.StringVar()
    tk.Entry(window, textvariable=name_var, width=25).grid(row=0, column=1, padx=10, pady=10)
    tk.Label(window, text="Виберіть страви, які хочете замовити:", bg="#FDD9B5").grid(row=0, column=2, padx=10, pady=10)
    list_names_of_dish_vars = []
    counter = 0
    for category in Food.all_categories:
        for dish in category.list_of_dishes:
            list_names_of_dish_vars.append(tk.StringVar())
    for index_category in range(len(Food.all_categories)):
        for index_dish in range(len(Food.all_categories[index_category].sorted_dishes())):
            if Food.all_categories[index_category].sorted_dishes()[index_dish].amount > 0:
                name_of_dish = Food.all_categories[index_category].sorted_dishes()[index_dish].name
                var_text = f"{name_of_dish}, {Food.all_categories[index_category].sorted_dishes()[index_dish].price} Євро"
                new_button = tk.Checkbutton(window, text=var_text,
                                            variable=list_names_of_dish_vars[counter], onvalue=name_of_dish, offvalue=0)
                new_button.deselect()
                new_button.grid(row=counter, column=3)
                counter += 1
    tk.Button(window, text="Замовити",
              command=lambda: show_price_for_order(window, name_var, list_names_of_dish_vars)).grid(row=3, column=0,
                                                                                                    padx=10, pady=10)


def canceling_ordering_dish():
    window = tk.Toplevel(bg='#FDD9B5')
    tk.Label(window, text="Введіть ім'я замовника:", bg="#FDD9B5").grid(row=0, column=0, padx=10, pady=10)
    name_var = tk.StringVar()
    tk.Entry(window, textvariable=name_var, width=25).grid(row=0, column=1, padx=10, pady=10)
    tk.Label(window, text="Введіть назву страви, яку хочете скасувати:", bg="#FDD9B5").grid(row=0, column=2,
                                                                                            padx=10, pady=10)
    dish_var = tk.StringVar()
    tk.Entry(window, textvariable=dish_var, width=25).grid(row=0, column=3, padx=10, pady=10)
    tk.Button(window, text="Скасувати замовлення", bg="#FE7D70",
              command=lambda: process_of_canceling_dish(window, name_var, dish_var)).grid(row=1, column=0,
                                                                                          columnspan=4, pady=20)


root = tk.Tk()
root['bg'] = '#FDD9B5'
root.title("Ресторан")
root.geometry('800x200')
root.resizable(width=False, height=False)
tk.Label(root, text="Форматування меню:", bg="#FDD9B5").grid(row=0, column=0, padx=25, pady=25)
tk.Label(root, text="Замовлення: ", bg="#FDD9B5").grid(row=1, column=0, rowspan=2, padx=25, pady=25)
order_button = tk.Button(root, text="Налаштування меню", activebackground="#1410fa", command=ordering_window)
order_button.grid(row=0, column=1, columnspan=3, padx=5, pady=25)
orders_manage_button = tk.Button(root, text="Управління замовленнями", command=orders_manage_window)
orders_manage_button.config(activebackground="#1410fa")
orders_manage_button.grid(row=1, column=1, padx=10, pady=25)
make_an_order_button = tk.Button(root, text="Зробити замовлення", command=make_an_order)
make_an_order_button.config(activebackground="#1410fa")
make_an_order_button.grid(row=1, column=2, padx=10, pady=25)
cancel_an_order_button = tk.Button(root, text="Скасувати замовлення страви", command=canceling_ordering_dish)
cancel_an_order_button.config(activebackground="#1410fa")
cancel_an_order_button.grid(row=1, column=3, padx=10, pady=25)

tk.mainloop()
