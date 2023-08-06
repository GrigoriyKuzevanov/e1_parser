import os

BASE_URL = "https://www.e1.ru"  # url для построения адреса ссылки
URL = "https://www.e1.ru/text/"  # url раздела "Все новости" сайта e1
OUTPUT_DATA_DIR = os.getcwd() + '/data_files/output_e1.xlsx'
PAGES = range(1, 10)  # число страниц для парсинга
SLEEP_TIME = 0.05  # время для функции sleep
