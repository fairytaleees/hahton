from hahaton1 import listing, retrieve, create, update, delete

def important():
    print('Привет! Тебе доступны следующие функции интернет маркета:\n\tLIST-1\n\tDETAIL-2\n\tCREATE-3\n\tUPDATE-4\n\tDELETE-5')
    choice = input('Введите действие(1,2,3,4,5): ')

    if choice.strip() == '1':
        print(listing())
    elif choice.strip() == '2':
        print(retrieve())
    elif choice.strip() == '3':
        print(create())
    elif choice.strip() == '4':
        print(update())
    elif choice.strip() == '5':
        print(delete())
    else:
        print('Надо выбрать нормально, не тупи!')

    answer = input('Хотите продолжить?(yes/no)')
    if answer.lower().strip() == 'yes':
        important()
    else:
        print('bay bay babe!!')

important()