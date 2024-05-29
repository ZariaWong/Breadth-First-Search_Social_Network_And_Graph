user={} #Global variable with key as node ID (an integer), value as name of the node.
follow={} #Global variable with key as the node ID (an integer), value as a list of neighbor node ID(s) 
userlist=[]

def AddUser(id,name):
    x=int(id)
    userlist.append(x)
    y=str(name)
    if user.get(x,'None')!='None':
        print('ID exists.')
    else:
        localdict={x:y}
        user.update(localdict)
        localdict.clear()
    return id,name

def append_value(follow, x, y):
    if x in follow:
        if not isinstance(follow[x], list):
            follow[x] = [follow[x]]
        follow[x].append(y)
    else:
        follow[x] = [y]


def AddFollow(id1,id2):
    x=id1
    y=id2
    if user.get(x, "None")=="None" or user.get(y, "None")=="None":
        print('No such user.')
    elif follow.get(x,'None')!='None':
        if y in follow.get(x):
            print('Follow exists.')
        else:
            append_value(follow, x, y)
    else:
        append_value(follow, x, y)
    return id1,id2


def ListFollower(id1):
    x=id1
    listOfKeys = get(follow, x)
    for a in range(len(listOfKeys)):
        print(str(listOfKeys[a]),user[listOfKeys[a]])
    return id1

def get(follow, x):
    k=0
    listOfKeys = list()
    listOfValues = follow.items()
    for key,values in listOfValues:
        for a in range(len(values)):
            if values[a] == x:
                listOfKeys.append(key)
                k+=1
    if k==0:
        print('No followers.')
    return  listOfKeys

def CommonFollow(id1,id2):
    x=id1
    y=id2
    k=0
    if follow.get(x,'None')=='None' or follow.get(y,'None')=='None':
        if user.get(x, "None")=="None" or user.get(y, "None")=="None":
            print('No such user.')
        else:
            print('No common follow.')
    else:
        for a in range(len(follow[x])):
            for b in range(len(follow[y])):
                if follow[x][a]== follow[y][b]:
                    print(follow[x][a],user[follow[x][a]])
                    k+=1
        if k==0:
            print('No common follow.')
    return id1,id2

def Recommend(id1):
    x=id1
    if user.get(x,'None')=='None':
        print('No such user.')
    elif follow.get(x,'None')!='None':
        inilist=follow.get(x)
        kkk=0
        finallist=[]
        outputlist=[]
        for a in range(len(inilist)):
            if follow.get(inilist[a],'None')!='None':
                locallist=follow.get(inilist[a])
                for j in locallist:
                    if j!=x:
                        if j not in follow.get(x):
                            finallist.append(str(j))
        for k in range(len(finallist)):
            if finallist[k] not in outputlist:
                if str(user.get(int(finallist[k])))!='None':
                    outputlist.append(finallist[k])
                    outputlist.append(outputlist[z])
                    outputlist.sort(str(user.get(int(outputlist[z])))+' '+'('+str(finallist.count(outputlist[z])))
        for z in range(len(outputlist)):
            print(str(outputlist[z])+' '+str(user.get(int(outputlist[z])))+' '+'('+str(finallist.count(outputlist[z]))+')')
            kkk+=1
        if kkk==0:
            print('No recommendation.')
    else:
            print('No recommendation.')
    return id1


def ShortestPath(src, des):
    q = []
    visited = []
    q.append([src])
    visited.append(src)
    while q:
        path = q.pop(0)
        current = path[-1]
        if current == des:
            for a in path:
                print (a,user.get(a))
            return
        for l in follow.get(current, []):
          if l not in visited:
            newpath = list(path)
            newpath.append(l)
            visited.append(l)
            q.append(newpath)
    print ("No path found.")

def main():
    command=input().split()
    while(command[0]!="END"):
        if (command[0]=="AddUser"):
            AddUser(int(command[1]),command[2])
        elif (command[0]=="AddFollow"):
            AddFollow(int(command[1]),int(command[2]))
        elif (command[0]=="CommonFollow"):
            CommonFollow(int(command[1]),int(command[2]))
        elif (command[0]=="ListFollower"):
            ListFollower(int(command[1]))        
        elif (command[0]=="Recommend"):
            Recommend(int(command[1]))
        elif (command[0]=="ShortestPath"):
            ShortestPath(int(command[1]),int(command[2]))
        command=input().split()
    return

main()
