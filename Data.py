def room_4():  # Функция 4-й комнаты.
    print('Hello! How are U?')
    text = input().lower()
    if text in ('fine', 'ok', "I'm fine"):
        print("It's so perfect!")
        return True  # Продолжить стандартным вводом
    else:
        print("Fuck up!")
        print('You died :(')
        return False


def room_5():  # Функция 5-й комнаты.
    print("It's the end.")
    return False  # Не вызывать стандартный ввод


next_room_text = 'Выберете следующую комнату'
flag_texts = {
    'cry_flag_1': 'Ты нашёл этот флаг',
    'cry_flag_2': 'Этот тоже'
}
dct_main = [
    (1, 'Текст первой комнаты', {'n': 2}, {'cry': 'cry_flag_1'}),
    (2, 'Текст второй комнаты', {'s': 1, 'n': 3, 'w': 4}, {'cry': 'cry_flag_2'}),
    (3, 'Текст третьей комнаты', {'s': 2}, {}),
    (4, 'Текст четвёртой комнаты', {'e': 2, 'n': 5}, {}, room_4),
    (5, 'Текст пятой комнаты', {'s': 4}, {}, room_5)
]
