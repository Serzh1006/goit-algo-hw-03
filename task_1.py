import argparse
import shutil
from pathlib import Path
import os
import sys

def display_tree(path, destination_dir="dist", ) -> None:
    if '.' in path.name:
        _, file_extension = os.path.splitext(path.name)

        # Якщо папки не існує тоді створюємо її
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        # Якщо папки з розширенням не існує, створюємо її або копіюємо файли в неї
        if not os.path.exists(os.path.join(destination_dir,file_extension[1:])):
            extension_folder = os.path.join(destination_dir,file_extension[1:])
            os.makedirs(extension_folder)
            destination_item = os.path.join(destination_dir, file_extension[1:], path.name)
            shutil.copy2(path,destination_item)
        else:
            destination_item = os.path.join(destination_dir, file_extension[1:], path.name)
            shutil.copy2(path,destination_item)

    if path.is_dir():
        for child in path.iterdir():
            display_tree(child, destination_dir)

def main():
    print(sys.argv)
    if len(sys.argv)<2:
        print("Введіть хоча б один аргумент. Не знайдено шлях до директорії")
        sys.exit(1)
    # Створення парсера аргументів командного рядка
    parser = argparse.ArgumentParser(description='Копіювання файлів з однієї директорії в іншу.')
    
    # Додавання аргументів
    parser.add_argument('source_dir', help='Шлях до вихідної директорії')
    parser.add_argument('destination_dir', nargs='?', default='dist', help='Шлях до директорії призначення (за замовчуванням dist)')
    
    # Розбір аргументів
    args = parser.parse_args()
    
    source_dir = Path(args.source_dir)
    destination_dir = Path(args.destination_dir)
    
    if not os.path.exists(source_dir):
        print("Не вірно вказано шлях!")
        return

    # Виклик функції
    result = display_tree(source_dir,destination_dir)
    if result != False:
        print("Дані скопійовано успішно!")
        

if __name__ == '__main__':
    main()
