def answer(total_lambs):
    if total_lambs < 10 or total_lambs > 10**9:
        return 0
    return stin_lambs(total_lambs) - gen_lambs(total_lambs)

def gen_lambs(tl):
    ans = [1]
    while(sum(ans) <= tl):
        ans.append(ans[-1]*2)
    else:
        ans.pop(-1)
        if (ans[-1]+ans[-2])<(tl-sum(ans)):
            ans.append(tl-ans[-1])
        elif(sum(ans) + ans[-1]+ans[-2]<=tl):
            ans.append(ans[-1]+ans[-2])               
    print(ans)
    print(sum(ans))
    return len(ans)

def stin_lambs(tl):
    ans = [1,1]
    while(sum(ans) <= tl):
        ans.append(ans[-1]+ans[-2])
    else:
        ans.pop(-1)
    print(ans)
    print(sum(ans))
    return len(ans)

print(answer(10))
