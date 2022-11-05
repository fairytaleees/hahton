import json
from decimal import Decimal

FILE_PATH = '/home/ayana/Desktop/hahaton/haha.json '
ID_FILE_PATH = '/home/ayana/Desktop/hahaton//id.txt'

def get_data():
    with open(FILE_PATH) as file:
        return json.load(file)

def save_data(data):
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)


def listing():
    data = get_data()
    return f'Список всех товаров: {data}'

def retrieve():
    data = get_data()
    try:
        id = int(input('Введите id продукта: '))
        product = list(filter(lambda x: id == x['id'], data))
        return product[0]
    except:
        return 'Неверный id!'


def get_id():
    with open(ID_FILE_PATH, 'r') as file:
        id = int(file.read())
        id += 1
    with open(ID_FILE_PATH, 'w') as file:
        file.write(str(id))
        return id

def create():
    data = get_data()
    try:
        product = {
        'id': get_id(),
        'title': input('Введите марку продукта: '),
        'model': input('Введите модель продукта: '),
        'year' : int(input('Введите год выпуска: ')),
        'description': input('Введите описание: '),
        'price': round(float(input('Введите цену продукта: ')),2)
        }
    except:
        return 'Неверные данные!'

    data.append(product)
    save_data(data)
    return 'Создан новый товар!'



def update():
    data = get_data()
    try:
        id = int(input('Введите id продукта: '))
        product = list(filter(lambda x: x['id'] == id, data))[0]
        print(f'Товар для обновления: {product["title"]}')
    except:
        return 'Неверный id!'

    index = data.index(product)
    choice = input('Что вы хотите изменить?(1-title, 2-model, 3-year, 4-description, 5-price): ')
    if choice.lower().strip() == '1':
        data[index]['title'] = input('Введите новое название марки: ')
    elif choice.lower().strip() == '2':
        data[index]['model'] = input('Введите новое название модели: ')
    elif choice.strip() == '3':
        try:
            data[index]['year'] = int(input('Введите новый год для товара: '))
        except:
            return 'Неверное значение для цены!'
    elif choice.strip() == '4':
        data[index]['description'] = input('Введите новое описание для товара: ')
    elif choice.strip() == '5':
        try:
            data[index]['price'] = round(float(input('Введите новую цену для товара: ')),2)
        except:
            return 'Неверное значение для цены!'
    else:
        return 'Неверные значение для обновления!'

    save_data(data)
    return 'Товар обновлен!'

def delete():
    data = get_data()
    try:
        id = int(input('Введите id продукта: '))
        product = list(filter(lambda x: x['id'] == id, data))[0] 
        print(f'Товар для удаления {product["title"]}')
    except:
        return 'Неверный id!'
    
    choice = input('Удалить этот товар(yes/no)? ')
    if choice.lower().strip() != 'yes':
        return 'Товар не удален!'
    data.remove(product)
    save_data(data)
    return 'Товар удален!'