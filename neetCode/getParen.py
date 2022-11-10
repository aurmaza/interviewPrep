def genParan(n):#created by chris
	
	stack = []
	res = []

	def backtrack(op,cp):
		if op == cp == n:
			res.append("".join(stack))
			return

		if op < n:
			stack.append("(")
			backtrack(op+1,cp)
			stack.pop()

		if cp < op:
			stack.append(")")
			backtrack(op,cp+1)
			stack.pop()
	backtrack(0,0)

	return res




def test():
	n = 3
	print(genParan(n))


  
	
	
	
	