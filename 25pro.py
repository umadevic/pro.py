#a
def LIS(arr,size):
    res1=[]
    value=1
    for i in range(0,size-1):
        if arr[i]<arr[i+1]:
            value+=1
        else:
            res1.append(value)
            value=1
    res1.append(value)
    print(max(res1))
size=int(input())
arr=list(map(int,input().split()))
LIS(arr,size)
