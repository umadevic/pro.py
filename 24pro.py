#a
    
mi=int(input())
n9=2**mi
list1=[]
for i in range(0,n9):
    l=bin(i)[2:].zfill(mi)
    if(len(l)<len(bin(2**mi-1)[2:])):
        list1.append([l.count("1"),l])
    else:
        list1.append([l.count("1"),l])
list1.sort()
for i in range(len(list1)):
    print(list1[i][1])
