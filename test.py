# 
x = "hello viet nam"
print(x[::-1])


# Dùng for
rev_string = ""
for i in range(len(x) - 1, 0, -1):
  rev_string += x[i]


# Dùng hàm đệ quy
rev_s = ""
def de_quy(n, s, res):
  res += s[n]
  if(n == 0):
    return res
  return de_quy(n - 1, s, res)
