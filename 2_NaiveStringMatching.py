def naive_string_matching(T,P):
  n=len(T)
  m=len(P)
  l=[]
  for s in range(0,n-m+1):
    if P[:m]==T[s:s+m]:
      l.append(s)
  return l
T="abababbabababbababbbab"
P="bbab"
print(naive_string_matching(T,P))