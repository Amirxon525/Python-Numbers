from num2words import num2words

food01 = float(input("Food Price: "))
food02 = float(input("Food Price: "))
food03 = float(input("Food Price: "))

price = round(food01 + food02 + food03, 1)

words_en = num2words(
    price, 
    to='currency', 
    currency='USD'
)
words_ru = num2words(
    price, 
    lang='ru', 
    to='currency', 
    currency='USD'
)

print(price, words_en, words_ru)
