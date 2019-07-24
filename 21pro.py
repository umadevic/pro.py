import statistics as st
value1=int(input())
arr=list(map(int,input().split()))
res=False
for i in range(1,value1):
    m1=arr[:i]
    m2=arr[i:]
    if st.mean(m1)==st.mean(m2):
        res=True
if res==True:
    print("yes")
else:
    print("no")
