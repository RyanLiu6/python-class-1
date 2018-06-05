def main():
    pattern(2)


def pattern(num):
    if num == 0:
        printf(0)
    else:
        printf(0)
        printf(num)
        pattern(num - 1)

def printf(num):
    print(num, end=" ")


if __name__ == "__main__":
    main()
