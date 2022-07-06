from random import randint
import json
def perekus(text: str, mode: str):
    newText = ""
    with open("data.json", "r", encoding="utf-8") as f:
        words = json.load(f)

    for letter in text:
        letter = letter.lower()
        if letter == " ":
            newText += "\n"

        elif letter in words:
            index = randint(0, len(words[letter])-1)
            word = words[letter][index].capitalize()
            if mode.lower() == "yes":
                newText += f"{letter.capitalize()} - {word}\n"
            else: newText += f"{word}\n"

    return newText


def main():
    name = input("Перекус на имя: ")
    mode = input("Показывать буквы? (yes) ")
    print(f"\n\nПерекус на имя {name}:\n" + perekus(name, mode))


if __name__ == "__main__":
    main()