s = [[0] * 30 for i in range(30)]
for i in range(1, 30):
  s[1][i] = i
for i in range(2, 30):
  for j in range(i, 30):
    for k in range(i - 1, j):
      s[i][j] += s[i - 1][k]
t = int(input())
for i in range(t):
  a, b = map(int, input().split())
  print(s[a][b])