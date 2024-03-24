import collections

def adder(n, m, carry="0"):
    carry=int(carry)
    n = int(n)
    m = int(m)


    # print(type(n),type(m),type(carry))
    sum = n+m+carry

    if sum > 9:
        return (str(sum)[-1], str(sum)[-2])
    else:
        return (str(sum))
        

def _sum(x, y, xlen, sum, extra=True):
    carry = "0"
    index = 0
    for ind, i in enumerate(reversed(y)):
        eqnum = x[xlen - ind]
        index = ind


        if carry == "0": # if there is no carry before adding
            res = adder(i, eqnum)
        else:
            res = adder(i, eqnum, carry)
        
        sum.appendleft(res[0])
        if len(res) == 2:
            carry = res[1]
        elif len(res) == 1:
            carry = "0"
        # print(f"{i} + {eqnum} = {res[0]} along with {carry} carry")
    if extra == True:
        x = x[:-index-1]
        # print(x)
        for i in reversed(x):
            res = adder(i, carry)
            if len(res) == 2:
                carry = res[1]
            elif len(res) == 1:
                carry = "0"
            sum.appendleft(res[0])
        if carry != "0":
            sum.appendleft(carry)
    else:
        if carry != "0":
            sum.appendleft(carry)
    
    return sum
    

def sum_strings(x, y):
    xlen = len(x)-1
    ylen = len(y)-1
    # print(f"x: {x} of length {xlen}")
    # print(f"y: {y} of length {ylen}")
    # print(f"Should be {int(x)+int(y)}")
    sum = collections.deque([])

    if x == "" and y == "":
        return "0"
    elif x == "":
        return y
    elif y == "":
        return x


    if xlen > ylen:
        sum = _sum(x, y, xlen, sum)

    elif ylen > xlen:
        sum = _sum(y, x, ylen, sum)

    elif xlen == ylen:
        sum = _sum(y, x, xlen, sum, False)
    else:
        sum = None

    if len(sum) > 1 and sum[0] == "0":
        sum.popleft()
    
    return "".join(sum)