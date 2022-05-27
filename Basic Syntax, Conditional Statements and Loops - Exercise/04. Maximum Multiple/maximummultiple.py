divisor = int(input())
boundary = int(input())

n =  max(num for num in range(boundary+1) if num % divisor == 0)


print(n)


