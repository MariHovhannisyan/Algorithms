def prefix(t):
    p = [0] * len(t)
    j = 0
    for i in range(1, len(t)):
        while j > 0 and t[i] != t[j]:
            j = p[j - 1]
        if t[i] == t[j]:
            j += 1
            p[i] = j
    return p

t = "abab"
a = "abaccababac"
p = prefix(t)
m = len(t)
n = len(a)
i = 0
j = 0
l=[]

while i < n:
    if a[i] == t[j]:
        i += 1
        j += 1
        if j == m:
            l.append(i-j)
            print("YES")
            break
    else:
        if j > 0:
            j = p[j - 1]
        else:
            i += 1
else:
    print("NO")
print(l)