# https://projecteuler.net/problem=1
list=[]
for v in range(1,1000):
    if v%3==0 or v%5==0:
        list.append(v)
print(list)
print(sum(list))