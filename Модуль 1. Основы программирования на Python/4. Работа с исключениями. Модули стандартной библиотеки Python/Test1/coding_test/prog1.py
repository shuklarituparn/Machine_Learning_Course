def double_print(string):
    if len(string) == 0:
        raise ValueError("empty string is not allowed")
    else:
        print(string)
        print(string)


if __name__ == "__main__":
    double_print('HELLO')
