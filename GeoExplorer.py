import os
import json
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Относительный путь к файлам
cwd = os.getcwd()
dirname = os.path.dirname(__file__)

file_city = os.path.join(dirname, 'json/cities.json')
file_capital = os.path.join(dirname, 'json/capital.json')
file_languages = os.path.join(dirname, 'json/country-by-languages.json')
file_continent = os.path.join(dirname, 'json/country-by-continent.json')
file_currency = os.path.join(dirname, 'json/country-by-currency-name.json')
file_government = os.path.join(dirname, 'json/country-by-government-type.json')
file_dish = os.path.join(dirname, 'json/country-by-national-dish.json')
file_symbol = os.path.join(dirname, 'json/country-by-national-symbol.json')
file_population = os.path.join(dirname, 'json/country-by-population.json')
file_region = os.path.join(dirname, 'json/country-by-region-in-world.json')
file_religion = os.path.join(dirname, 'json/country-by-religion.json')
file_temperature = os.path.join(dirname, 'json/country-by-yearly-average-temperature.json')
file_calling = os.path.join(dirname, 'json/country-by-calling-code.json')

with open(file_city, encoding="utf-8") as cities:
    city_dict = json.load(cities)

with open(file_capital, encoding="utf-8") as cities:
    countries_dict = json.load(cities)

with open(file_languages, encoding="utf-8") as cities:
    country_by_languages_dict = json.load(cities)

with open(file_continent, encoding="utf-8") as cities:
    country_by_continent_dict = json.load(cities)

with open(file_currency, encoding="utf-8") as cities:
    country_by_currency_name_dict = json.load(cities)

with open(file_government, encoding="utf-8") as cities:
    country_by_government_type_dict = json.load(cities)

with open(file_dish, encoding="utf-8") as cities:
    country_by_national_dish_dict = json.load(cities)

with open(file_symbol, encoding="utf-8") as cities:
    country_by_national_symbol_dict = json.load(cities)

with open(file_population, encoding="utf-8") as cities:
    country_by_population_dict = json.load(cities)

with open(file_region, encoding="utf-8") as cities:
    country_by_region_in_world_dict = json.load(cities)

with open(file_religion, encoding="utf-8") as cities:
    country_by_religion_dict = json.load(cities)

with open(file_temperature, encoding="utf-8") as cities:
    country_by_yearly_average_temperature_dict = json.load(cities)

with open(file_calling, encoding="utf-8") as cities:
    country_by_calling_code_dict = json.load(cities)


# Абсолютный путь к файлам

# with open(r"""C:\Users\kiris\OneDrive\Desktop\Python project\Проекты\Города и страны Tkinter\cities.json""", encoding="utf-8") as cities:
#     city_dict = json.load(cities)

# with open(r"""C:\Users\kiris\OneDrive\Desktop\Python project\Проекты\Города и страны Tkinter\capital.json""", encoding="utf-8") as capital:
#     countries_dict = json.load(capital)

# with open(r"""C:\Users\kiris\OneDrive\Desktop\Python project\Проекты\Города и страны Tkinter\json\country-by-languages.json""", encoding="utf-8") as country_by_languages:
#     country_by_languages_dict = json.load(country_by_languages)

# with open(r"""C:\Users\kiris\OneDrive\Desktop\Python project\Проекты\Города и страны Tkinter\json\country-by-continent.json""", encoding="utf-8") as country_by_continent:
#     country_by_continent_dict = json.load(country_by_continent)

# with open(r"""C:\Users\kiris\OneDrive\Desktop\Python project\Проекты\Города и страны Tkinter\json\country-by-currency-name.json""", encoding="utf-8") as country_by_currency_name:
#     country_by_currency_name_dict = json.load(country_by_currency_name)

# with open(r"""C:\Users\kiris\OneDrive\Desktop\Python project\Проекты\Города и страны Tkinter\json\country-by-government-type.json""", encoding="utf-8") as country_by_government_type:
#     country_by_government_type_dict = json.load(country_by_government_type)

# with open(r"""C:\Users\kiris\OneDrive\Desktop\Python project\Проекты\Города и страны Tkinter\json\country-by-national-dish.json""", encoding="utf-8") as country_by_national_dish:
#     country_by_national_dish_dict = json.load(country_by_national_dish)

# with open(r"""C:\Users\kiris\OneDrive\Desktop\Python project\Проекты\Города и страны Tkinter\json\country-by-national-symbol.json""", encoding="utf-8") as country_by_national_symbol:
#     country_by_national_symbol_dict = json.load(country_by_national_symbol)

# with open(r"""C:\Users\kiris\OneDrive\Desktop\Python project\Проекты\Города и страны Tkinter\json\country-by-population.json""", encoding="utf-8") as country_by_population:
#     country_by_population_dict = json.load(country_by_population)

# with open(r"""C:\Users\kiris\OneDrive\Desktop\Python project\Проекты\Города и страны Tkinter\json\country-by-region-in-world.json""", encoding="utf-8") as country_by_region_in_world:
#     country_by_region_in_world_dict = json.load(country_by_region_in_world)

# with open(r"""C:\Users\kiris\OneDrive\Desktop\Python project\Проекты\Города и страны Tkinter\json\country-by-religion.json""", encoding="utf-8") as country_by_religion:
#     country_by_religion_dict = json.load(country_by_religion)

# with open(r"""C:\Users\kiris\OneDrive\Desktop\Python project\Проекты\Города и страны Tkinter\json\country-by-yearly-average-temperature.json""", encoding="utf-8") as country_by_yearly_average_temperature:
#     country_by_yearly_average_temperature_dict = json.load(country_by_yearly_average_temperature)

# with open(r"""C:\Users\kiris\OneDrive\Desktop\Python project\Проекты\Города и страны Tkinter\json\country-by-calling-code.json""", encoding="utf-8") as country_by_calling_code_dict:
#     country_by_calling_code_dict = json.load(country_by_calling_code_dict)


# Cоздаём класс MultiPageApp, который наследуется от tk.Tk — это главное окно программы.
# class MultiPageApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("GeoExplorer")
#         self.geometry("900x600")  # Размер по умолчанию
#         self.minsize(400, 300)   # Минимальный размер
#         self.configure(bg="#687373")  # Светло-серый фон
#         self.attributes('-alpha', 0.9)
#
#         # Контейнер для фреймов (страниц)
#         container = tk.Frame(self)
#         container.pack(side="top", fill="both", expand=True)
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)
#
#         # Словарь для хранения фреймов
#         self.frames = {}
#
#         # Создаем страницы
#         for F in (StartPage, Page1, Page2, Page3):
#             frame = F(container, self)
#             self.frames[F] = frame
#             frame.grid(row=0, column=0, sticky="nsew")
#
#         # Кнопки для навигации
#         self.show_frame(StartPage)
#
#         # Панель с кнопками (можно разместить где угодно)
#         button_frame = tk.Frame(self)
#         button_frame.pack(side="bottom", fill="x")
#
#         btn1 = tk.Button(button_frame, text="Главная", font=("Arial", 12), bg='#3b3e3f', fg="#f6f7f7",
#                          command=lambda: self.show_frame(StartPage))
#         btn1.pack(side="bottom", padx=0, pady=50)
#
#         btn2 = tk.Button(button_frame, text="Страны", font=("Arial", 12), bg='#3b3e3f', fg="#f6f7f7",
#                          command=lambda: self.show_frame(Page1))
#         btn2.pack(side="bottom", padx=0, pady=50)
#
#         btn3 = tk.Button(button_frame, text="Воды", font=("Arial", 12), bg='#3b3e3f', fg="#f6f7f7",
#                          command=lambda: self.show_frame(Page2))
#         btn3.pack(side="bottom", padx=0, pady=50)
#
#         btn3 = tk.Button(button_frame, text="Горы", font=("Arial", 12), bg='#3b3e3f', fg="#f6f7f7",
#                          command=lambda: self.show_frame(Page3))
#         btn3.pack(side="bottom", padx=0, pady=50)
#
#     def show_frame(self, cont):
#         """Показывает выбранный фрейм"""
#         frame = self.frames[cont]
#         frame.tkraise()
#
#
# # Классы для разных страниц
# class StartPage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="GeoExplorer", font=("Arial", 12))
#         label.pack(pady=10, padx=10)
#
#
# class Page1(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="Страница 1")
#         label.pack(pady=10, padx=10)
#
#
# class Page2(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="Страница 2")
#         label.pack(pady=10, padx=10)
#
# class Page3(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="Страница 2")
#         label.pack(pady=10, padx=10)


# parent — это контейнер, в который помещается страница.
# controller — ссылка на главное окно (можно использовать для вызова show_frame из самой страницы).

window = tk.Tk()
# window = Tk()
window.title("GeoExplorer")
window.geometry('1200x800')
window['bg'] = "#505353"
window.wait_visibility(window)
window .wm_attributes('-alpha', 0.9)

for theme in ttk.Style().theme_names():
    print(theme) # Получение доступных тем

current_theme = ttk.Style().theme_use()
print(current_theme) # Получение текущей темы

# --- Первый фрейм ---
frame1 = Frame(window, bg="#ffffff")
frame1.place(relx=0.15, rely=0.10, relheight=0.3, relwidth=0.7)

city_text = Label(frame1, text='Все города страны:', font=("Arial", 15), bg="#ffffff")
city_text.pack(anchor="s", padx=10, pady=10)

city_input = Entry(frame1, bg="#e6e6e6", fg='#000000', width=30, font=20)
city_input.pack()

country_text = Label(frame1, text='О стране:', font=("Arial", 15), bg="#ffffff")
country_text.pack(anchor="s", padx=10, pady=10)

country_input = Entry(frame1, bg="#e6e6e6", fg='#000000', width=30, font=20)
country_input.pack()

# --- Второй фрейм ---
frame_list = tk.Frame(window, width=1050, height=1000, bg="#ffffff")
frame_list.place(relx=0.15, rely=0.47, relheight=0.5, relwidth=0.7)
frame_list.pack_propagate(False)

scrollbar = tk.Scrollbar(frame_list)
scrollbar.pack(side="right", fill="y")

city_listbox = tk.Listbox(frame_list, yscrollcommand=scrollbar.set, font=("Arial", 13), bg="#ffffff", width=120,  height=250, justify='left', selectbackground='#505353', selectforeground='White', activestyle='none')
city_listbox.pack(fill="both", expand=True)
scrollbar.config(command=city_listbox.yview)

# --- Третий фрейм ---
frame3 = Frame(window, bg='#505353')
frame3.place(relx=0, rely=0.40, relheight=0.07, relwidth=0.5)

# --- Четвертый фрейм ---
frame4 = Frame(window, bg='#505353')
frame4.place(relx=0.5, rely=0.40, relheight=0.07, relwidth=0.5)

# --- Логика ---

# Очистка полей
def clear_all_frame():
    city_listbox.delete(0, tk.END)
    city_input.delete(0, tk.END)
    country_input.delete(0, tk.END)

clear_button = Button(frame3, width=10, height=30, text='Очистить', font=("Arial", 12), bg='#08f', fg='#fff', borderwidth="0", highlightthickness='0', cursor='hand2', command=clear_all_frame)
def focus_in(e):
    clear_button.configure(fg='#08f', bg='#fff')  # При наведении: синий текст, белый фон

def focus_out(e):
    clear_button.configure(fg='#f6f7f7', bg='#08f')  # Исходный стиль: белый текст, синий фон

# Привязка событий
clear_button.bind('<Enter>', focus_in)    # При наведении курсора
clear_button.bind('<Leave>', focus_out)    # При уходе курсора

clear_button.pack(padx=30, pady=12, anchor='e')

# Вывод городов
def cities_of_the_country(event=None):
    city_listbox.delete(0, tk.END)  # очистка
    country = city_input.get().strip()
    if country in city_dict:
        for city in city_dict[country]:
            city_listbox.insert(tk.END, city)
    # else:
    #     output_label.config("Страна не найдена.")

city_input.bind("<Return>", cities_of_the_country)

# О стране
country_map = {item['country'].lower(): item['city'] for item in countries_dict}
country_languages = {item['country'].lower(): ", ".join(item['languages']) for item in country_by_languages_dict}
country_continent = {item['country'].lower(): item['continent'] for item in country_by_continent_dict}
country_currency = {item['country'].lower(): item['currency_name'] for item in country_by_currency_name_dict}
country_government = {item['country'].lower(): item['government'] for item in country_by_government_type_dict}
country_dish = {item['country'].lower(): item['dish'] for item in country_by_national_dish_dict}
country_symbol = {item['country'].lower(): item['symbol'] for item in country_by_national_symbol_dict}
country_population = {item['country'].lower(): item['population'] for item in country_by_population_dict}
country_region = {item['country'].lower(): item['location'] for item in country_by_region_in_world_dict}
country_religion = {item['country'].lower(): item['religion'] for item in country_by_religion_dict}
country_temperature = {item['country'].lower(): item['temperature'] for item in country_by_yearly_average_temperature_dict}
country_calling = {item['country'].lower(): item['calling_code'] for item in country_by_calling_code_dict}

def capital_of_the_country(event=None):
    city_listbox.delete(0, tk.END)  # очистить список
    country = country_input.get().strip().lower()
    capital = country_map.get(country)
    languages = country_languages.get(country)
    continent = country_continent.get(country)
    currency = country_currency.get(country)
    government = country_government.get(country)
    dish = country_dish.get(country)
    symbol = country_symbol.get(country)
    population = country_population.get(country)
    region = country_region.get(country)
    religion = country_religion.get(country)
    temperature = country_temperature.get(country)
    calling = country_calling.get(country)


    if capital:
        city_listbox.insert(tk.END, f"Столица: {capital}")
        #city_listbox.insert(tk.END, f"Столица {country_input.get().strip().capitalize()}: {capital}")
    if languages:
        city_listbox.insert(tk.END, f"Языки: {languages}")
    if continent:
        city_listbox.insert(tk.END, f"Континент: {continent}")
    if currency:
        city_listbox.insert(tk.END, f"Валюта: {currency}")
    if currency:
        city_listbox.insert(tk.END, f"Тип правительства: {government}")
    if currency:
        city_listbox.insert(tk.END, f"Национальная еда: {dish}")
    if currency:
        city_listbox.insert(tk.END, f"Национальный символ: {symbol}")
    if currency:
        city_listbox.insert(tk.END, f"Популяция: {population}")
    if currency:
        city_listbox.insert(tk.END, f"Регион мира: {region}")
    if currency:
        city_listbox.insert(tk.END, f"Религия: {religion}")
    if currency:
        city_listbox.insert(tk.END, f"Среднегодовая температура: {temperature}")
    if currency:
        city_listbox.insert(tk.END, f"Код телефонного номера: {calling}")

    else:
        city_listbox.insert(tk.END, "Страна не найдена.")

country_input.bind("<Return>", capital_of_the_country)

# --- Кнопка всех стран ---
def all_country():
    city_listbox.delete(0, tk.END)
    for country in city_dict.keys():
        city_listbox.insert(tk.END, country)

all_country_button = Button(
    frame1,
    text='Список всех стран',
    font=("Arial", 12),
    borderwidth=1,
    relief='ridge',
    activeforeground="#111111",
    fg="#f6f7f7",
    bg="#08f",  # Добавляем фоновый цвет
    highlightthickness=0,
    cursor='hand2',
    command=all_country,
    height=15
)
# Функции для изменения стиля при наведении
def focus_in(e):
    all_country_button.configure(fg='#08f', bg='#fff')  # При наведении: синий текст, белый фон

def focus_out(e):
    all_country_button.configure(fg='#f6f7f7', bg='#08f')  # Исходный стиль: белый текст, синий фон

# Привязка событий
all_country_button.bind('<Enter>', focus_in)    # При наведении курсора
all_country_button.bind('<Leave>', focus_out)    # При уходе курсора

all_country_button.pack(padx=10, pady=30)

# --- Копирование из фрейма в буфер ---
def copy_to_frame():
    data = "\n".join(city_listbox.get(0, tk.END))
    city_listbox.clipboard_clear() # Очищает буфер обмена
    city_listbox.clipboard_append(data)

copy_frame_button = Button(frame4, width=10, height=30,text='Копировать', font=("Arial", 12), borderwidth="0", activeforeground="#111111",bg="#08f",fg="#f6f7f7", highlightthickness='0', cursor='hand2', command=copy_to_frame)
def focus_in(e):
    copy_frame_button.configure(fg='#08f', bg='#fff')  # При наведении: синий текст, белый фон

def focus_out(e):
    copy_frame_button.configure(fg='#f6f7f7', bg='#08f')  # Исходный стиль: белый текст, синий фон

# Привязка событий
copy_frame_button.bind('<Enter>', focus_in)    # При наведении курсора
copy_frame_button.bind('<Leave>', focus_out)    # При уходе курсора

copy_frame_button.pack(padx=30, pady=12, anchor='w')


# app = MultiPageApp()
# app.mainloop()


window.mainloop()



