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


#numset is of format ([,,,,],"...")
def getAllPoss(numset):
    newposs = []
    curstr = numset[1] + ","
    curset = numset[0]
    for i in range(len(curset)):
        for j in range(i+1,len(curset)):
            nthing = getPoss(curset[i],curset[j])
            nset = []
            for k in range(len(curset)):
                if k!=i and k!=j:
                    nset.append(curset[k])
                for n in nthing:
                    tmp = [x for x in nset]
                    tmp.append(n[0])
                    newposs.append((tmp,curstr + n[1]))
    return newposs

