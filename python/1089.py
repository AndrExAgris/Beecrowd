while True:
	n = int(input())
	if n == 0:
		break
	r = 0
	li = [int(i) for i in input().split()]
	for i in range(n):
		if li[i-1] < li[i] > li[(i+1)%n] or li[i-1] > li[i] < li[(i+1)%n]:
			r += 1
	print(r)

