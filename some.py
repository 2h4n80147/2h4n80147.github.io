def is_prime(x):
	if x < 2:
		return False
	for y in range(2,x):
		if x%y==0:
			return False
	return True

cnt=0

a = int(input())
b = int(input())

for x in range(a,b+1):
	for y in range(a,b+1):
		if x != y and x < y and is_prime(x+y):
			cnt=cnt+1

			print(x,y,x+y)
print(cnt)

