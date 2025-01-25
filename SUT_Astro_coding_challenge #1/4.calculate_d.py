import math
def calculate_d(M, m):
    d = math.exp((M - m) / 5) + 1
    return d

M = -16.339065057631082
m = 14.541391237647325
result = calculate_d(M,m)
print(result)