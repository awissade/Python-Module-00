def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    print(
        f"{seed_type.capitalize()} seeds:",
        f"{quantity}",
        end=" "
    )
    if unit in ["packets", "grams", "area"]:
        print(unit)
    else:
        print("Unknown unit type")
