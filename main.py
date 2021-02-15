from Labirint import Data


def print_room(text):
    print(text)


def input_room(text):
    print(f'{Data.next_room_text} ({", ".join(text)})')
    text_input = input().lower()
    while text_input and text_input not in text:
        print_room('NameError')
        text_input = input().lower()
    return text_input


def next_room(out_numbers, flags):

    # Вывод текста и вариантов ответа.

    text_input = input_room(list(out_numbers.keys()) + list(flags.keys()))

    if text_input:

        if text_input in out_numbers.keys():
            dct_rooms_numbers[str(out_numbers[text_input])].start()  # Вызов комнаты из словаря по изначению комнаты.

        else:
            if not dct_flags[flags[text_input]]:
                dct_flags[flags[text_input]] = True
                print_room(Data.flags[flags[text_input]])
            else:
                print_room('Если тут что-то и было, это забрали')
            next_room(out_numbers, flags)

    else:
        print('Bye!')


dct_rooms_numbers = {}  # Словарь {номер комнаты: объект класса Rooms}.
dct_flags = {}


class Rooms:

    def __init__(self, number, out_numbers, flags=None, function=lambda: True):
        if flags is None:
            flags = {}

        if flags:
            for i in flags.values():
                if i not in dct_flags.keys():
                    dct_flags.update({i: False})

        self.number = str(number)  # Строка номера комнаты.
        self.out_numbers = out_numbers
        self.flags = flags
        # Словарь {направление: ссылка на объект}.
        self.function = function
        global dct_rooms_numbers
        dct_rooms_numbers.update({self.number: self})

    def start(self):
        print_room(Data.text_room[self.number])
        if self.function():  # Вызываем функцию текущей комнаты, если не была передана, вызываем пустую.
            next_room(self.out_numbers, self.flags)  # Ввод и переход к следующей комнате.


def room_4():  # Функция 4-й комнаты.
    print('Hello! How are U?')
    input()
    print('Ok!')
    return True  # Продолжить стандартным вводом


def room_5():
    print("It's the end.")
    return False  # Не вызывать стандартный ввод


Rooms(1, {'n': 2}, {'cry': 'cry_flag_1'})
Rooms(2, {'s': 1, 'n': 3, 'w': 4}, {'cry': 'cry_flag_2'})
Rooms(3, {'s': 2})
Rooms(4, {'e': 2, 'n': 5}, function=room_4)
Rooms(5, {'s': 4}, function=room_5)
dct_rooms_numbers['1'].start()
