from bs4 import BeautifulSoup as bs
import codecs

#открытие файла
doc = bs(codecs.open('karta.html', encoding='utf-8', mode='r').read(), 'html.parser')

#извлечение данных со страницы
author = doc.select('.author')[0].decode_contents().strip()
title1 = doc.select('.title')[0].decode_contents().strip()
title2 = doc.select('.podtitle')[0].decode_contents().strip()

#вывод на экран
print('Автор:', author)
print('Заголовок:', title1)
print('Подзаголовок:', title2)

#извлечение данных о разделах на странице
tegs = []
for node in doc.select('.text'):
    text = doc.select('.text')[0].decode_contents().strip()
    tegs.append({'text': text})

#извлечение данных о списках на странице
lists = []
for node in doc.select('ul'):
    list = doc.select('ul')[0].decode_contents().strip()
    lists.append({'list': list})

#извлечение данных об элементах на странице
els = []
for node in doc.select('li'):
    el = doc.select('li')[0].decode_contents().strip()
    els.append({'el': el})

#вывод информации на экран
print('Количество разделов на странице: ', len(tegs))
print('Количество списков на странице: ', len(lists))

#самый маленький раздел
print('Самый большой раздел:', sorted(tegs, key=lambda x: len(x['text']))[0]['text'])

print('Самый большой элемент списка:', sorted(els, key=lambda x: len(x['el']))[0]['el'])
