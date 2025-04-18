# print(type("test"))

# print(type(3.14))

# # None은 파이썬에서 Null타입
# none_var = None

# print(type(none_var))


def print_type(param) :
    print(type(param))
    print(int(param))
    print(float(param))
    print(str(param))

def sol_question(param) :
    print(type(param))
    print(float(param))
    print(bool(param))
    print(int(param))
    print(str(param))
    return str(param)


if __name__ == "__main__" :
    sol_question(123)