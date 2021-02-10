from Labirint import Data


def print_room(text):
    print(text)


def input_room(text, out_numbers):
    print(f'{text} ({", ".join(sorted(out_numbers.keys()))})')
    text_input = input().lower()

    if text_input in out_numbers.keys():
        dct[str(out_numbers[text_input])].start()
    else:
        print('Name error')


dct = {}


class JustRooms:

    def __init__(self, number, out_numbers, function=lambda: None):
        self.number = str(number)  # Строка номера комнаты
        self.out_numbers = out_numbers
        # Словарь напривлений и ссылок на объекты выхода
        self.function = function
        print(self.function)
        global dct
        dct.update({self.number: self})

    def start(self):
        print_room(Data.text_room[self.number])
        self.function()
        input_room(Data.text_room[self.number], self.out_numbers)


def room_4():
    print('Hello')

room1 = JustRooms(1, {'n': 2})
room2 = JustRooms(2, {'s': 1, 'n': 3, 'w': 4})
room3 = JustRooms(3, {'s': 2})
room4 = JustRooms(4, {'e': 2, 'n': 5}, room_4())
room5 = JustRooms(5, {'s': 4})
room1.start()
