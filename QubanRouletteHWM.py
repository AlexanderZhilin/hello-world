t = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
     '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
     '28', '29', '30', '31', '32', '33', '34', '35', '36', '0',
     '00']  # Создаем список всех возможных чисел
listdrop = []  # Создаем список всех выпавших чисел
list10_15 = []  # Создаем список для хранения положительных и отрицательных исходов 10-15
list28_33 = []  # Создаем список для хранения положительных и отрицательных исходов 28-33
list2Column = []  # Создаем список для хранения положительных и отрицательных исходов 2Column
listRED = []  # Создаем список для хранения положительных и отрицательных исходов RED
listwin_lose = []  # Создаем список для хранения выигранных и проигранных сумм


def fun():
    n_stavok_list10_15 = int(input(f'Введите число ставок на 10-15 или 0, чтобы не использовать эти ставки:'))
    n_stavok_list28_33 = int(input(f'Введите число ставок на 28-33 или 0, чтобы не использовать эти ставки:'))
    n_stavok_list2Column = int(input(f'Введите число ставок на 2Column или 0, чтобы не использовать эти ставки:'))
    n_stavok_listRED = int(input(f'Введите число ставок на RED или 0, чтобы не использовать эти ставки:'))
    stavka = int(input(f'Ваша ставка:'))
    if (n_stavok_list10_15 and n_stavok_list28_33 and n_stavok_list2Column
        and n_stavok_listRED) not in range(1, 30) or stavka not in range(1, 100000):
        print('Число ставок должно быть в пределах от 1 до 30, а ставка от 1 до 100 000')
        return fun()
    else:
        # print(f'{listdrop} - список всех выпавших чисел')
        # print(f'{listwin_lose} - список выигрышей и проигрышей')
        print(f'{sum(listwin_lose)} - сумма выигрышей и проигрышей')
        print(f'{list10_15} - список выпавших 10-15, где 0 - положительный исход, а 1 -отрицательный')
        print(f'{list28_33} - список выпавших 28-33, где 0 - положительный исход, а 1 -отрицательный')
        print(f'{list2Column} - список выпавших 2Column, где 0 - положительный исход, а 1 -отрицательный')
        print(f'{listRED} - список выпавших RED, где 0 - положительный исход, а 1 -отрицательный')

        if sum(list10_15[-(n_stavok_list10_15):]) <= (
                n_stavok_list10_15 - 1):  # сумма списка от конца до N-ого элемента с конца
            print(f'Увеличиваем ставку на 10-15')
        else:
            list10_15.clear()
            x1 = -((((6 / (6 - 1)) ** (n_stavok_list10_15 - 1)) * stavka * 6) - (
                    stavka * 5))  # где 6 это коэф выигрыша равный 36/(6 занимаемых цифр)
            listwin_lose.append(int(x1))
            print(f'Мы проиграли {round(x1, )} ставя на 10-15')

        if sum(list28_33[-(n_stavok_list28_33):]) <= (
                n_stavok_list28_33 - 1):  # сумма списка от конца до 5ого элемента с конца
            print(f'Увеличиваем ставку на 28-33')
        else:
            list28_33.clear()
            x2 = -((((6 / (6 - 1)) ** (n_stavok_list28_33 - 1)) * stavka * 6) - (
                    stavka * 5))  # где 6 это коэф выигрыша равный 36/(6 занимаемых цифр)
            listwin_lose.append(int(x2))
            print(f'Мы проиграли {round(x2, )} ставя на 28-33')

        if sum(list2Column[-(n_stavok_list2Column):]) <= (
                n_stavok_list2Column - 1):  # сумма списка от конца до 5ого элемента с конца
            print(f'Увеличиваем ставку на 2Column')
        else:
            list2Column.clear()
            x3 = -((((3 / (3 - 1)) ** (n_stavok_list2Column - 1)) * stavka * 3) - (
                    stavka * 2))  # где 3 это коэф выигрыша равный 36/(12 занимаемых цифр)
            listwin_lose.append(int(x3))
            print(f'Мы проиграли {round(x3, )} ставя на 2Column')

        if sum(listRED[-(n_stavok_listRED):]) <= (
                n_stavok_listRED - 1):  # сумма списка от конца до 5ого элемента с конца
            print(f'Увеличиваем ставку на RED')
        else:
            listRED.clear()
            x4 = -((((2 / (2 - 1)) ** (n_stavok_listRED - 1)) * stavka * 2) - (
                    stavka * 1))  # где 2 это коэф выигрыша равный 36/(18 занимаемых цифр)
            listwin_lose.append(int(x4))
            print(f'Мы проиграли {round(x4, )} ставя на RED')

        number = input('Введите Q для выхода из программы или введите новое число:')

        if number == 'Q' or number == 'q':
            return False

        elif number in t:
            listdrop.append(int(number))

            if number in ['10', '11', '12', '13', '14', '15']:
                list10_15.append(0)
                listwin_lose.append(int(stavka * 5))  # 5 это 36/6 - 1(чистый выигрыш)
                print(f'Выиграли чистыми {stavka * 5} ставя на 10-15')
            elif number in ['0', '00', '1', '2', '3', '4', '5', '6', '7', '8', '9', '16', '17', '18', '19', '20', '21',
                            '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36']:
                list10_15.append(1)

            if number in ['28', '29', '30', '31', '32', '33']:
                list28_33.append(0)
                listwin_lose.append(int(stavka * 5))  # 5 это 36/6 - 1(чистый выигрыш)
            elif number in ['0', '00', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
                            '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '34', '35', '36']:
                list28_33.append(1)

            if number in ['2', '5', '8', '11', '14', '17', '20', '23', '26', '29', '32', '35']:
                list2Column.append(0)
                listwin_lose.append(int(stavka * 2))  # 2 это 36/12 - 1(чистый выигрыш)
            elif number in ['0', '00', '1', '3', '4', '6', '7', '9', '10', '12', '13', '15', '16', '18', '19', '21',
                            '22',
                            '24', '25', '27', '28', '30', '31', '33', '34', '36']:
                list2Column.append(1)

            if number in ['1', '3', '5', '7', '9', '12', '14', '16', '18', '19', '21', '23', '25', '27', '30', '32',
                          '34',
                          '36']:
                listRED.append(0)
                listwin_lose.append(int(stavka * 1))  # 1 это 36/18 - 1(чистый выигрыш)
            elif number in ['0', '00', '2', '4', '6', '8', '10', '11', '13', '15', '17', '20', '22', '24', '26', '28',
                            '29',
                            '31', '33', '35']:
                listRED.append(1)
            return fun()

        else:
            print('Ошибка! Неверный ввод.')
            return fun()


fun()
