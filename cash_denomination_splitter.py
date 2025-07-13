from num2words import num2words
from decimal import Decimal, ROUND_HALF_UP

# Foydalanuvchidan qiymatlar
prices = input("Mahsulot narxlarini kiriting (vergul bilan): ")
price_list = [Decimal(p.strip()) for p in prices.split(",")]

total = sum(price_list)
rounded_total = total.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)

# So‘z shakllari
def to_words(amount):
    dollars = int(amount)
    cents = int((amount - dollars) * 100)
    en = f"{num2words(dollars, lang='en')} dollars and {num2words(cents, lang='en')} cents"
    ru = f"{num2words(dollars, lang='ru')} долларов {num2words(cents, lang='ru')} центов"
    return en, ru

en_total, ru_total = to_words(total)
en_rounded, ru_rounded = to_words(rounded_total)

print(f"Umumiy narx: ${total:.2f} ({en_total}, {ru_total})")
print(f"Yaxlitlangan narx: ${rounded_total:.2f} ({en_rounded}, {ru_rounded})")

