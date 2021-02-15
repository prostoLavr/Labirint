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


dct_flags = {}


class Rooms:

    def __init__(self, number, text, out_numbers, flags=None, function=lambda: True):
        if flags:
            for i in flags.values():
                if i not in dct_flags.keys():
                    dct_flags.update({i: False})
        self.text = text
        self.number = str(number)  # Строка номера комнаты.
        self.out_numbers = out_numbers
        self.flags = flags
        # Словарь {направление: ссылка на объект}.
        self.function = function

    def start(self, dct):
        print_room(self.text)
        if self.function():  # Вызываем функцию текущей комнаты, если не была передана, вызываем пустую.
            self.do_room(dct)  # Ввод и переход к следующей комнате.

    def do_room(self, dct):
        # Вывод текста и вариантов ответа.
        text_input = input_room(list(self.out_numbers.keys()) + list(self.flags.keys()))
        if text_input:
            if text_input in self.out_numbers.keys():
                dct[int(self.out_numbers[text_input])].start(dct)
                # Вызов комнаты из словаря по изначению комнаты.
            if text_input in self.flags.keys():
                if not dct_flags[self.flags[text_input]]:
                    dct_flags[self.flags[text_input]] = True
                    print_room(Data.flag_texts[self.flags[text_input]])
                else:
                    print_room('Если тут что-то и было, это забрали')
                self.do_room(dct)
        else:
            print('Bye!')


dct_rooms = {}
for element in Data.dct_main:
    dct_rooms.update({element[0]: Rooms(*element)})
dct_rooms[1].start(dct_rooms)
