
from num2words import num2words
from decimal import Decimal, ROUND_HALF_UP

BASE_FARE = Decimal("3.00")
PER_KM_RATE = Decimal("1.20")

distance = Decimal(input("Masofani kiriting (km): "))
fare = (BASE_FARE + distance * PER_KM_RATE).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

# So‘z shakli
dollars = int(fare)
cents = int((fare - dollars) * 100)
en = f"{num2words(dollars, lang='en')} dollars and {num2words(cents, lang='en')} cents"
ru = f"{num2words(dollars, lang='ru')} долларов {num2words(cents, lang='ru')} центов"

print(f"Taxi narxi: ${fare} ({en}, {ru})")
