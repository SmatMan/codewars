from math import sqrt

def getDivisors(num, min=1):
    divisors=[]
    # for i in range(min, int(sqrt(num))+1):
    #     if num % i == 0:
    #         divisors.append(i)
    #         other = num // i
    #         if other != i: 
    #             divisors.append(other) 

    divisors = [i for i in range(min, int(sqrt(num))+1) if num % i == 0]
    divisors.append(num)
        
    return divisors


def list_squared(m, n):
    answers = []
    
    for i in range(m, n):
        squared = []
        sum = 0
        for div in getDivisors(i):
            sum += div**2


        if sqrt(sum).is_integer():
            answers.append([i, sum])

    return answers

print(getDivisors(289))