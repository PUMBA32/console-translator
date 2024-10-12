import os
import sys

if "googletrans" not in sys.builtin_module_names:
    os.system("pip install googletrans==3.1.0a0")

from googletrans import Translator


class Program:
    def __init__(self) -> None:
        self.ru: str = 'абвгдеёжзиклмнопрстуфхцчшщьыъэюя'
        self.t = Translator()
    

    def cls(self) -> None:
        os.system("cls" if sys.platform == "win32" else "clear")
    

    def translate(self, inp: str) -> str:
        is_ru = False
        for letter in self.ru:
            if letter in inp:
                is_ru = True
        to_lang: str = "en" if is_ru else "ru"
        return self.t.translate(inp, dest=to_lang)


def main() -> None:
    program = Program()
    program.cls()
    while True:
        
        inp: str = input(">>> ").strip()

        if inp != '':
            try:
                result = program.translate(inp)
            except:
                print("[!] error - something went wrong, try later...\n")
            else:
                print(f"{result}\n")


if __name__ == '__main__':
    main()

