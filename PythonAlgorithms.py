def sum1(n):
    '''
    Take an input of n and return the sum of the numbers from 0 to n
    '''
    final_sum = 0
    for x in range(n+1):
        final_sum += x

    return final_sum


print(sum1(10))
