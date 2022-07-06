from cmath import e
from random import randint
from sqlite3 import connect

db = connect("data.db")
cur = db.cursor()

def perekus(text: str, mode: str):
    newText = ""
    a = ord("а")
    alphabet = [chr(i) for i in range(a, a+32)]

    for letter in text:
        letter = letter.lower()
        if letter == " ":
            newText += "\n"

        elif letter in alphabet:
            lines = cur.execute(f"SELECT words FROM perekus WHERE id = '{letter}'").fetchone()[0].split(";")
            index = randint(0, len(lines)-1)
            line = lines[index].capitalize()
            if mode == "yes":
                newText += f"{letter.capitalize()} - {line}\n"
            else: newText += f"{line}\n"    

    return newText


def main():
    name = input("Перекус на имя: ")
    mode = input("Включить показ букв? (yes) ")
    print(f"\n\nПерекус на имя {name}:\n" + perekus(name, mode))


if __name__ == "__main__":
    main()