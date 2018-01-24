#iterative
n=100
sum=0
while(n>=1):
    sum=sum+n
    n=n-1
print(sum)

#recursive
def sum_n(n):
    if n==0:
        return 0
    else:
        return n + sum_n(n-1)
print(sum_n(100))
