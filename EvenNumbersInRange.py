def evenNumInRange(arr,query):
    result=[]
    for q in query:
        start=q[0]
        end=q[1]
        
        count=0
        for i in range(start,end+1):
            if arr[i]%2==0:
                count+=1
        result.append(count)

    return result

arr=list(map(int,input().split()))
query=[]
q=int(input())
for i in range(q):
    query.append(list(map(int,input().split())))
print(evenNumInRange(arr,query))