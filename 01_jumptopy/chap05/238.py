def positive(numberList):
    result = []

    for num in numberList:
        if num > 0:
            result.append(num)

    return result

print(positive([1,-2,2,0,-5,6]))