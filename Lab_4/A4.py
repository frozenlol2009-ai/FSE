def validate_luhn(card_number: str) -> bool:
    # номер карты на корректность по алгоритму Луна.
    total_sum = 0

    for i, digit_char in enumerate(reversed(card_number)):
        digit = int(digit_char)
        
        if i % 2 == 1:
            doubled = digit * 2
            if doubled > 9:
                total_sum += doubled - 9
            else:
                total_sum += doubled
        else:
            total_sum += digit
            
    return total_sum % 10 == 0


def get_card_type(card_number: str) -> str:
    # тип платежной системы
    length = len(card_number)
    
    if length == 15 and (card_number.startswith('34') or card_number.startswith('37')):
        return "American Express"
        
    elif length == 16 and any(card_number.startswith(prefix) for prefix in ['51', '52', '53', '54', '55']):
        return "MasterCard"
        
    elif (length == 13 or length == 16) and card_number.startswith('4'):
        return "Visa"
    # добавил белкард
    elif (length == 16) and (card_number.startswith('91123801') or card_number.startswith('91123800')):
        return "Belcard"
    return "Unknown"


def card_validator(card_number: str):
    # функция валидатор - структура и алгоритм Луна.

    clean_number = card_number.replace(" ", "").replace("-", "")
    
    if not clean_number.isdigit():
        print(f"Ошибка: Номер '{card_number}' содержит некорректные символы!")
        return

    card_type = get_card_type(clean_number)
    
    if card_type == "Unknown":
        print(f"Карта {card_number} — INVALID (Неизвестный тип или неверная длина)")
        return

    if validate_luhn(clean_number):
        print(f"Карта {card_number} — VALID ({card_type})")
    else:
        print(f"Карта {card_number} — INVALID (Ошибка алгоритма Луна)")

cardNumber = (input("Введите номер банковской карты: "))
card_validator(cardNumber)
