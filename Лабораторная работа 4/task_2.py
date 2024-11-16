import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Считываем данные CSV файла
    with open(INPUT_FILENAME, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    # Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
