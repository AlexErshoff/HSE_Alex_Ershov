def input_participant(participant_num):
    print(f"\nВведите данные участника #{participant_num}:")
    name = input("Наименование: ")
    status = input("Статус (например, Истец/Ответчик/Третье лицо): ")
    inn = input("ИНН: ")
    return {"name": name, "status": status, "inn": inn}


def main():
    participants = []

    # вод данных для 3 участников
    for i in range(1, 4):
        participants.append(input_participant(i))

    # Вывод результата
    print("\nСписок участников спора:")
    print(participants)


if __name__ == "__main__":
    main()