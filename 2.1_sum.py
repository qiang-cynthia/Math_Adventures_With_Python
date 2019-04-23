def summation(start, end):
    result = 0
    for i in range(start, end + 1):
        result += i

    return result

start = int(input('start = '))
end = int(input('end = '))

print('result = {}'.format(summation(start, end)))
