value1=int(input())
array=[]
su=[]
for i in range(value1):
    array.append(list(map(int,input().split())))
for llist in array:
    for num in llist:
        su.append(num)
su.sort()
for i in su:
    print(i,end=' ')
    #a
