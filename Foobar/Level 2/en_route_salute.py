def answer(s):
    ans = 0
    temp = 0
    for i in s:
        if i == '>':
            temp += 1
        elif i == '<':
            temp *= 2 
            ans += temp
            temp //= 2
    return ans

print(answer('<<>><'))
