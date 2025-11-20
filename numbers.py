
print("Power -1 of 2 :" , 2 ** -1)
print("==" * 20)
# Power 10 of 2 
print("Power 10 of 2 :" , 10 ** 2)
print("==" * 20)
# modulus
print("Modulus of 10 % 3 :" , 10 % 3)
print("==" * 20)
# division
print("Division of 10 / 3 :" , 10 / 3)

print("==" * 20)
# quotient
print("Quotient of 10 // 3 :" , 10 // 3)
print("==" * 20)
# divmod
print("Divmod of 10 % 3 and 10 // 3 :" , divmod(10,3))
print("==" * 20)
# modulus
print("Modulus of 10 % 3 :" , 10 % 3)

def is_even(n):
    return n % 2 == 0

def is_even_v2(n):
    divmod_result = divmod(n, 2)
    return divmod_result[1] == 0

# Write a function to display the number in words, eg: 353 -> three thousand five hundred fifty three
def number_to_words(n):
    if n == 0:
        return "zero"

    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand"]

    words = ""
    if n >= 1000:
        # 3  for thousands
        words += ones[n // 1000] + " " + thousands[1] + " "
        n = n % 1000
    if n >= 100:
        words += ones[n // 100] + " hundred "
        n %= 100
    if n >= 20:
        words += tens[n // 10] + " "
        n %= 10
    elif n >= 10:
        words += teens[n - 10] + " "
        n = 0
    if n > 0:
        words += ones[n] + " "

    return words.strip()

print(number_to_words(4353))

# Write a function to check display the digits of a number
def display_digits(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    digits.reverse()
    return digits

print(display_digits(4353))