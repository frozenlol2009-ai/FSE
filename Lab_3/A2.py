import string
anythingsym = '*-#'
password = input("Введите пароль: ")


dlina = len(password) == 8
digital = any(symbol.isdigit() for symbol in password)
lowersym = any(symbol.islower() for symbol in password)
uppersym = any(symbol.isupper() for symbol in password)
specsym = any(symbol in anythingsym for symbol in password)

errors = []

if not dlina:
    errors.append("Длина пароля должна быть от 8 символов.")
if not digital:
    errors.append("В пароле отсутствуют цифры.")
if not lowersym:
    errors.append("В пароле отсутствуют строчные буквы.")
if not uppersym:
    errors.append("В пароле отсутствуют заглавные буквы.")
if not specsym:
    errors.append("В пароле отсутствуют специальные символы.")


if not errors:
    print("Надежный пароль.")
else:
    print("Пароль не подходит по следующим причинам:")
    for error in errors:
        print(f"- {error}")