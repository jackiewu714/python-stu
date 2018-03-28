
x = []

while True:
	inputStr = input("enter a number or Enter to finish: ")
	try:
		if inputStr:
			intVal = int(inputStr)
			x.append(intVal)
			continue
		else:
			break

	except ValueError as err:
		print(err)
		continue
	except EOFError as err:
		print(err)
		break

list.sort(x)
print("x", x)

count = len(x)
sum = sum(x)
print("count=",count, ", sum=", sum)
