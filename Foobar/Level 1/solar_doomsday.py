#python 2
def answer(area):
    ans = []
    while(area!=0):
        res = (int(area**.5))**2
        ans.append(res)
        area = area - res
    return ans

print answer(15324)
