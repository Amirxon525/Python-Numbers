from num2words import num2words
from decimal import Decimal, ROUND_HALF_UP

data = input("Haftalik harajatlarni kiriting (vergul bilan): ")
amounts = [Decimal(x.strip()) for x in data.split(",")]

average = (sum(amounts) / 7).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

# So‘z shakli
dollars = int(average)
cents = int((average - dollars) * 100)
en = f"{num2words(dollars, lang='en')} dollars and {num2words(cents, lang='en')} cents"
ru = f"{num2words(dollars, lang='ru')} долларов {num2words(cents, lang='ru')} центов"

print(f"O‘rtacha harajat: ${average} ({en}, {ru})")
