import random
from time import sleep
print("""
               ROCK / PAPER / SCISSOR
""")
a=["rock","paper","scissor"]

def you_lose(comp):
	sleep(0.3)
	print(f":> COMPUTER : {comp}")
	sleep(0.4)
	print(":> You Lose !")
def you_won(comp):
	sleep(0.3)
	print(f":> COMPUTER : {comp}")
	sleep(0.4)
	print(":> You Won !")

try:
	print("-"*53)
	count=int(input(":> How many times you want to play : "))
	print("-"*53)
except:
	print("--UnExcepted value")
	exit()
counter=0
comp_points=0
user_points=0

while counter!=count:
	sleep(0.5)
	comp=random.choice(a)
	user=input("\n:> YOU : ").lower()
	
	if user==comp:
		print(f":> COMPUTER : {comp}")
		print(":> Draw ! ")
	
	elif user=="rock" and comp=="paper":
		you_lose(comp)
		comp_points+=1

	elif user=="rock" and comp=="scissor":
		you_won(comp)
		user_points+=1
	
	elif user=="paper" and comp=="scissor":
		you_lose(comp)
		comp_points+=1
	elif user=="paper" and comp=="rock":
		you_won(comp)
		user_points+=1
	
	
	elif user=="scissor" and comp=="paper":
		you_won(comp)
		user_points+=1
	
	elif user=="scissor" and comp=="rock":
		you_lose(comp)
		comp_points+=1
	else:
		counter-=1
	counter+=1
sleep(1)
print('\n\nYour Points = ',user_points)
print('Computer Points = ',comp_points)
sleep(0.8)
if user_points>comp_points:
	print("\n\n》 ¥ou ₩on the Match...☆☆☆☆☆")
elif comp_points>user_points:
	print("\n\n《 You Losed the Match...\n  LOSER !")
else:
	print("\n\n¿ Match Draw ¿  @ Nice Played...♡")


