import sys

# stdin
l = []
for e in sys.stdin:
  if e == '\n':
    break
  else:
    l.append(e.strip('\n'))

n, p = int(l[0]), l[1]

if p[n - 1] == 'o':
  print('Yes')
else:
  print('No')
