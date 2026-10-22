def count_days(day: int) -> None:
    if day == 0:
        return
    count_days(day - 1)
    print(f"Day {day}")


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    count_days(days)
    print("Harvest time!")
