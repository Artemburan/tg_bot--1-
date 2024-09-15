import json
import os

from app.data import list_files



def open_file(path: str = list_files.ANIMALS) -> list:

    if not os.path.exists(path):
        with open(path, "w") as fh:
            json.dump([], fh)

    with open(path, "r", encoding="utf-8") as file:
        animals = json.load(file)

    return animals


def save_file(file: list, path: str = list_files.ANIMALS):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(file, fh, indent=4, ensure_ascii=False)


def del_animal(animals):
    animal = open_file()
    animal.remove(animals)
    save_file(animal)

    return f"Тваринку '{animal}' успішно видалено"


def cured_animal(animal, path: str = list_files.CURED_ANIMALS) -> str:
    del_animal(animal)
    cured_animal = open_file(path)
    cured_animal.append(animal)
    save_file(cured_animal, path)

    return f"Тваринку '{animal}' успішно вилікувано."


def add_animal(animals, path: str = list_files.ANIMALS) -> str:
    animal = open_file()

    if animal not in animals:
        animal.append(animals)
        save_file(animals)
        msg = f"Тваринку '{animal}' успішно додано."
    else:
        msg = f"Ця тваринка '{animal}' вже є у списку твариок."

    return msg