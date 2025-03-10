for num in range(11):
    print(num)
    mask = 1 << num
    print("Mask: ", mask, type(mask))
    print("Mask - 1: ", mask - 1, type(mask - 1))
    print("Mask - 1 - 1: ", mask - 1 - 1)
    print("Mask - 2: ", mask - 2)
    print("Mask - 10: ", mask - 10)
    print("Mask ^ 1: ", mask ^ 1)
    print("Mask ^ 2: ", mask ^ 2)
    print("Mask ^ 10: ", mask ^ 10, type(mask ^ 10))