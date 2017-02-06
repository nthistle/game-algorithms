import collections

wordlist = open(r"C:\Users\neilt\Documents\Projects\words.txt").read()
wordlist = wordlist.split("\n")
wordlist.pop(0)
print(len(wordlist))
wordlist = [x for x in wordlist if x[0].lower() == x[0]]
print(len(wordlist))
wordlist = [x for x in wordlist if len(x) <= 7]
print(len(wordlist))
valid_starts = {}
for e in wordlist:
    c = ""
    for d in e:
        c = c + d
        valid_starts[c] = None

word_dict = {}
for e in wordlist:
    word_dict[e] = None

    
def getNeighbors(x,y):
    neighbors = []
    if(x < 3):
        neighbors.append((x+1,y))
        if(y < 3):
            neighbors.append((x+1,y+1))
        if(y > 0):
            neighbors.append((x+1,y-1))
    if(x > 0):
        neighbors.append((x-1,y))
        if(y < 3):
            neighbors.append((x-1,y+1))
        if(y > 0):
            neighbors.append((x-1,y-1))
        if(y < 3):
            neighbors.append((x,y+1))
        if(y > 0):
            neighbors.append((x,y-1))
    return neighbors


def bfs_word(lmap, spot, results):
    q = collections.deque()
    q.append(([spot],lmap[spot[0]][spot[1]]))
    while(len(q)>0):
        cur = q.popleft()
        if cur[1] in word_dict:
            results[cur[1]] = None
            #print(cur[1])
        x = cur[0][-1][0]
        y = cur[0][-1][1]
        neighbors = getNeighbors(x, y)
        for neighbor in neighbors:
            if neighbor in cur[0]:
                continue # can't go back on itself
            newstart = cur[1] + lmap[neighbor[0]][neighbor[1]]
            if newstart not in valid_starts:
                continue
            newlist = [x for x in cur[0]]
            newlist.append(neighbor)
            q.append((newlist,newstart))

def findall(lmap):
    for i in range(4):
        for j in range(4):
            print("")
            print("STARTING FROM (",i,",",j,")")
            posswords = {}
            bfs_word(lmap, (i,j), posswords)
            pwords = [x for x in posswords]
            pwords.sort()
            for x in pwords:
                print(x)
