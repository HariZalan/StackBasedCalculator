import sys
sys.setrecursionlimit(100000)
def execute(string,stack=[],registers=dict()):
	string=string.replace("  "," ").strip().split(" ")
	try:
		for i in range(len(string)):
			try:
				string[i]=int(string[i])
				stack.append(string[i])
			except:
				try:
					string[i]=float(string[i])
					stack.append(string[i])
				except:
					if (string[i]=="+"):
						x=stack.pop()
						y=stack.pop()
						stack.append(x+y)
					elif (string[i]=="-"):
						x=stack.pop()
						y=stack.pop()
						stack.append(y-x)
					elif (string[i]=="*"):
						x=stack.pop()
						y=stack.pop()
						stack.append(x*y)
					elif (string[i]=="/"):
						x=stack.pop()
						y=stack.pop()
						stack.append(y/x)
					elif (string[i]=="d"):
						x=stack.pop()
						stack.append(x)
						stack.append(x)
					elif (string[i]=="p"):
						x=stack.pop()
						stack.append(x)
						print(str(x))
					elif (string[i]=="u" or string[i]=="U"):
						x=input()
						if (string[i]=="U"):
							X=x.split(" ")
						else:
							X=[x]
						for j in X:	
							try:
								stack.append(int(j))
							except:
								stack.append(j)
					
					elif (string[i]=="P"):
						stack.pop()
					elif (string[i]=="e"):
						x=stack.pop()
						x=str(x).replace("_"," ")
						execute(x,stack,registers)
					elif (string[i]=="q"):
						exit(0)
					elif (string[i][0]=="r" and len(string[i])==2):
						x=stack.pop()
						registers[string[i][1]]=x
					elif (string[i][0]=="R" and len(string[i])==2):
						x=registers[string[i][1]]
						stack.append(x)
					elif (string[i][0]=="=" and len(string[i])==2):
						x=stack.pop()
						y=stack.pop()
						z=stack.pop()
						if (x==y):
							registers[string[i][1]]=z
						else:
							stack.append(z)
					elif (string[i][0]=="<" and len(string[i])==2):
						x=stack.pop()
						y=stack.pop()
						z=stack.pop()
						if (y<x):
							registers[string[i][1]]=z
						else:
							stack.append(z)
					else:
						stack.append(string[i])
	except KeyboardInterrupt:
		print("Interrupted")
	except IndexError:
		print("Stack empty")
	except TypeError:
		print("Bad typing")
	except RecursionError:
		print("Too many recursion levels")
	except ZeroDivisionError:
		print("Division by zero")
		
