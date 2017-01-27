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
ops = [[mult,add],[div,sub]]


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

def is24(num,epsilon=0.000001):
    if(abs(num-24.0) < epsilon):
        return True
    return False
    
def solve24(nums):
    q = []
    q.append((nums,""))
    while(len(q) > 0):
        cur = q.pop(0)
        if(len(cur[0])==1 and is24(cur[0][0])):
            return cur[1]
        newstuff = getAllPoss(cur)
        for e in newstuff:
            q.append(e)
    return None
