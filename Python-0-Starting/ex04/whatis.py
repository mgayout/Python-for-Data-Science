import sys

if len(sys.argv) == 0:
	sys.exit()

try:
	if len(sys.argv) > 2:
		raise AssertionError("more than one argument is provided")
	try:
		nb = int(sys.argv[1])
	except:
		raise AssertionError("argument is not an integer")
	if nb % 2 == 1:
		print("I'm Odd.")
	else:
		print("I'm Even.")
except AssertionError as error:
	print(AssertionError.__name__ + ":", error)