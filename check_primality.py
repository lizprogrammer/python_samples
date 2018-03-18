def get_integer(help_text):
    return int(input(help_text))

num = get_integer("Enter a number: ")
a = list(range(2, num ))

prime = True

for i, a in enumerate(a):
    if num % a == 0:
        prime = False
        break

print(prime)







