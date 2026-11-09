import random
import time

n = int(input("Введите количество примеров: "))

correct_answers = 0
total_time = 0.0

for i in range(1, n + 1):
    print(f"Вопрос {i}/{n}")
    
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    
    correct_result = a * b

    start_time = time.time()
    
    while True:
        try:
            user_input = input(f"{a} × {b} = ")
            answer = int(user_input)
            break
        except ValueError:
            print("Пожалуйста, введите целое число!")

    time_spend = time.time() - start_time
    total_time += time_spend

    if answer == correct_result:
        print(f"Верно! (Время: {time_spend:.2f} сек)")
        correct_answers += 1
    else:
        print(f"Неверно! Правильно: {correct_result} (Время: {time_spend:.2f} сек)")

avg_time = total_time / n if n > 0 else 0
percentage = (correct_answers / n) * 100 if n > 0 else 0

print("==================================================")
print("СТАТИСТИКА:")
print("==================================================")
print(f"Общее время: {total_time:.2f} секунд")
print(f"Среднее время на вопрос: {avg_time:.2f} сек")
print(f"Правильных ответов: {correct_answers}/{n}")
print(f"Процент правильных: {percentage:.1f}%")
