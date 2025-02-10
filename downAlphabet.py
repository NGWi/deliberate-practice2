import os


def getSmallestString(s):
    splitStr = list(s)
    print(splitStr)
    count = 0
    starting = 0
    for index, c in enumerate(splitStr):
        if c == 'a':
            if count > 0:
                break
        else:
            if count == 0:
                starting = index
            count += 1

    for i in range(starting, starting + count):
        c = splitStr[i]
        code = ord(c) - 1
        splitStr[i] = chr(code)

    return ''.join(splitStr)


# Driver code:    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = getSmallestString(s)

    fptr.write(result + '\n')

    fptr.close()
