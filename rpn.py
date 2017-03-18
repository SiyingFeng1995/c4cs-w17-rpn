#!/usr/bin/env python3

import operator
import readline
from termcolor import colored

OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
}


def calculate(arg):
	print("Calculate " + colorize(arg))
	stack = list()
	for operand in arg.split():
		try:
			operand = float(operand)
			stack.append(operand)
		except:
			arg2 = stack.pop()
			arg1 = stack.pop()
			operator_fn = OPERATORS[operand]
			result = operator_fn(arg1, arg2)
			
			stack.append(result)
	return stack.pop()

def colorize(input_t):
	output = ""
	for char in input_t.split():
		if char in OPERATORS:
			output += colored(char, 'green') + " "
		elif float(char) < 0:
			output += colored(char, 'red') + " "
		else:
			output += char + " "
	return output



def main():
	while True:
		result = calculate(input('rpn calc> '))
		print("Result:", result)

if __name__ == '__main__':
	main()
