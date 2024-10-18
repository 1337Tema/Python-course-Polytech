money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
num = 0  # Счетчик числа месяцев

while money_capital > spend:
    money_capital += salary  # Получаем зарплату
    money_capital -= spend  # Тратим зарплату
    num += 1  # Отсчитываем очередной месяц
    if num == 1:  # Пропускаем первый месяц
        continue
    spend *= (1 + increase)  # Индексируем траты

print("Количество месяцев, которое можно протянуть без долгов:", num)
