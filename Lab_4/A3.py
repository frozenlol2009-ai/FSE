vvod = input()
digits = str(vvod)

all = 0
dlina = 0
poteryashka = 0
high = 0

for num in digits:
    if num == "0":
        poteryashka += 1
        all += 1
        dlina += 1
        if high <= dlina:
            high = dlina
        elif high > dlina:
            high = high
    else:
        all += 1
        dlina = 0
    

procent = poteryashka / all        
procent = procent * 100 

if procent >= 0 and procent <= 1:
    verdikt = "Отличное качество"
elif procent > 1 and procent <= 5:
    verdikt = "Хорошее качество"
elif procent > 5 and procent <= 10:
    verdikt = "Удовлетворительное качество"
elif procent > 10 and procent <= 20:
    verdikt = "Плохое качество"
elif procent > 20:
    verdikt = "Критическое состояние сети"

print(f"\nОбщее количество пакетов: {all}")
print(f"Количество потерянных пакетов:  {poteryashka}")       
print(f"Длина самой длинной последовательности потерянных пакетов: {high} ")
print(f"Процент потерь: {procent:.1f}%")
print(f"Процент потерь: {verdikt}")