def calculate_bonus(amount):
    if amount > 2500:
        return 25
    elif amount > 2000:
        return 20
    elif amount > 1500:
        return 15
    elif amount > 1250:
        return 10
    elif amount > 1000:
        return 5
    else:
        return 0


def calculate_penalty(amount):
    if amount < 1000:
        return 10
    return 0