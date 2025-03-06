# def misolar(temp):
#     upper_count = sum(1 for t in temp if t.isupper())
#     lower_count = sum(1 for t in temp if t.islower())
#     number_count = sum(1 for t in temp if t.isnumeric())
#
#     return upper_count, lower_count, number_count
#
# temp = (input(" Nimadir kirit !!! "))
# upper_count, lower_count, number_count = misolar(temp)
#
# print(f"Katta harf:{upper_count}")
# print(f"Kichik harf:{lower_count}")
# print(f"Raqam Soni:{number_count}")


# def polindrom(temp):
#     cleaned_text = ''.join(t.lower() for t in temp if t.isalnum())
#     return cleaned_text == cleaned_text[::-1]
#
# temp = (input("Nimadir kirit !!!"))
#
# if polindrom(temp):
#     print("Ha polindorm")
# else:
#     print("Yo'q polinrom emas")


# def reverse(s):
#     return s[::-1]
#
# s = input("Nimadir kirit   ")
# print(reverse(s))


# def swapcase_text(s):
#     return s.swapcase()
#
# s = input("Nimadir kirit  ")
# print(swapcase_text(s))


def r_case(temp):
    return ''.join(temp.split())

temp = input("Nimadir kirit  ")
print(r_case(temp))

