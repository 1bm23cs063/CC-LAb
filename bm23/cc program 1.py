import sys

num = int(sys.argv[1])

def checkArmstrong(num):
	num_str= str(num)
	n=len(num_str)

	sum_of_power = sum(int(digit) ** n for digit in num_str)

	if sum_of_power ==num:
		return "yes"
	else:
		return "no"

print(checkArmstrong(num))
