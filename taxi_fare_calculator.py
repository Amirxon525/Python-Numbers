
from decimal import Decimal, ROUND_HALF_UP
from num2words import num2words

# Narx: 1 kWh = $0.45
PRICE_PER_KWH = Decimal("0.45")

# Foydalanuvchidan kiritish
start = Decimal(input("Oy boshidagi ko‘rsatkich (kWh): "))
end = Decimal(input("Oy oxiridagi ko‘rsatkich (kWh): "))

# Sarflangan energiya miqdori
used = end - start
if used < 0:
    print("Xatolik: Oy oxiridagi ko‘rsatkich boshlang'ichdan kichik bo'lishi mumkin emas.")
else:
    # To‘lovni hisoblash
    payment = (used * PRICE_PER_KWH).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    # To‘lovni so‘z bilan ifodalash (ingliz va rus)
    dollars = int(payment)
    cents = int((payment - dollars) * 100)

    english_words = f"{num2words(dollars, lang='en')} dollars and {num2words(cents, lang='en')} cents"
    russian_words = f"{num2words(dollars, lang='ru')} долларов {num2words(cents, lang='ru')} центов"

    # Natija
    print(f"To‘lov: ${payment} ({english_words}, {russian_words})")
