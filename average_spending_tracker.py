from num2words import num2words

amount = int(input("Pul miqdorini kiriting ($): "))

bills = [50, 10, 5, 1]
bill_counts = {}

remaining = amount
for bill in bills:
    bill_counts[bill] = remaining // bill
    remaining %= bill

for bill in bills:
    print(f"${bill} kupyuradan: {bill_counts[bill]} ta")

# So‘z shakllar
en_words = num2words(amount, lang='en')
ru_words = num2words(amount, lang='ru')

print(f"Umumiy summa: ${amount} ({en_words}, {ru_words})")
