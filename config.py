import os

BASE_URL = "https://www.e1.ru"  # url для построения адреса ссылки
URL = "https://www.e1.ru/text/"  # url раздела "Все новости" сайта e1
BASE_DIR = os.getcwd()
PAGES = range(1, 10)  # число страниц для парсинга
SLEEP_TIME = 0.05  # время для функции sleep
