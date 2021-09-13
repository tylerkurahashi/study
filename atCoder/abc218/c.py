import sys

arr = []
for line in sys.stdin:
  if line == '\n':
    break
  arr.append(line.strip('\n'))

N = arr[0]
S = []
T = []

for r in arr[1:6]:
  S.append([e for e in r])

for r in arr[6:]:
  T.append([e for e in r])

print(S, T)
