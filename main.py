from Labirint import Data


def print_room(text):
    print(text)


def input_room(text, out_numbers):
    print(f'{text} ({", ".join(sorted(out_numbers.keys()))})')  # Вывод текста и вариантов ответа.
    text_input = input().lower()
    if text_input:
        if text_input in out_numbers.keys():
            dct_rooms_numbers[str(out_numbers[text_input])].start()  # Вызов комнаты из словаря по значению комнаты.
        else:
            print('Name error')
    else:
        print('Bye!')


dct_rooms_numbers = {}  # Словарь номеров комнат и объектов.


def room_none():
    pass


class Flags:
    def __init__(self, kind):
        global dct_rooms_numbers
        self.raised = False
        self.kind = kind
        dct_rooms_numbers.update({kind: self})
        if self.kind in dct_rooms_numbers.keys():
            dct_rooms_numbers[kind] = (dct_rooms_numbers[kind], self)
        else:
            dct_rooms_numbers.update({kind: (self,)})

    def start(self):
        self.raised = True


class MyObject:
    def __


class Rooms:

    def __init__(self, number, out_numbers, function=lambda: None):
        self.number = str(number)  # Строка номера комнаты.
        self.out_numbers = out_numbers
        # Словарь направлений и ссылок на объекты выхода.
        self.function = function
        dct_rooms_numbers.update({self.number: self})

    def start(self):
        # print_room(Data.text_room[self.number])
        self.function()  # Вызываем функцию текущей комнаты, если она есть.
        input_room(Data.text_room[self.number], self.out_numbers)  # Ввод и переход к следующей комнате.


def room_4():  # Функция 4-й комнаты.
    print('Hello! How are U?')
    input()
    print('Ok!')


room1 = Rooms(1, {'n': 2})
room2 = Rooms(2, {'s': 1, 'n': 3, 'w': 4})
room3 = Rooms(3, {'s': 2, 'cry': Flags('key')})
room4 = Rooms(4, {'e': 2, 'n': 5}, room_4)
room5 = Rooms(5, {'s': 4})
room1.start()
