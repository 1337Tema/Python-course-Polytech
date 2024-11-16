import json

filename = "input.json"

def task() -> float:
    # Чтение данных из файла в формате JSON
    with open(filename) as file:
        data = json.load(file)
    sum_elem = 0
    for line in data:
        sum_elem += line['score'] * line['weight']
    return round(sum_elem, 3)


print(task())
