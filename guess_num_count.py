import random
num = random.randint(1, 100)
count=1
while True:
	guess = int(input("猜第"+str(count)+"次, 請猜一整數:"))
	if guess == num:
		print("終於猜對了!")
		break
	elif guess > num:
		print("比答案大")
	elif guess < num:
		print("比答案小")
	count+=1