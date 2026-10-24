import os

times = []
wc_temps = []
wc_effects = []

with open(r'C:\Study\FSE\Lab_2\1.WCData.txt', 'r', encoding='utf-8') as file: 
    lines = file.readlines()

for line in lines[2:]:
    line = line.strip()
    if not line:
        continue
        
    parts = line.split()
    if len(parts) == 3:
        times_val = parts[0]
        air_temp = int(parts[1])
        wind_speed = int(parts[2])

        answer = 35.74 + (0.6125 * air_temp) + ((0.4275 * air_temp) - 35.75) * (wind_speed ** 0.16)

        answer_end = round(answer, 1)
        raznica = round(answer_end - air_temp, 1)
        
        times.append(
            times_val,
        )

        wc_temps.append(
            answer_end
        )

        wc_effects.append(
            raznica
        )

count = len(wc_temps)
summa = sum(wc_temps)
avg = summa / count
end_answer = round(avg, 1)

number = 0
with open('output.txt', 'w', encoding = 'utf-8') as file:
    file.write(f"Time             Air Temap       Wind Speed\n")
    file.write(f'-'*100 + '\n')
    for row in times: 
        line = f"{times[number]}          {wc_temps[number]}          {wc_effects[number]}\n"
        number += 1
        file.write(line)
    file.write(f'-'*100 + '\n')
    file.write(f'The everage adjusted temperature, based on {count} observations, was {end_answer}\n')


os.system("start output.txt")