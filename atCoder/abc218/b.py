import sys
import string

asc = string.ascii_lowercase

l = sys.stdin.readline()
l = l.strip('\n').split(' ')

ans = ''
for e in l:
  e = int(e) - 1
  ans += str(asc[e])

print(ans)
