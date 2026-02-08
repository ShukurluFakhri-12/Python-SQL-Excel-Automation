import logging
import pandas as pd
import sqlite3
import requests

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--limit', type=int, default=5)
parser.add_argument('--file' , default='review.xlsx')
parser.add_argument('--only-excel', action='store_true')
args = parser.parse_args()


logging.basicConfig(filename='tracker.log', level=logging.INFO, 
                    format='%(asctime)s | %(levelname)s | %(message)s')

base = sqlite3.connect('tracker.db')
editor = base.cursor()
editor.execute('CREATE TABLE IF NOT EXISTS news (id TEXT PRIMARY KEY, title TEXT, link TEXT)')
logging.info('Base has successfully been created')

def data_draw():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url, timeout=4)
    data = response.json()
    cleaned_set = []
    for x in data[:args.limit]:
        new_format = {'id': x['id'], 'title': x['title'], 'link': x['body']}
        cleaned_set.append(new_format)
    logging.info(f'The number of data taken from API: {len(cleaned_set)}')
    return cleaned_set

def writing_to_base(newslist):
    for y in newslist:
        editor.execute(f"INSERT OR IGNORE INTO news VALUES ('{y['id']}', '{y['title']}', '{y['link']}')")
    base.commit()
    logging.info('Data were moved to the base')

def export_to_excel():
    df = pd.read_sql('SELECT * FROM news', base)
    df.to_excel(args.file, index=False)
    logging.info('Excel file has been created')

try:
    if not args.only_excel:
        received_data = data_draw()      
        writing_to_base(received_data)
    export_to_excel()               
    print(f"Uğurla tamamlandı! Fayl adı: {args.file}")
except Exception as e:
    logging.error(f"Error occurred: {e} ")
    print(f"Error: {e}")

base.close()
