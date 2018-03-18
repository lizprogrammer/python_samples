import random

a = [random.randrange(0, 3)]
count = random.randrange(0,40)
i = 1

while i < count:
    a.append( random.randrange(0, 10))
    i += 1

print(a)


def get_set(a_list):
    my_set = set(a_list)
    return my_set


my_new_set = get_set(a)
print(sorted(my_new_set))

#def defaultArg( name, msg = "Hello!"):
