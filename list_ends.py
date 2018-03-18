import random

a = [random.randrange(0, 3)]
count = random.randrange(0,100)
i = 1

while i < count:
    a.append( random.randrange(0, 100))
    i += 1

print(a)


def get_new_list():
    new_list = a[0], a[-1]
    return new_list


my_list = get_new_list()
print(my_list)

#def defaultArg( name, msg = "Hello!"):

    