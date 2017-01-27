## solution for 24 game


## operations
	
def mult(a,b):
    return (a*b,str(a) + "*" + str(b))

def add(a,b):
    return (a+b,str(a) + "+" + str(b))

def div(a,b):
    return (a/b,str(a) + "/" + str(b))

def sub(a,b):
    return (a-b,str(a) + "-" + str(b))

# more operations can be added if necessary

def getPoss(num1,num2):
    poss = []
    t = None
    for op in ops[0]:
        poss.append(op(num1,num2))
    for op in ops[1]:
        poss.append(op(num1,num2))
        poss.append(op(num2,num1))
    return poss
