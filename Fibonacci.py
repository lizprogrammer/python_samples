#Fibonacci
#1, 1, 2, 3, 5, 8, 13

count = input("Enter how many Fibonacci numbers would you like: ")


print(count)


def get_fibonacci(num):
    num=int(num)
    new_list = [1,1]
    i = 1

    while i < num:
        new_list.append(new_list[i-1] + new_list[i])
        i += 1

    return new_list


a = get_fibonacci(count)
print(a)