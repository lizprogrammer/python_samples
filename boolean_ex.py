def is_number_in(u_num, u_list):
    return u_num in u_list


if __name__ == "__main__":
    user_list = input("Give me a list: ")
    user_num = input("Give me a number: ")
    is_in = is_number_in(user_num, user_list)
    print(is_in)