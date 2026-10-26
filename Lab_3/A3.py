schetchik1 = int(input("Введите показание счетчика в прошлом месяце: "))
schetchik2 = int(input("Введите показание счетчика в этом месяце: "))

if (schetchik2 < schetchik1):
    ispolzovano = schetchik2 + 10000 - schetchik1
else:
    ispolzovano = schetchik2 - schetchik1
    
if ispolzovano <= 300:
    price = 21      # работает
elif (ispolzovano > 300 and ispolzovano <= 600):
    price = 21 + ((ispolzovano-300)*0.06)  # работает
elif (ispolzovano > 600 and ispolzovano <= 800):
    price = 21 + (300*0.06) + ((ispolzovano-600)*0.04)     # работает
elif (ispolzovano > 800):
    price = 21 + (300*0.06) + (200*0.04) + ((ispolzovano-800) * 0.025)      # работает

price =  round (price, 2)
midprice = round(price/ispolzovano, 2) 

print ("Предыдущее           Текущее          Использовано         К оплате            Ср. цена m^3")
print (f"    {schetchik1}                  {schetchik2}                {ispolzovano}                 {price}                 {midprice}")