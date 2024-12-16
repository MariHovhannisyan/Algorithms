def compute_last_occurence(pattern):
  last = {}
  for i in range(len(pattern)):
    last[pattern[i]] = i
  return last
def boyer_moore(t,p):
  n = len(t)
  m = len(p)
  l = compute_last_occurence(p)
  i = 0
  while i <= n-m:
    j = m-1
    while j >= 0 and p[j] == t[i+j]:
      j-=1
    if j<0:
      print(f'pattern found from {i}')
      i+=1
    else:
      i += max(1, j - l.get(t[i + j], -1))
text = "abacaabadcabacabaabb"
pattern = "abacab"
boyer_moore(text, pattern)