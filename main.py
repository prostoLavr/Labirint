from Labirint import Data


def print_room(text):
    print(text)


def next_room(out_numbers):
    print(f'{Data.next_room_text} ({", ".join(sorted(out_numbers.keys()))})')  # Вывод текста и вариантов ответа.
    text_input = input().lower()
    while text_input and text_input not in out_numbers.keys():
        print('NameError')
        text_input = input().lower()
    if text_input:
        dct_rooms_numbers[str(out_numbers[text_input])].start()  # Вызов комнаты из словаря по изначению комнаты.
    else:
        print('Bye!')


dct_rooms_numbers = {}  # Словарь номеров комнат и объектов.


class Rooms:

    def __init__(self, number, out_numbers, function=lambda: True):
        self.number = str(number)  # Строка номера комнаты.
        self.out_numbers = out_numbers
        # Словарь напривлений и ссылок на объекты выхода.
        self.function = function
        global dct_rooms_numbers
        dct_rooms_numbers.update({self.number: self})

    def start(self):
        print_room(Data.text_room[self.number])
        if self.function():  # Вызываем функцию текущей комнаты, если не была передана, вызываем пустую.
            next_room(self.out_numbers)  # Ввод и переход к следующей комнате.


def room_4():  # Функция 4-й комнаты.
    print('Hello! How are U?')
    input()
    print('Ok!')
    return True  # Продолжить стандартным вводом


def room_5():
    print("It's the end.")


room1 = Rooms(1, {'n': 2})
room2 = Rooms(2, {'s': 1, 'n': 3, 'w': 4})
room3 = Rooms(3, {'s': 2})
room4 = Rooms(4, {'e': 2, 'n': 5}, room_4)
room5 = Rooms(5, {'s': 4}, room_5)
room1.start()
