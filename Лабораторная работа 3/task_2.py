def find_common_participants(first_group, second_group, sep = ','):
    common_participants = []
    first_group_list = first_group.split(sep)
    second_group_list = second_group.split(sep)
    for surname_1 in first_group_list:
        for surname_2 in second_group_list:
            if surname_2 == surname_1:
                common_participants.append(surname_2)
    common_participants.sort()
    return common_participants

# Проверка работы программы при разделителе - '|'
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))

# Проверка работы программы при разделителе - ','
participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

print(find_common_participants(participants_first_group, participants_second_group))
